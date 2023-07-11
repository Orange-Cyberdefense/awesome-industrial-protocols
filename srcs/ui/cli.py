# Turn/IP
# Claire-lex - 2023
# Command-line interface
# pylint: disable=invalid-name,too-few-public-methods,redefined-builtin,no-self-use
# pylint: disable=redefined-outer-name

"""Command-line interface."""

from argparse import ArgumentParser
from os import get_terminal_size
from os.path import exists, join
from sys import stderr
from subprocess import run as subprocess_run
from textwrap import fill
from bson.objectid import ObjectId
# Internal
from config import TOOL_DESCRIPTION, AI_WARNING, protocols as p
from config import links, types, mongodb, wireshark, scapy
from db import MongoDB, DBException
from db import Protocols, Protocol, Links, Link, Packets, Packet
from out import Markdown, MDException
from search import SearchException, AI, Wireshark, Scapy, CVEList, Youtube

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

OPTIONS = (
    # Behavior
    ("-f", "--force", "never ask for confirmation", False, None),
    # View
    ("-F", "--filter", "list protocols matching a filter", None, "filter"),
    ("-V", "--view", "view only a field of each protocol", None, "field"),
    # Protocols
    ("-L", "--list", "list all protocols", None, None),
    ("-A", "--add", "add a new protocol", None, "protocol"),
    ("-R", "--read", "read data of a protocol", None, "protocol"),
    ("-W", "--write", "write data to a protocol", None, ("protocol", "field", "value"), 3),
    ("-D", "--delete", "delete a protocol", None, "protocol"),
    # Links
    ("-LL", "--list-links", "list all links", None, None),
    ("-AL", "--add-link", "add a new link", None, ("name", "url"), 2),
    ("-RL", "--read-link", "read data of a link", None, "url"),
    ("-WL", "--write-link", "change data of a link", None, ("url", "field", "value"), 3),
    ("-DL", "--delete-link", "delete a link", None, "url"),
    # Packets
    ("-LP", "--list-packets", "list all packets", None, None),
    ("-RP", "--read-packet", "read a packet from a protocol", None, ("protocol", "name"), 2),
    ("-AP", "--add-packet", "add a new packet", None, ("protocol", "name"), 2),
    ("-WP", "--write-packet", "change data of a packet", None, ("protocol", "name"), 2),
    ("-DP", "--delete-packet", "delete a packet", None, ("protocol", "name"), 2),
    # Output
    ("-G", "--gen", "generate Markdown files with protocols' data", None, None),
    ("-C", "--check", "check the database's content", None, None),
    # Note
    ("-N", "--note", "add personal notes for a protocol", None, "protocol"),
    # Automated search
    ("-S", "--search", "search for data from various sources", None, ("method", "protocol"), 2),
    # Database
    ("-MI", "--mongoimport", "Import database from JSON files in repository.", False, None),
    ("-ME", "--mongoexport", "Export database to JSON files in repository.", False, None)
)

MSG_PROTO_COUNT = "[*] Total number of protocols: {0}"
MSG_LINKS_COUNT = "[*] Total number of links: {0}"
MSG_WRITE_ALIST = "Awesome list written to {0}."
MSG_WRITE_PPAGE = "{0} protocol page written to {1}."
MSG_MULTIDISSECTOR = "Multiple matching dissectors found: {0}."
MSG_MULTILAYER = "Multiple matching layers found: {0}."
MSG_CVE_WAIT = "Searching for CVEs in NIST's database (it may take some time)."

MSG_CONFIRM_ADD_PROTO = "Do you want to add protocol '{0}'?"
MSG_CONFIRM_ADD_FIELD = "Do you want to add field '{0}' to protocol '{1}'?"
MSG_CONFIRM_ADD_LINK = "Do you want to add link '{0}'?"
MSG_CONFIRM_ADD_PACKET = "Do you want to add packet '{0}'?"
MSG_CONFIRM_WRITE = "Do you want to write '{0}: {1}' to '{2}' (previous value: '{3}')?"
MSG_CONFIRM_WRITE_LINK = "Do you want to write '{0}: {1}' to '{2}' (previous value: '{3}')?"
MSG_CONFIRM_APPEND = "Do you want to append '{0}' to field '{1}'?"
MSG_CONFIRM_DELETE = "Do you really want to delete protocol '{0}'? (ALL DATA WILL BE LOST)"
MSG_CONFIRM_DELETE_LINK = "Do you really want to delete '{0}'?"
MSG_CONFIRM_DELETE_PACKET = "Do you really want to delete '{0}' ({1})?"
MSG_CONFIRM_OVERWRITE = "File '{0}' already exists. Overwrite?"
MSG_CONFIRM_ADDDISSECTOR = "Do you want to set dissector {0} for protocol {1}?"
MSG_CONFIRM_ADDLAYER = "Do you want to set layer {0} for protocol {1}?"
MSG_CONFIRM_ADDCVE = "Do you want to add {0} to protocol {1}?"
MSG_CONFIRM_ADDVIDEO = "Do you want to add video '{0}' to protocol {1}?"

ERR_ACTION = "No action is defined. Choose between {0} (-h for help)."
ERR_WRITE = "Write requires data (-d) OR link (-l) (-h for help)."
ERR_BADDATA = "Data to write is invalid (-h for help)."
ERR_BADLINK = "Link is invalid (-h for help)."
ERR_LINKEXISTS = "Link '{0}' already exists."
ERR_NOFIELD = "Field '{0}' does not exist in any protocol."
ERR_PACKETEXISTS = "Packet '{0}' already exists for protocol {1}."
ERR_OPENAI = "OpenAI not found (pip install openai)."
ERR_SEARCHMETHOD = "Search method not found. Choose between {0} (-h for help)."
ERR_NODISSECTOR = "No dissector found for protocol {0}."
ERR_NOLAYER = "No layer found for protocol {0}."
ERR_GOOGLEAPI = "To use Youtube search you need google-api-python-client." \
                "(pip install google-api-python-client)."

def ERROR(msg: str, will_exit: bool = False):
    """Display error messages to terminal."""
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

    #-------------------------------------------------------------------------#
    # Prepare arguments and run                                               #
    #-------------------------------------------------------------------------#
    
    def __init__(self):
        self.functions = {
            "filter": self.__cmd_filter,
            "view": self.__cmd_view,
            "list": self.__cmd_list,
            "add": self.__cmd_add,
            "read": self.__cmd_read,
            "write": self.__cmd_write,
            "delete": self.__cmd_delete,
            "note": self.__cmd_note,
            "list_links": self.__cmd_list_links,
            "add_link": self.__cmd_add_link,
            "read_link": self.__cmd_read_link,
            "write_link": self.__cmd_write_link,
            "delete_link": self.__cmd_delete_link,
            "list_packets": self.__cmd_list_packets,
            "add_packet": self.__cmd_add_packet,
            "read_packet": self.__cmd_read_packet,
            "write_packet": self.__cmd_write_packet,
            "delete_packet": self.__cmd_delete_packet,
            "gen": self.__cmd_gen,
            "check": self.__cmd_check,
            "search": self.__cmd_search,
            "mongoimport": self.__cmd_mongoimport,
            "mongoexport": self.__cmd_mongoexport
        }
        self.options = self.__init_options()
        try:
            self.db = MongoDB()
        except DBException as dbe:
            if not self.options.mongoimport:
                ERROR(dbe, will_exit=True)
        self.protocols = Protocols()
        self.links = Links()
        self.packets = Packets()

    def __init_options(self) -> object:
        """Parse command line arguments."""
        options = ArgumentParser(description=TOOL_DESCRIPTION)
        for opt in OPTIONS:
            if not opt[4]: # Options takes no argument (so no meta)
                options.add_argument(opt[0], opt[1], help=opt[2],
                                     action="store_true", default=opt[3])
            elif len(opt) == 6:
                options.add_argument(opt[0], opt[1], help=opt[2], nargs=opt[5],
                                     metavar=opt[4], default=opt[3])
            else:
                options.add_argument(opt[0], opt[1], help=opt[2],
                                     metavar=opt[4], default=opt[3])
        return options.parse_args()
        
    def run(self):
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
    # Show and filter                                                         #
    #-------------------------------------------------------------------------#

    def __cmd_filter(self, filter = None) -> None:
        """-F / --filter"""
        filter = filter if filter else self.options.filter
        filter = filter.lower()
        searched_fields = p.ALL_FIELDS.keys()
        results = {}
        for protocol in self.protocols.all_as_objects:
            for key in searched_fields:
                _, value = protocol.get(key)
                if p.TYPE(key) == types.LINKLIST:
                    links = [self.links.get_id(x) for x in value]
                    value = " ".join([x.name for x in links] + \
                                     [x.description for x in links])
                else:
                    value = " ".join(value) if isinstance(value, list) else str(value)
                if filter in value.lower():
                    results[protocol.name] = protocol.get(key)[1]
        if results:
            self.__print_table(results, nocap=True)
    
    def __cmd_view(self, field = None) -> None:
        """-V / --view"""
        field = field if field else self.options.view
        at_least_one_proto_has_field = False
        pdict = {}
        for protocol in self.protocols.all_as_objects:
            try:
                _, content = protocol.get(field)
                pdict[protocol.name] = content
                at_least_one_proto_has_field = True
            except DBException as dbe:
                pass
        if not at_least_one_proto_has_field:
            ERROR(ERR_NOFIELD.format(field), will_exit=True)
        self.__print_table(pdict, nocap=True)

    #-------------------------------------------------------------------------#
    # Protocols                                                               #
    #-------------------------------------------------------------------------#

    def __get_protocol(self, protocol: str, noadd: bool = False) -> Protocol:
        """Helper: Return a Protocol object from its name, or create it."""
        try:
            self.protocols.get(protocol)
        except DBException as dbe: # Does not exist or multiple matches
            ERROR(str(dbe), will_exit=True if noadd else False)
            self.__cmd_add(protocol)
        # We check again if the protocol exists now.
        try:
            protocol = self.protocols.get(protocol)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        return protocol
    
    def __cmd_list(self) -> None:
        """-L / --list"""
        pdict = {x.name: x.description for x in self.protocols.all_as_objects}
        self.__print_table(pdict, nocap=True)
        # Stats
        print(MSG_PROTO_COUNT.format(self.protocols.count))
        print(MSG_LINKS_COUNT.format(self.links.count))
        
    def __cmd_add(self, new: str = None) -> bool:
        """-A / --add"""
        new = new if new else self.options.add
        if not self.__confirm(MSG_CONFIRM_ADD_PROTO.format(new), self.options.force):
            return False
        protocol = Protocol().create(name=new)
        try:
            self.protocols.add(protocol)
        except DBException as dbe:
            ERROR(dbe, will_exit=True)
        self.__cmd_read(new)
        return True

    def __cmd_read(self, protocol: str = None) -> None:
        """-R / --read"""
        try:
            protocol = protocol if protocol else self.options.read
            self.__print_table(self.protocols.get(protocol).to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __write_field(self, protocol: Protocol, field: str, value: str,
                      oldvalue: str):
        """Used by -W"""
        try:
            if p.TYPE(field) in (types.LIST, types.LINKLIST):
                # If it's a link, we need a link object
                if self.__confirm(MSG_CONFIRM_APPEND.format(value, p.NAME(field)),
                                  self.options.force):
                    if p.TYPE(field) == types.LINKLIST:
                        link = self.__cmd_add_link(value, value)
                        if not link:
                            return
                        value = link.id
                    protocol.set(field, value)
            else:
                if self.__confirm(MSG_CONFIRM_WRITE.format(p.NAME(field), value,
                                                           protocol.name,
                                                           oldvalue),
                                  self.options.force):
                    protocol.set(field, value)
        except DBException as dbe:
            ERROR(dbe, will_exit=True)

    def __cmd_write(self) -> None:
        """-W / --write"""
        protocol, field, value = self.options.write
        # Does protocol exist?
        protocol = self.__get_protocol(protocol)
        try:
            field, oldvalue = protocol.get(field)
        except DBException: # Field does not exist
            if self.__confirm(MSG_CONFIRM_ADD_FIELD.format(field,
                                                           protocol.name),
                              self.options.force):
                protocol.add(field, value)
        else: # Field exists, should we append or replace ?
            self.__write_field(protocol, field, value, oldvalue)
        self.__cmd_read(protocol.name)

    def __cmd_delete(self) -> None:
        """-D / --delete"""
        protocol = self.__get_protocol(self.options.delete, noadd=True)
        if self.__confirm(MSG_CONFIRM_DELETE.format(protocol.name),
                          self.options.force):
            self.protocols.delete(protocol)

    #-------------------------------------------------------------------------#
    # Links                                                                   #
    #-------------------------------------------------------------------------#
            
    def __cmd_list_links(self) -> None:
        """-LL / --list-links"""
        for link in self.links.all_as_objects:
            print(link)

    def __cmd_add_link(self, name: str = None, url: str = None,
                       description: str = None, type: str = None) -> Link:
        """-AL / --add-link"""
        if self.options.add_link:
            name, url = self.options.add_link
        try:
            # links.add checks that too but we need to do that before confirmation
            link = self.links.get(url)
            ERROR(ERR_LINKEXISTS.format(link.url))
            return link
        except DBException: # Link does not exist, we can continue
            pass
        if self.__confirm(MSG_CONFIRM_ADD_LINK.format(url), self.options.force):
            try:
                link = self.links.add(name, url, description if description else
                                      "", type if type else links.DEFAULT_TYPE)
                return link
            except DBException as dbe:
                ERROR(str(dbe), will_exit=True)
        return None

    def __cmd_read_link(self, link: str = None) -> None:
        """-RL / --read-link"""
        try:
            link = link if link else self.options.read_link
            self.__print_table(self.links.get(link).to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __cmd_write_link(self, url: str = None, field: str = None,
                         value: str = None) -> None:
        """-WL / --write-link"""
        if self.options.write_link:
            url, field, value = self.options.write_link
        try:
            link = self.links.get(url)
            oldvalue = link.get(field)
            if self.__confirm(MSG_CONFIRM_WRITE_LINK.format(field, value, link.url, oldvalue),
                              self.options.force):
                link.set(field, value)
                self.__cmd_read_link(link.url)
        except DBException as dbe:
            ERROR(dbe, will_exit=True)

    def __cmd_delete_link(self) -> None:
        """-DL / --delete-link"""
        try:
            links = self.links.get(self.options.delete_link, no_raise=True)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        links = links if isinstance(links, list) else [links]
        for link in links:
            if self.__confirm(MSG_CONFIRM_DELETE_LINK.format(link.url),
                              self.options.force):
                self.links.delete(link)

    #-------------------------------------------------------------------------#
    # Packets                                                                 #
    #-------------------------------------------------------------------------#
                
    def __cmd_list_packets(self) -> None:
        """-LP / --list-packets"""
        for packet in self.packets.all_as_objects:
            print(packet)
                
    def __cmd_add_packet(self, protocol: str = None, name: str = None,
                         description: str = None, raw: str = None,
                         scapy: str = None) -> Packet:
        """-AL / --add-packet"""
        if self.options.add_packet:
            protocol, name = self.options.add_packet
        protocol = self.__get_protocol(protocol)
        try:
            # packets.add checks that too but we need to do that before confirmation
            packet = self.packets.get(protocol, name)
            ERROR(ERR_PACKETEXISTS.format(packet.name, protocol.name), will_exit=True)
        except DBException: # Packet does not exist, we can continue
            pass
        if self.__confirm(MSG_CONFIRM_ADD_PACKET.format(name, protocol),
                          self.options.force):
            try:
                packet = self.packets.add(protocol, name)
                return packet
            except DBException as dbe:
                ERROR(str(dbe), will_exit=True)
        return None

    def __cmd_read_packet(self, protocol: str = None, name: str = None) -> None:
        """-RP / --read-packet"""
        protocol, name = protocol if protocol else self.options.read_packet
        protocol = self.__get_protocol(protocol, noadd=True)
        try:
            packets = self.packets.get(protocol, name)
            packets = packets if isinstance(packets, list) else [packets]
            for packet in packets:
                self.__print_table(packet.to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __cmd_write_packet(self):
        """-WP / --write-packet"""
        pass

    def __cmd_delete_packet(self):
        """-DP / --delete-packet"""
        protocol, name = self.options.delete_packet
        protocol = self.__get_protocol(protocol, noadd=True)
        try:
            packet = self.packets.get(protocol, name)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        if self.__confirm(MSG_CONFIRM_DELETE_PACKET.format(packet.name,
                                                           protocol.name),
                          self.options.force):
            self.packets.delete(protocol, packet)
            
    #-------------------------------------------------------------------------#
    # Output                                                                  #
    #-------------------------------------------------------------------------#
            
    def __cmd_gen(self) -> None:
        """-G / --gen"""
        try:
            md_generator = Markdown()
            # Awesome list
            path = md_generator.gen_awesome_list(self.protocols, self.links, write=False)
            if exists(path):
                if self.__confirm(MSG_CONFIRM_OVERWRITE.format(path), self.options.force):
                    md_generator.write_awesome()
                    print(MSG_WRITE_ALIST.format(path))
            else:
                md_generator.write_awesome()
                print(MSG_WRITE_ALIST.format(path))
            # Protocol pages
            for protocol in self.protocols.all_as_objects:
                path = md_generator.gen_protocol_page(protocol, self.links, write=False)
                if exists(path):
                    if self.__confirm(MSG_CONFIRM_OVERWRITE.format(path), self.options.force):
                        md_generator.write_protocol_page()
                        print(MSG_WRITE_PPAGE.format(protocol.name, path))
                else:
                    md_generator.write_protocol_page()
                    print(MSG_WRITE_PPAGE.format(protocol.name, path))
        except MDException as mde:
            ERROR(mde, will_exit=True)

    def __cmd_check(self) -> None:
        """-C / --check"""
        for issue in self.protocols.check():
            print(issue)
        for issue in self.links.check():
            print(issue)

    #-------------------------------------------------------------------------#
    # Automated search                                                        #
    #-------------------------------------------------------------------------#
            
    def __cmd_search(self, method: str = None, protocol:str = None) -> None:
        """-S / --search"""
        methods = {
            "openai": self.__cmd_search_openai,
            "wireshark": self.__cmd_search_wireshark,
            "scapy": self.__cmd_search_scapy,
            "cve": self.__cmd_search_cve,
            "youtube": self.__cmd_search_youtube
        }
        if not method and not protocol:
            method, protocol = self.options.search
        if protocol == "all":
            for p in self.protocols.all_as_objects:
                self.__cmd_search(method, p)
        else:
            if not isinstance(protocol, Protocol):
                protocol = self.__get_protocol(protocol)
            if method.lower() == "all":
                for method in methods:
                    if method != "openai":
                        methods[method.lower()](protocol)
            elif method.lower() not in methods.keys():
                ERROR(ERR_SEARCHMETHOD.format(", ".join(methods.keys())), will_exit=True)
            else:
                methods[method.lower()](protocol)

    def __cmd_search_openai(self, protocol: Protocol) -> None:
        """-S openai / --search openai"""
        try:
            ai = AI()
            print(AI_WARNING)
            for q, a in ai.protocol_generator(protocol.name):
                self.__write_field(protocol, q, a, getattr(protocol, q))
        except SearchException as se:
            ERROR(str(se), will_exit=True)
        except ModuleNotFoundError:
            ERROR(ERR_OPENAI, will_exit=True)

    def __cmd_search_wireshark(self, protocol: Protocol) -> None:
        """-S wireshark / --search wireshark"""
        try:
            candidates = Wireshark().get_dissector(protocol)
            if len(candidates) < 1:
                ERROR(ERR_NODISSECTOR.format(protocol.name))
            elif len(candidates) > 1:
                d = ", ".join([x.name for x in candidates])
                print(MSG_MULTIDISSECTOR.format(d))
            else:
                dissector = candidates[0]
                if self.__confirm(MSG_CONFIRM_ADDDISSECTOR.format(
                        dissector.name, protocol.name), self.options.force):
                    description = wireshark.dissector_desc.format(protocol.name)
                    link = self.__cmd_add_link(dissector.name, dissector.url,
                                               description, "tool")
                    if link:
                        protocol.set(p.wireshark, link.id, replace=True)
        except SearchException as se:
            ERROR(str(se), will_exit=True)

    def __cmd_search_scapy(self, protocol: Protocol) -> None:
        """-S scapy / --search scapy"""
        try:
            candidates = Scapy().get_layer(protocol)
            if len(candidates) < 1:
                ERROR(ERR_NOLAYER.format(protocol.name))
            elif len(candidates) > 1:
                d = ", ".join([x.name for x in candidates])
                print(MSG_MULTILAYER.format(d))
            else:
                layer = candidates[0]
                if self.__confirm(MSG_CONFIRM_ADDLAYER.format(layer.name,
                                                              protocol.name),
                                  self.options.force):
                    description = scapy.layer_desc.format(protocol.name)
                    link = self.__cmd_add_link(layer.name, layer.url,
                                               description, "tool")
                    if link:
                        protocol.set(p.scapy, link.id, replace=True)
        except SearchException as se:
            ERROR(str(se), will_exit=True)

    def __cmd_search_cve(self, protocol: Protocol) -> None:
        """-S cve / --search cve"""
        try:
            current_list = [self.links.get_id(x).name for x in protocol.get(p.cve)[1]]
            print(MSG_CVE_WAIT)
            candidates = CVEList().search_by_keywords(protocol)
            for c in candidates:
                if self.links.has(c.url) and c.id in current_list:
                    continue # Skipping the ones we already have
                self.__box_print(c.id, c.url, c.description)
                if self.__confirm(MSG_CONFIRM_ADDCVE.format(c.id,
                                                            protocol.name),
                                  self.options.force):
                    link = self.__cmd_add_link(c.id, c.url, c.description,
                                               "cve")
                    if link:
                        try:
                            protocol.set(p.cve, link.id)
                        except DBException as dbe:
                            ERROR(str(dbe))
        except SearchException as se:
            ERROR(str(se), will_exit=True)

    def __cmd_search_youtube(self, protocol: Protocol) -> None:
        """-S youtube / --search youtube"""
        try:
            candidates = Youtube().get_videos(protocol)
            for c in candidates:
                self.__box_print(str(c), c.url, c.description)
                if self.__confirm(MSG_CONFIRM_ADDVIDEO.format(c.title,
                                                              protocol.name),
                                  self.options.force):
                    link = self.__cmd_add_link(c.title, c.url,
                                               "@ {0} ({1})".format(c.channel, c.year),
                                               "conference")
                    if link:
                        try:
                            protocol.set(p.resources, link.id)
                        except DBException as dbe:
                            ERROR(str(dbe))
        except SearchException as se:
            ERROR(str(se), will_exit=True)
        except ModuleNotFoundError:
            ERROR(ERR_GOOGLEAPI, will_exit=True)

    #-------------------------------------------------------------------------#
    # Notes                                                                   #
    #-------------------------------------------------------------------------#
            
    def __cmd_note(self) -> None:
        """-N / --note"""
        raise NotImplementedError("CLI: note")

    #-------------------------------------------------------------------------#
    # Database                                                                #
    #-------------------------------------------------------------------------#
    
    def __cmd_mongoimport(self) -> None:
        "-MI / --mongoimport"
        cmd = ["mongoimport", "--db=\"{0}\"".format(mongodb.database), "--drop"]
        protofile = join(mongodb.dbfile_path, mongodb.dbfile_protocols)
        linksfile = join(mongodb.dbfile_path, mongodb.dbfile_links)
        packetsfile = join(mongodb.dbfile_path, mongodb.dbfile_packets)
        proto = ["--collection=protocols", "--file=\"{0}\"".format(protofile)]
        links = ["--collection=links", "--file=\"{0}\"".format(linksfile)]
        packets = ["--collection=packets", "--file=\"{0}\"".format(packetsfile)]
        subprocess_run(cmd + proto)
        subprocess_run(cmd + links)
        subprocess_run(cmd + packets)

    def __cmd_mongoexport(self) -> None:
        "-ME / --mongoexport"
        cmd = ["mongoexport", "--db=\"{0}\"".format(mongodb.database)]
        protofile = join(mongodb.dbfile_path, mongodb.dbfile_protocols)
        linksfile = join(mongodb.dbfile_path, mongodb.dbfile_links)
        packetsfile = join(mongodb.dbfile_path, mongodb.dbfile_packets)
        proto = ["--collection=protocols", "--out=\"{0}\"".format(protofile)]
        links = ["--collection=links", "--out=\"{0}\"".format(linksfile)]
        packets = ["--collection=packets", "--out=\"{0}\"".format(packetsfile)]
        subprocess_run(cmd + proto)
        subprocess_run(cmd + links)
        subprocess_run(cmd + packets)

    #-------------------------------------------------------------------------#
    # Terminal display                                                        #
    #-------------------------------------------------------------------------#

    def __box_print(self, title: str, url: str, description: str) -> None:
        """Display information in ASCII boxes."""
        table_size = get_terminal_size().columns
        text_size = table_size - 4
        table_format = "| {0: <" + str(text_size) + "} |"
        print("-" * (table_size - 1))
        for t in fill(title, text_size).split("\n"):
            print(table_format.format(t))
        for u in fill(url, text_size).split("\n"):
            print(table_format.format(u))
        print("-" * (table_size - 1))
        for d in fill(description, text_size).split("\n"):
            print(table_format.format(d))
        print("-" * (table_size - 1))

    def __print_links(self, table_format, key, link_ids: list) -> None:
        """Print links from ID."""
        full_table_size = get_terminal_size().columns
        table_size = full_table_size - 20 - 8
        if not isinstance(link_ids, list):
            print(table_format.format(key, ERR_BADLINK))
            return
        for id in link_ids:
            try:
                link = self.links.get_id(id).url
                link = link if len(link) < table_size else link[:table_size-3]+"..."
            except DBException as dbe:
                link = str(dbe)
            print(table_format.format(key, link))
            key = "" # We only want to print the key for the first line

    def __print_table(self, protocol: dict, nocap: bool = False) -> None:
        """Displays the protocol table on terminal."""
        full_table_size = get_terminal_size().columns
        table_size = full_table_size - 20 - 8
        table_format = "| {0: <20} | {1: <" + str(table_size) + "} |"
        print("-" * (full_table_size - 1))
        for k, v in protocol.items():
            if k == mongodb.id:
                continue
            elif k in p.ALL_FIELDS and p.TYPE(k) == types.LINKLIST and v:
                self.__print_links(table_format, p.NAME(k), v)
            elif v and isinstance(v, list) and isinstance(v[0], ObjectId):
                self.__print_links(table_format, p.NAME(k), v)
            else:
                v = ", ".join(v) if isinstance(v, list) else str(v)
                v = v if len(v) < table_size else v[:table_size-3]+"..."
                if k in p.ALL_FIELDS:
                    k = p.NAME(k)
                else:
                    k = k if nocap else k.capitalize()
                print(table_format.format(k, v))
        print("-" * (full_table_size - 1))

    def __confirm(self, msg: str, force: bool):
        """Interactively ask for confirmation from the user."""
        confirm = True if force else False
        if not force:
            res = input("{0} [y/n]: ".format(msg))
            confirm = True if res in ("y", "Y") else False
        return confirm
