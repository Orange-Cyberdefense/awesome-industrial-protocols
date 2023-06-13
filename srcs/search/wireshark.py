# Turn/IP
# Claire-lex - 2023
# Interface to search for data in Wireshark dissectors

"""Search for data in Wireshark dissectors."""

from requests import get
from requests.exceptions import ConnectionError
from json import loads
from json.decoder import JSONDecodeError
from re import search as re_search
from os.path import join
from base64 import b64decode
# Internal
from config import wireshark as w
from db import search, has_common_items, Protocol
from . import SearchException

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_APICONN = "API is not reachable."
ERR_APIJSON = "Could not extract JSON."
ERR_BADTREE = "Invalid GitHub tree format."
ERR_DLCODE = "Dissector's code could not be retrieved ({0})."

#-----------------------------------------------------------------------------#
# Wireshark class                                                             #
#-----------------------------------------------------------------------------#

class Dissector(object):
    """Object representing data about a dissector."""
    raw = None

    def __init__(self, raw: dict):
        self.raw = raw
        self.api_url = raw["url"]
        self.code = self.__dl_code()

    def __str__(self):
        return "Dissector {0}: {1}".format(self.name, self.url)

    def __dl_code(self):
        """Retrieve the dissector's complete code from GitHub API."""
        dissector = Wireshark.get_api_json(self.api_url)
        if "content" not in dissector.keys():
            raise SearchException(ERR_DLCODE.format(self.name))
        content = b64decode(dissector["content"]).decode('utf-8')
        return content
    
    @property
    def name(self):
        return self.raw["path"]

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
    dissector = None
    
    def __init__(self):
        pass

    @staticmethod
    def get_api_json(url: str) -> list:
        """Get data from API and return it as a parsed JSON list."""
        try:
            api = get(url)
            json = loads(api.content)
            return json
        except ConnectionError:
            raise SearchException(ERR_APICONN) from None
        except JSONDecodeError:
            raise SearchException(ERR_APIJSON) from None
        return None

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
                    match = search(path.group(1), protocol.names, threshold=1)
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
        epan_tree = self.get_api_json(w.api_epan_folder)
        dissectors_sha = self.__search_in_dictlist("name", w.dissectors_folder,
                                                   "sha", epan_tree)
        if not dissectors_sha:
            raise SearchException("Dissector's SHA could not be retrieved.")
        # Get the tree corresponding to the SHA
        return self.get_api_json(join(w.api_trees, dissectors_sha))
        
    def __search_in_dictlist(self, searchkey: str, searchvalue: str,
                            requestedkey: str, listdict: list) -> object:
        """In a list of dictionaries, the return the value of
        listdict["requestedkey"] where listdict["searchkey"] == searchvalue.
        """
        for entry in listdict:
            if not isinstance(entry, dict):
                continue
            if searchkey not in entry.keys() or requestedkey not in entry.keys():
                continue
            if entry[searchkey] == searchvalue:
                return entry[requestedkey]
        return None

