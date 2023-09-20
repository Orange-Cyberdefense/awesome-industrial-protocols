# Turn/IP
# Claire-lex - 2023
# Main features for all user interfaces

"""Main features for all user interfaces with common commands."""

from sys import stderr
# Internal
from config import protocols as p, types
from db import MongoDB, DBException, exact_search
from db import Protocols, Links, Packets
from db import Protocol

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

def ERROR(msg: str, will_exit: bool = False):
    """Display error messages to terminal."""
    print("ERROR:", msg, file=stderr)
    if will_exit:
        exit(-1)

#-----------------------------------------------------------------------------#
# UI                                                                         #
#-----------------------------------------------------------------------------#

class UIError(Exception):
    """Exception class for user interface errors."""

class UI(object):
    """Main class for user interfaces."""

    def __init__(self):
        protocols = None
        links = None
        packets = None
        try:
            self.db = MongoDB()
        except DBException as dbe:
            raise UIError(dbe) from None
        self.protocols = Protocols()
        self.links = Links()
        self.packets = Packets()

    def view(self, field: str) -> dict:
        """View only the specified field for each protocol.

        Used by -V (CLI) and View box (TUI).
        Returns a dictionary where each entry is {protocol_name: field_content}.
        """
        vdict = {}
        for protocol in self.protocols.all_as_objects:
            try:
                vdict[protocol.name] = protocol.get(field)[1]
            except DBException as dbe:
                pass
        return vdict

    def search(self, search: str) -> dict:
        """Search string in selected fields of a protocol objects.

        Used by -S (CLI) and Search box (TUI).
        Returns a dictionary where each entry is {protocol_name: matching_field}.
        """
        sdict = {}
        search = search.lower() # Search is case-insensitive
        for protocol in self.protocols.all_as_objects:
            for key in p.SEARCHED_FIELDS:
                try: # Check if protocol exists
                    _, value = protocol.get(key)
                except DBException:
                    continue
                if p.TYPE(key) in [types.LINKLIST, types.PKTLIST]:
                    print("uilist")
                elif isinstance(value, list):
                    print("felfjzel")
                else:
                    if exact_search(value.lower(), search):
                        if not isinstance(sdict[protocol.name], dict):
                            sdict[protocol.name] = {}
                        sdict[protocol.name][key] = value
        # Debug
        for name, match in sdict:
            for k, v in match:
                print(name, k, v)
        return sdict

    def add(self, protocol: str) -> None:
        """Add protocol to the list of protocols.

        Used by -A (CLI) and TODO (TUI).
        """
        protocol = Protocol().create(name=protocol)
        try:
            self.protocols.add(protocol)
        except DBException as dbe:
            raise UIError(dbe) from None
