# Turn/IP
# Claire-lex - 2023
# Interface to search for data in Wireshark dissectors

"""Search for data in Wireshark dissectors."""

from re import search as re_search
from os.path import join
# Internal
from config import wireshark as w
from db import find, has_common_items, Protocol
from . import SearchException, get_api_json, search_json, get_code_from_github

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_BADTREE = "Invalid GitHub tree format."

#-----------------------------------------------------------------------------#
# Wireshark classes                                                           #
#-----------------------------------------------------------------------------#

class Dissector(object):
    """Object representing data about a dissector."""
    raw = None

    def __init__(self, raw: dict):
        self.raw = raw
        self.name = raw["path"]
        self.api_url = raw["url"]
        self.code = get_code_from_github(self.api_url)

    def __str__(self):
        return "Dissector {0}: {1}".format(self.name, self.url)

    @property
    def url(self):
        return join(w.dissectors_url, self.raw["path"])

    @property
    def names(self):
        """List of names for the dissected protocols, extracted from code.

        We rely on arguments to function proto_register_protocol.
        """
        names = []
        for line in self.code.split("\n"):
            if w.naming_function in line:
                names = re_search("[^\(]\((.*?)\);", line)
                if names and len(names.groups()):
                    names = [x.replace("\"", "").strip() for x in names.group(1).split(",")]
                    return names
        return None
        
class Wireshark(object):
    """Interface to Wireshark dissectors code using GitHub's API."""
    
    def __init__(self):
        pass

    def get_dissector(self, protocol: Protocol):
        """Get the dissector corresponding to the protocol."""
        dissectors = self.__get_dissectors_tree()
        if "tree" not in dissectors.keys():
            raise SearchException(ERR_BADTREE)
        results = []
        for entry in dissectors["tree"]:
            if isinstance(entry, dict) and "path" in entry.keys():
                path = re_search("^packet-([^\.]+)\.c$", entry["path"])
                if path and len(path.groups()):
                    match = find(path.group(1), protocol.names, threshold=1)
                    if match:
                        results.append(Dissector(entry))
        # If multiple dissectors found, we want to check the list of names
        # in dissectors to see if it matches with the protocol we have.
        if len(results) > 1:
            for entry in results:
                if has_common_items(entry.names, protocol.names):
                    return [entry] # This one matches, it's enough
        return results
        
    def __get_dissectors_tree(self):
        """Get the SHA of the dissectors' folder tree.

        We have to use the Trees API because the content API only returns the
        1000 first results. Therefore :
        - We get the SHA of the dissector folder from the parent folder epan
        - We call the Trees API using this SHA.
        """
        # Get the SHA of the dissectors folder
        epan_tree = get_api_json(w.api_epan_folder)
        dissectors_tree = search_json("name", w.dissectors_folder, "git_url",
                                      epan_tree)
        if not dissectors_tree:
            raise SearchException("Dissector's tree could not be retrieved.")
        # Get the tree corresponding to the SHA
        return get_api_json(dissectors_tree)
