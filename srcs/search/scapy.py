# Turn/IP
# Claire-lex - 2023
# Interface to search for data in Scapy layers

"""Search for data in Scapy layers."""

from importlib.util import find_spec
from os.path import dirname, basename, join
from glob import glob
# Internal
from config import scapy as s
from db import find, has_common_items, Protocol
from . import SearchException, get_api_json

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_BADTREE = "Invalid GitHub tree format."

#-----------------------------------------------------------------------------#
# Scapy classes                                                               #
#-----------------------------------------------------------------------------#

class Layer(object):
    """Object representing data about a layer."""
    raw = None

    def __init__(self, raw: dict):
        self.raw = raw
        self.name = raw["name"]
        self.url = raw["html_url"].split("?")[0]
        # self.code = get_code_from_github(self.)

    @property
    def names(self):
        return self.name
        
    def __str__(self):
        return "Layer {0}: {1}".format(self.name, self.url)
        
class Scapy(object):
    """Interface to Scapy layers using GitHub's API and current install."""
    local_install = None

    def __init__(self):
        pass

    def __get_local_install(self):
        """Get Scapy's install directory if it is installed."""
        if find_spec("scapy"):
            import scapy
            self.scapy_directory = dirname(scapy.__file__)
            
    def get_layer(self, protocol: Protocol) -> list:
        """Get the Scapy layer corresponding to protocol from Github's API."""
        candidates = []
        layers = get_api_json(s.api_layers_folder)
        contrib = get_api_json(s.api_contrib_folder)
        if not isinstance(layers, list) or not isinstance(contrib, list):
            raise SearchException(ERR_BADTREE)
        for layer in layers + contrib:
            if isinstance(layer, dict) and "name" in layer.keys():
                match = find(layer["name"].replace(".py", ""), protocol.names, threshold=1)
                if match:
                    candidates.append(Layer(layer))
        return candidates
