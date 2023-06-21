# Turn/IP
# Claire-lex - 2023
# Interface to search for data in Scapy layers
# pylint: disable=redefined-builtin

"""Functions for data search using JSON APIs (GitHub)."""

from base64 import b64decode
from json import loads
from json.decoder import JSONDecodeError
from requests import get
from requests.exceptions import ConnectionError

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_APICONN = "API is not reachable."
ERR_APIJSON = "Could not extract JSON."
ERR_DLCODE = "Code could not be retrieved from API ({0})."

#-----------------------------------------------------------------------------#
# Search helpers                                                              #
#-----------------------------------------------------------------------------#

class SearchException(Exception):
    """Exception class for automated search-related errors."""
    pass

#--- Extract data from JSON APIs ---------------------------------------------#

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

def search_json(searchkey: str, searchvalue: str, requestedkey: str, listdict:
                list) -> object:
    """In a list of dictionaries (JSON), return listdict["requestedkey"] where
    listdict["searchkey"] == searchvalue.
    """
    for entry in listdict:
        if not isinstance(entry, dict):
            continue
        if searchkey not in entry.keys() or requestedkey not in entry.keys():
            continue
        if entry[searchkey] == searchvalue:
            return entry[requestedkey]
    return None

#--- GitHub API specific -----------------------------------------------------#

def get_code_from_github(api_url: str) -> str:
    """Retrieve a component's complete code from GitHub API."""
    component = get_api_json(api_url)
    if "content" not in component.keys():
        raise SearchException(ERR_DLCODE.format(api_url))
    content = b64decode(component["content"]).decode('utf-8')
    return content
