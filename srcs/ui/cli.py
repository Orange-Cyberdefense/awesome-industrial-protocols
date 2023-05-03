# Turn/IP
# Claire-lex - 2023
# Command-line interface

"""Command-line interface
"""

from argparse import ArgumentParser
from os import get_terminal_size
from sys import stderr
# Internal
from config import TOOL_DESCRIPTION
from db import MongoDB, DBException, Protocols, Protocol

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

OPTIONS = (
    ("-L", "--list", "list all protocols", None, None),
    ("-R", "--read", "read data of a protocol", None, "protocol"),
    ("-W", "--write", "write data to a protocol", None, "protocol"),
    ("-G", "--gen", "generate Markdown files with protocols' data", None, None),
    ("-C", "--check", "check the database's content", None, None),
    ("-d", "--data", "values to change with format field:value (with -W)", None, "field:value"),
    ("-l", "--link", "link to add with format name:url (with -W)", None, "name:url"),
    ("-f", "--force", "do not ask for confirmation (with -W)", False, None)
)

MSG_PROTO_COUNT = "[*] Total number of protocols: {0}"
MSG_LINKS_COUNT = "[*] Total number of links: {0}"

MSG_CONFIRM_ADD = "Do you want to add protocol '{0}'?"
MSG_CONFIRM_WRITE = "Do you want to write '{0}: {1}' to {2} (previous value: {3})?"

ERR_ACTION = "No is action defined. Choose between {0} (-h for help)."
ERR_WRITE = "Write requires data (-d) OR link (-l) (-h for help)."
ERR_BADDATA = "Data to write is invalid (-h for help)."

def ERROR(msg: str, will_exit: bool=False):
    print("ERROR:", msg, file=stderr)
    if will_exit:
        exit(-1)

#-----------------------------------------------------------------------------#
# CLI                                                                         #
#-----------------------------------------------------------------------------#

class CLI(object):
    """Parse and run commands gathered from the command-line interface."""
    db = None
    options = None
    functions = None
    protocols = None

    def __init__(self):
        self.functions = {
            "list": self.__cmd_list,
            "read": self.__cmd_read,
            "write": self.__cmd_write,
            "gen": self.__cmd_gen,
            "check": self.__cmd_check
        }
        self.options = self.__init_options()
        try:
            self.db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
        self.protocols = Protocols()
            
    def run(self, argv: list=None):
        """Use arguments for command line to launch commands."""
        is_function = False
        for option in vars(self.options):
            value = getattr(self.options, option)
            if not value: # Argument is False or None
                continue
            if option in self.functions:
                is_function = True
                self.functions[option]()
        if not is_function:
            ERROR(ERR_ACTION.format(", ".join(self.functions)), will_exit=True)

    #-------------------------------------------------------------------------#
    # Private                                                                 #
    #-------------------------------------------------------------------------#

    def __init_options(self) -> object:
        options = ArgumentParser(description=TOOL_DESCRIPTION)
        for opt in OPTIONS:
            if not opt[4]: # Options takes no argument (so no meta)
                options.add_argument(opt[0], opt[1], help=opt[2],
                                     action="store_true", default=opt[3])
            else:
                options.add_argument(opt[0], opt[1], help=opt[2],
                                     metavar=opt[4], default=opt[3])
        return options.parse_args()

    #--- Commands ------------------------------------------------------------#
    
    def __cmd_list(self) -> None:
        pdict = {x.name: x.keywords for x in self.protocols.all}
        self.__print_table(pdict)
        # Stats
        print(MSG_PROTO_COUNT.format(self.protocols.count))
        print(MSG_LINKS_COUNT.format(self.db.links_count))

    def __cmd_read(self, protocol: str=None) -> None:
        try:
            protocol = protocol if protocol else self.options.read
            self.__print_table(self.protocols.get(protocol).to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __cmd_write(self) -> None:
        # Check what kind of data needs to be written
        # We use "is not" because we want one or the other, not both
        if (self.options.data != None) is (self.options.link != None):
            ERROR(ERR_WRITE, will_exit=True)
        # Does protocol exist?
        try:
            protocol = self.protocols.get(self.options.write)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)
            # Protocol does not exist but can be added
            if self.__cmd_add(self.options.write):
                self.__cmd_write() # We call the function again 8D
            return # Protocol was not created, leaving.
        # Now we need to parse the data or link to be stored.
        if self.options.data:
            self.__write_data(protocol, self.options.data)
        elif self.options.link:
            self.__write_link(protocol, self.options.link)

    def __cmd_add(self, new: str=None) -> None:
        # Do something here
        return self.__confirm(MSG_CONFIRM_ADD.format(new), self.options.force)
        
    def __cmd_gen(self) -> None:
        print("elyeneratorrrr")

    def __cmd_check(self) -> None:
        print("uijeverifi")

    #--- Handle data ---------------------------------------------------------#

    def __write_data(self, protocol:Protocol, data:str):
        """Write data with format field:value to protocol."""
        field, value = self.__parse_data(data)
        try:
            _, oldval = protocol.get(field)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True) # tmp
        if self.__confirm(MSG_CONFIRM_WRITE.format(field, value, protocol.name, oldval),
                          self.options.force):
            protocol.set(field, value)
            self.__cmd_read(protocol.name)

    def __write_link(self, protocol:Protocol, link:str):
        """Write link information with format name:url to protocol.
        We must first create the link in the Link connection.
        """
        name, url = self.__parse_data(link)
        if self.__confirm(MSG_CONFIRM_WRITE.format(name, url, protocol),
                          self.options.force):
            pass
        
    #--- Helpers -------------------------------------------------------------#
        
    def __print_table(self, protocol: dict) -> None:
        """Displays the protocol table on terminal."""
        full_table_size = get_terminal_size().columns
        table_size = full_table_size - 16 - 8
        table_format = "| {0: <16} | {1: <" + str(table_size) + "} |"
        print("-" * (full_table_size - 1))
        for k, v in protocol.items():
            if k == "_id":
                continue
            v = ", ".join(v) if isinstance(v, list) else str(v)
            v = v if len(v) < table_size else v[:table_size-3]+"..."
            print(table_format.format(k, v))
        print("-" * (full_table_size - 1))

    def __parse_data(self, data) -> tuple:
        """Translates from str field:value to tuple (field, value)."""
        field = data[:data.find(":")].strip()
        value = data[data.find(":")+1:].strip()
        if data.find(":") < 0 or not field or not value:
            ERROR(ERR_BADDATA, will_exit=True)
        return field, value

    def __confirm(self, msg, force):
        """Interactively ask for confirmation from the user."""
        confirm = True if force else False
        if not force:
            res = input("{0} [y/n]: ".format(msg))
            confirm = True if res in ("y","Y") else False
        return confirm
