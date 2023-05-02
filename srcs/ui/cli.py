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
from db import MongoDB, DBException

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

MSG_CONFIRM_ADD = "Do you want to add protocol '{0}'?"
MSG_CONFIRM_WRITE = "Do you want to store {0} to {1}?"

ERR_ACTION = "No is action defined. Choose between {0} (-h for help)."
ERR_WRITE = "Write requires data (-d) OR link (-l) (-h for help)."
ERR_UNKPROTO = "Protocol '{0}' does not exist."

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
            
    def run(self, argv: list=None):
        """Use arguments for command line to launch commands."""
        is_function = False
        for option in vars(self.options):
            value = getattr(self.options, option)
            if not value: # Argument is False or None
                continue
            if option in self.functions:
                is_function = True
                try:
                    self.functions[option]()
                except DBException as dbe:
                    ERROR(dbe)
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
        ct = 0
        for protocol in self.db.get_protocol():
            print("[{0}] {1}".format(ct, protocol["name"]))
            ct += 1

    def __cmd_read(self) -> None:
        self.__print_protocol(self.db.get_protocol(self.options.read))

    def __cmd_write(self) -> None:
        # Check what kind of data needs to be written
        # We use "is not" because we want one or the other, not both
        if (self.options.data != None) is (self.options.link != None):
            ERROR(ERR_WRITE, will_exit=True)
        # Does protocol exist?
        try:
            self.db.get_protocol(self.options.write)
        except DBException:
            ERROR(ERR_UNKPROTO.format(self.options.write), will_exit=False)
            # Protocol does not exist but can be added
            if not self.__cmd_add(self.options.write):
                return # Protocol was not created, leaving.
        # Now we need to parse the data or link to be stored.
        # TODO
        # And then we prepare for write to db
        # TODO
        # Ask for confirmation
        if self.__confirm(MSG_CONFIRM_WRITE.format("poulet", self.options.write),
                          self.options.force):
            # Actually write
            pass

    def __cmd_add(self, new: str=None) -> None:
        # Do something here
        return self.__confirm(MSG_CONFIRM_ADD.format(new), self.options.force)
        
    def __cmd_gen(self) -> None:
        print("elyeneratorrrr")

    def __cmd_check(self) -> None:
        print("uijeverifi")

    #--- Helpers -------------------------------------------------------------#
        
    def __print_protocol(self, protocol: dict) -> None:
        table_size = get_terminal_size().columns - 16 - 8
        table_format = "| {0: <16} | {1: <" + str(table_size) + "} |"
        for k, v in protocol.items():
            if k == "_id":
                continue
            v = ", ".join(v) if isinstance(v, list) else str(v)
            v = v if len(v) < table_size else v[:table_size-3]+"..."
            print(table_format.format(k.capitalize(), v))

    def __confirm(self, msg, force):
        confirm = True if force else False
        if not force:
            res = input("{0} [y/n]: ".format(msg))
            confirm = True if res in ("y","Y") else False
        return confirm
