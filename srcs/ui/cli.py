# Turn/IP
# Claire-lex - 2023
# Command-line interface

"""Command-line interface
"""

from argparse import ArgumentParser
from os import get_terminal_size
from sys import stderr
# Internal
from config import TOOL_DESCRIPTION, mongodb, protocols, AI_WARNING
from db import MongoDB, DBException, Protocols, Protocol, Links, Link

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

OPTIONS = (
    ("-L", "--list", "list all protocols", None, None),
    ("-F", "--filter", "list protocols according to filter", None, "filter"),
    ("-A", "--add", "add a new protocol", None, "protocol"),
    ("-R", "--read", "read data of a protocol", None, "protocol"),
    ("-W", "--write", "write data to a protocol", None, "protocol"),
    ("-D", "--delete", "delete a protocol", None, "protocol"),
    ("-AI", "--ask_ai", "search data for a protocol using IA", None, "protocol"),
    ("-N", "--note", "add personal notes for a protocol", None, "protocol"),
    ("-LL", "--list-links", "list all links", None, None),
    ("-AL", "--add-link", "add a new link", None, "description:url"),
    ("-RL", "--read-link", "read data of a link", None, "url"),
    ("-WL", "--write-link", "change data of a link", None, "url"),
    ("-DL", "--delete-link", "delete a link", None, "url"),
    ("-G", "--gen", "generate Markdown files with protocols' data", None, None),
    ("-C", "--check", "check the database's content", None, None),
    ("-d", "--data", "values to change with format field:value (with -W)", None, "field:value"),
    ("-l", "--link", "link to add with format name:url (with -W)", None, "description:url"),
    ("-f", "--force", "do not ask for confirmation (with -W)", False, None)
)

MSG_PROTO_COUNT = "[*] Total number of protocols: {0}"
MSG_LINKS_COUNT = "[*] Total number of links: {0}"

MSG_CONFIRM_ADD_PROTO = "Do you want to add protocol '{0}'?"
MSG_CONFIRM_ADD_FIELD = "Do you want to add field '{0}' protocol {1}?"
MSG_CONFIRM_ADD_LINK = "Do you want to add link '{0}'?"
MSG_CONFIRM_ADD_LINK_PROTO = "Do you want to add link '{0}: {1}' to protocol {2}?"
MSG_CONFIRM_WRITE = "Do you want to write '{0}: {1}' to {2} (previous value: {3})?"
MSG_CONFIRM_DELETE = "Do you really want to delete protocol {0}? (ALL DATA WILL BE LOST)"

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
    links = None

    def __init__(self):
        self.functions = {
            "list": self.__cmd_list,
            "filter": self.__cmd_filter,
            "add": self.__cmd_add,
            "read": self.__cmd_read,
            "write": self.__cmd_write,
            "delete": self.__cmd_delete,
            "ask_ai": self.__cmd_ask_ai,
            "note": self.__cmd_note,
            "list_links": self.__cmd_list_links,
            "add_link": self.__cmd_add_link,
            "write_link": self.__cmd_write_link,
            "delete_link": self.__cmd_delete_link,
            "gen": self.__cmd_gen,
            "check": self.__cmd_check
        }
        self.options = self.__init_options()
        try:
            self.db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
        self.protocols = Protocols()
        self.links = Links()

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
        """-L / --list"""
        pdict = {x.name: x.keywords for x in self.protocols.all_as_objects}
        self.__print_table(pdict)
        # Stats
        print(MSG_PROTO_COUNT.format(self.protocols.count))
        print(MSG_LINKS_COUNT.format(self.links.count))

    def __cmd_filter(self) -> None:
        """-F / --filter"""
        raise NotImplementedError("CLI: filter")
        
    def __cmd_add(self, new: str=None) -> bool:
        """-A / --add"""
        new = new if new else self.options.add
        if not self.__confirm(MSG_CONFIRM_ADD_PROTO.format(new), self.options.force):
            return False
        protocol = Protocol().create(name=new)
        print(protocol)
        self.protocols.add(protocol)
        self.__cmd_read(new)
        return True
        
    def __cmd_read(self, protocol: str=None) -> None:
        """-R / --read"""
        try:
            protocol = protocol if protocol else self.options.read
            self.__print_table(self.protocols.get(protocol).to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __cmd_write(self) -> None:
        """-W / --write"""
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

    def __cmd_delete(self) -> None:
        """-D / --delete"""
        try:
            protocol = self.protocols.get(self.options.delete) # Will raise if unknown
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        if self.__confirm(MSG_CONFIRM_DELETE.format(protocol.name),
                          self.options.force):
            self.protocols.delete(protocol)

    def __cmd_ask_ai(self) -> None:
        """-AI / --ask-ai"""
        try:
            from auto import AI
        except ImportError:
            ERROR("OpenAI not found (pip install openai)", will_exit=True)
        print(AI_WARNING)
        # Check if protocol exists, if not create it.
        try:
            ai = AI()
            # TODO : replace with scenario
            print(ai.request("write a 4 lines poem about seagulls"))
        except AIError as aie:
            ERROR(str(aie), will_exit=True)
            
    def __cmd_note(self) -> None:
        """-N / --note"""
        raise NotImplementedError("CLI: note")
            
    def __cmd_list_links(self) -> None:
        """-LL / --links"""
        for links in self.links.all:
            print(links)

    def __cmd_add_link(self, new: str=None) -> None:
        """-AL / --add-link"""
        new = new if new else self.options.add_link
        description, url = self.__parse_data(new)
        try:
            # links.add checks that too but we need to do that before confirmation
            self.links.get(new)
        except DBException: # Link does not exist, we can continue
            pass
        if self.__confirm(MSG_CONFIRM_ADD_LINK.format(new), self.options.force):
            link = self.links.add(url, description)

    def __cmd_read_link(self) -> None:
        """-RL / --read-link"""
        raise NotImplementedError("CLI: read link")

    def __cmd_write_link(self) -> None:
        """-WL / --write-link"""
        raise NotImplementedError("CLI: write link")

    def __cmd_delete_link(self) -> None:
        """-DL / --delete-link"""
        raise NotImplementedError("CLI: delete link")
        
    def __cmd_gen(self) -> None:
        """-G / --gen"""
        raise NotImplementedError("CLI: generate files")

    def __cmd_check(self) -> None:
        """-C / --check"""
        raise NotImplementedError("CLI: check database")

    #--- Handle data ---------------------------------------------------------#

    def __write_data(self, protocol:Protocol, data:str):
        """Write data with format field:value to protocol."""
        field, value = self.__parse_data(data)
        try:
            _, oldval = protocol.get(field)
        except DBException as dbe: # Field does not exist
            ERROR(str(dbe), will_exit=False)
            if self.__confirm(MSG_CONFIRM_ADD_FIELD.format(field,
                                                           protocol.name),
                                  self.options.force):
                protocol.add(field, value)
                self.__cmd_read(protocol.name)                
        else: # Field exists
            if self.__confirm(MSG_CONFIRM_WRITE.format(field, value, protocol.name,
                                                       oldval), self.options.force):
                protocol.set(field, value)
                self.__cmd_read(protocol.name)
            
    def __write_link(self, protocol:Protocol, link:str):
        """Write link information with format name:url to protocol.
        We must first create the link in the Link connection.
        """
        description, url = self.__parse_data(link)
        # Check if link already exists, create it if not
        try:
            link = self.links.get(url)
        except DBException: # Link does not exist, we create it
            link = None
        # Actually create and associate the link
        if self.__confirm(MSG_CONFIRM_ADD_LINK_PROTO.format(url, description,
                                                            protocol.name),
                          self.options.force):
            link = link if link else self.links.add(url, description)
            protocol.add_link(link.id)
            # Add to protocol link list
        
    #--- Helpers -------------------------------------------------------------#

    def __print_links(self, table_format, key, link_ids: list) -> None:
        """Print links from ID."""
        for id in link_ids:
            try:
                link = str(self.links.get_id(id))
            except DBException as dbe:
                link = str(dbe)
            print(table_format.format(key, link))
            key = "" # We only want to print the key for the first line
    
    def __print_table(self, protocol: dict) -> None:
        """Displays the protocol table on terminal."""
        full_table_size = get_terminal_size().columns
        table_size = full_table_size - 16 - 8
        table_format = "| {0: <16} | {1: <" + str(table_size) + "} |"
        print("-" * (full_table_size - 1))
        for k, v in protocol.items():
            if k == mongodb.id:
                continue
            elif k == protocols.resources:
                self.__print_links(table_format, k, v)
            else:
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
