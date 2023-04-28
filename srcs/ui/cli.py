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

MSG_CONFIRM_WRITE = "Are you sure you want to store {0} to {1}? [y/n]: "

ERR_ACTION = "No is action defined. Choose between {0} (-h for help)."
ERR_WRITE = "Write requires data (-d) OR link (-l) (-h for help)."

def ERROR(msg: str, will_exit: bool=False):
    print("ERROR:", msg, file=stderr)
    if will_exit:
        exit(-1)

#-----------------------------------------------------------------------------#
# CLI                                                                         #
#-----------------------------------------------------------------------------#

class CLI(object):
    """TODO"""
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

    def __cmd_list(self) -> None:
        try:
            db = MongoDB()
            ct = 0
            for protocol in db.get_protocol():
                print("[{0}] {1}".format(ct, protocol["name"]))
                ct += 1
        except DBException as dbe:
            ERROR(dbe)

    def __cmd_read(self) -> None:
        try:
            db = MongoDB()
            self.__print_protocol(db.get_protocol(self.options.read))
        except DBException as dbe:
            ERROR(dbe)

    def __cmd_write(self) -> None:
        def confirm_write(force):
            confirm_write = True if force else False
            if not force:
                res = input(MSG_CONFIRM_WRITE.format("poulet", "roti"))
                confirm_write = True if res in ("y","Y") else False
            return confirm_write
        # Check what kind of data needs to be written
        # We use "is not" because we want one or the other, not both
        if (self.options.data != None) is (self.options.link != None):
            ERROR(ERR_WRITE, will_exit=True)
        # Ask for confirmation
        if confirm_write(self.options.force):
            # WRITE HERE
            pass

    def __cmd_gen(self) -> None:
        print("elyeneratorrrr")

    def __cmd_check(self) -> None:
        print("uijeverifi")

    def __print_protocol(self, protocol: dict) -> None:
        table_size = get_terminal_size().columns - 16 - 8
        table_format = "| {0: <16} | {1: <" + str(table_size) + "} |"
        for k, v in protocol.items():
            if k == "_id":
                continue
            v = ", ".join(v) if isinstance(v, list) else str(v)
            v = v if len(v) < table_size else v[:table_size-3]+"..."
            print(table_format.format(k.capitalize(), v))
