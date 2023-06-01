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
# Internal
from config import wireshark as w
from db import search

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_APICONN = "API is not reachable."
ERR_APIJSON = "Could not extract JSON."
ERR_BADTREE = "Invalid GitHub tree format."

#-----------------------------------------------------------------------------#
# Wireshark class                                                             #
#-----------------------------------------------------------------------------#

class WSException(Exception):
    pass

class Dissector(object):
    """Object representing data about a dissector."""
    raw = None
    def __init__(self, raw: dict):
        self.raw = raw

    def __str__(self):
        return self.raw

    @property
    def name(self):
        return self.raw["path"]
        
class Wireshark(object):
    """Interface to Wireshark dissectos code using GitHub's API."""
    dissector = None
    
    def __init__(self):
        pass

    def get_dissector(self, names):
        """Get the dissector corresponding to the protocol."""
        dissectors = self.__get_dissectors_tree()
        if "tree" not in dissectors.keys():
            raise WSException(ERR_BADTREE)
        results = []
        for entry in dissectors["tree"]:
            if isinstance(entry, dict) and "path" in entry.keys():
                protocol = re_search("^packet-([^\.]+)\.c$", entry["path"])
                if protocol and len(protocol.groups()):
                    match = search(protocol.group(1), names, threshold=1)
                    if match:
                        results.append(entry)
        return [Dissector(x) for x in results]
        
    def __get_dissectors_tree(self):
        """Get the SHA of the dissectors' folder tree.

        We have to use the Trees API because the content API only returns the
        1000 first results. Therefore :
        - We get the SHA of the dissector folder from the parent folder epan
        - We call the Trees API using this SHA.
        """
        # Get the SHA of the dissectors folder
        epan_tree = self.__get_api_json(w.api_epan_folder)
        dissectors_sha = self.__search_in_dictlist("name", w.dissectors_folder,
                                                   "sha", epan_tree)
        if not dissectors_sha:
            raise WSException("Dissector's SHA could not be retrieved.")
        # Get the tree corresponding to the SHA
        return self.__get_api_json(join(w.api_trees, dissectors_sha))
        
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
        
    def __get_api_json(self, url: str) -> list:
        """Get data from API and return it as a parsed JSON list."""
        try:
            api = get(url)
            json = loads(api.content)
            return json
        except ConnectionError:
            raise WSException(ERR_APICONN) from None
        except JSONDecodeError:
            raise WSException(ERR_APIJSON) from None
        return None
