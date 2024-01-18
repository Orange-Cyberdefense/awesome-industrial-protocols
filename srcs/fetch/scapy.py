# Turn/IP
# Claire-lex - 2023
# Interface to search for data in Scapy layers
# pylint: disable=too-few-public-methods,no-self-use,import-outside-toplevel

"""Search for data in Scapy layers."""

from importlib.util import find_spec
from os.path import dirname
# Internal
from config import scapy as s
from db import search, Protocol
from . import FetchException, get_api_json

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_BADTREE = "Invalid GitHub tree for protocol {0} (API limit exceeded?)."

#-----------------------------------------------------------------------------#
# Scapy classes                                                               #
#-----------------------------------------------------------------------------#

class Layer():
    """Object representing data about a layer."""
    raw = None

    def __init__(self, raw: dict):
        self.raw = raw
        self.name = raw["name"]
        self.url = raw["html_url"].split("?")[0]
        # self.code = get_code_from_github(self.)

    @property
    def names(self):
        """Return all the names but so far there's only one name..."""
        return self.name

    def __str__(self):
        return "Layer {0}: {1}".format(self.name, self.url)

class Scapy():
    """Interface to Scapy layers using GitHub's API and current install."""
    local_install = None

    def __init__(self):
        pass

    def __get_local_install(self):
        """Get Scapy's install directory if it is installed."""
        if find_spec("scapy"):
            import scapy
            self.local_install = dirname(scapy.__file__)

    def get_layer(self, protocol: Protocol) -> list:
        """Fetch the Scapy layer corresponding to protocol from Github's API."""
        candidates = []
        layers = get_api_json(s.api_layers_folder)
        contrib = get_api_json(s.api_contrib_folder)
        if not isinstance(layers, list) or not isinstance(contrib, list):
            raise FetchException(ERR_BADTREE.format(protocol.name))
        for layer in layers + contrib:
            if isinstance(layer, dict) and "name" in layer.keys():
                match = search(layer["name"].replace(".py", ""), protocol.names, threshold=1)
                if match:
                    candidates.append(Layer(layer))
        return candidates
