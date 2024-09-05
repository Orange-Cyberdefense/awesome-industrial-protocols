# Turn/IP
# Claire-lex - 2023
# Command-line interface
# pylint: disable=invalid-name,too-few-public-methods,redefined-builtin,no-self-use
# pylint: disable=redefined-outer-name,too-many-arguments,simplifiable-if-expression

"""Command-line interface."""

from argparse import ArgumentParser
from os import get_terminal_size
from os.path import exists, join
from subprocess import run as subprocess_run, CalledProcessError
from textwrap import fill
from bson.objectid import ObjectId
# Internal
from config import TOOL_DESCRIPTION, protocols as p, packets as pk
from config import links, types, mongodb, wireshark, scapy
from db import DBException
from db import Protocol, Link
from out import Markdown, MDException
from fetch import FetchException, Wireshark, Scapy, CVEList, Youtube
from .ui import UI, ERROR

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

OPTIONS = (
    # Behavior
    ("-f", "--force", "never ask for confirmation", False, None),
    # View
    ("-S", "--search", "list protocols matching the search", None, "search"),
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
    ("-WP", "--write-packet", "change data of a packet", None,
     ("protocol", "name", "field", "value"), 4),
    ("-DP", "--delete-packet", "delete a packet", None, ("protocol", "name"), 2),
    # Output
    ("-G", "--gen", "generate Markdown files with protocols' data", None, None),
    ("-C", "--check", "check the database's content", None, None),
    # Note
    ("-N", "--note", "add personal notes for a protocol", None, "protocol"),
    # Automated fetch
    ("-F", "--fetch", "fetch data from various sources", None, ("source", "protocol"), 2),
    # Database
    ("-MI", "--mongoimport", "Import database from JSON files in repository.", False, None),
    ("-ME", "--mongoexport", "Export database to JSON files in repository.", False, None)
)

MSG_PROTO_COUNT = "[*] Total number of protocols: {0}"
MSG_LINKS_COUNT = "[*] Total number of links: {0}"
MSG_PACKETS_COUNT = "[*] Total number of packets: {0}"
MSG_WRITE_ALIST = "Awesome list written to {0}."
MSG_WRITE_PPAGE = "{0} protocol page written to {1}."
MSG_DISSECTOR_EXISTS = "Dissector {0} already exists for protocol {1}."
MSG_LAYER_EXISTS = "Layer {0} already exists for protocol {1}."
MSG_EXISTS = "'{0}' already exists for protocol {1}."
MSG_MULTILAYER = "Multiple matching layers found: {0}."
MSG_CVE_WAIT = "Fetching CVEs in NIST's database (it may take some time)."

MSG_CONFIRM_ADD_PROTO = "Do you want to add protocol '{0}'?"
MSG_CONFIRM_ADD_FIELD = "Do you want to add field '{0}' to protocol '{1}'?"
MSG_CONFIRM_ADD_LINK = "Do you want to add link '{0}'?"
MSG_CONFIRM_ADD_PACKET = "Do you want to add packet '{0}'?"
MSG_CONFIRM_WRITE = "Do you want to write '{0}: {1}' to '{2}' (previous value: '{3}')?"
MSG_CONFIRM_APPEND = "Do you want to append '{0}' to field '{1}'?"
MSG_CONFIRM_DELETE = "Do you really want to delete protocol '{0}'? (ALL DATA WILL BE LOST)"
MSG_CONFIRM_DELETE_LINK = "Do you really want to delete '{0}'?"
MSG_CONFIRM_DELETE_LINK_FROM = "Link '{0}' is associated to protocol {1}. Delete?"
MSG_CONFIRM_DELETE_PACKET = "Do you really want to delete '{0}' ({1})?"
MSG_CONFIRM_OVERWRITE = "File '{0}' already exists. Overwrite?"
MSG_CONFIRM_ADDDISSECTOR = "Do you want to set dissector {0} for protocol {1}?"
MSG_CONFIRM_ADDLAYER = "Do you want to set layer {0} for protocol {1}?"
MSG_CONFIRM_ADDCVE = "Do you want to add {0} to protocol {1}?"
MSG_CONFIRM_ADDVIDEO = "Do you want to add video '{0}' to protocol {1}?"

ERR_ACTION = "No action is defined. Choose between {0} (-h for help)."
ERR_WRITE = "Write requires data (-d) OR link (-l) (-h for help)."
ERR_BADDATA = "Data to write is invalid (-h for help)."
ERR_BADID = "The ID is invalid (-h for help)."
ERR_LINKEXISTS = "Link '{0}' already exists."
ERR_NOFIELD = "Field '{0}' does not exist in any protocol."
ERR_PACKETEXISTS = "Packet '{0}' already exists for protocol {1}."
ERR_FETCHSOURCE = "Fetch source not found. Choose between {0} (-h for help)."
ERR_NODISSECTOR = "No dissector found for protocol {0}."
ERR_NOLAYER = "No layer found for protocol {0}."
ERR_NOCVE = "No CVE found for protocol {0}."
ERR_NOVID = "No video found for protocol {0}."
ERR_GOOGLEAPI = "To use Youtube search you need google-api-python-client." \
                "(pip install google-api-python-client)."

#-----------------------------------------------------------------------------#
# CLI                                                                         #
#-----------------------------------------------------------------------------#

class CLI(UI):
    """Parse and run commands gathered from the command-line interface."""
    db = None
    options = None
    functions = None

    #-------------------------------------------------------------------------#
    # Prepare arguments and run                                               #
    #-------------------------------------------------------------------------#

    def __init__(self):
        super().__init__()
        self.functions = {
            "search": self.__cmd_search,
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
            "fetch": self.__cmd_fetch,
            "mongoimport": self.__cmd_mongoimport,
            "mongoexport": self.__cmd_mongoexport
        }
        self.options = self.__init_options()

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
    # View and search                                                         #
    #-------------------------------------------------------------------------#

    def __cmd_search(self, search: str = None) -> None:
        """-S / --search"""
        search = search if search else self.options.search
        search = search.lower()
        # self.search(search)
        searched_fields = p.ALL_FIELDS.keys()
        results = {}
        for protocol in self.protocols.all_as_objects:
            for key in searched_fields:
                try:
                    _, value = protocol.get(key)
                except DBException:
                    continue
                if p.TYPE(key)in [types.LINKLIST, types.PKTLIST]:
                    if p.TYPE(key) == types.LINKLIST:
                        lst = [self.links.get_id(x) for x in value]
                    elif p.TYPE(key) == types.PKTLIST:
                        lst = [self.packets.get_id(x) for x in value]
                    value = " ".join([x.name for x in lst] + \
                                     [x.description for x in lst])
                else:
                    value = " ".join(value) if isinstance(value, list) else str(value)
                if search in value.lower():
                    # This sucks: very new matching field for the protocol
                    # erases the previous one...
                    results[protocol.name] = protocol.get(key)[1]
        if results:
            self.__print_table(results, nocap=True)

    def __cmd_view(self, field: str = None) -> None:
        """-V / --view"""
        field = field if field else self.options.view
        result = self.view(field)
        if result:
            self.__print_table(result, nocap=True)

    #-------------------------------------------------------------------------#
    # Protocols                                                               #
    #-------------------------------------------------------------------------#

    def __get_protocol(self, protocol: str, noadd: bool = False) -> Protocol:
        """Helper: Return a Protocol object from its name, or create it."""
        try:
            self.protocols.get(protocol)
        except DBException as dbe: # Does not exist or multiple matches
            ERROR(str(dbe), will_exit=bool(noadd))
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
        print(MSG_PACKETS_COUNT.format(self.packets.count))

    def __cmd_add(self, protocol: str = None) -> bool:
        """-A / --add"""
        protocol = protocol if protocol else self.options.add
        if not self.__confirm(MSG_CONFIRM_ADD_PROTO.format(protocol),
                              self.options.force):
            return False
        try:
            self.protocols.add(Protocol(name=protocol))
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        self.__cmd_read(protocol)
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
            if p.TYPE(field) in (types.LIST, types.LINKLIST, types.PKTLIST):
                # If it's a link, we need a link object
                if self.__confirm(MSG_CONFIRM_APPEND.format(value, p.NAME(field)),
                                  self.options.force):
                    if p.TYPE(field) == types.LINKLIST:
                        link = self.__cmd_add_link(value, value)
                        if not link:
                            return
                        value = link._id
                    elif p.TYPE(field) == types.PKTLIST:
                        packet = self.packets.get(protocol, value)
                        if not packet or isinstance(packet, list):
                            return
                        value = packet._id
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
                description = description if description else ""
                type = type if type else links.DEFAULT_TYPE
                link = self.links.add(Link(name=name, url=url,
                                           description=description, type=type))
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
            if self.__confirm(MSG_CONFIRM_WRITE.format(field, value, link.url, oldvalue),
                              self.options.force):
                link.set(field, value)
                self.__cmd_read_link(link.url)
        except DBException as dbe:
            ERROR(dbe, will_exit=True)

    def __cmd_delete_link(self) -> None:
        """-DL / --delete-link"""
        try:
            links = self.links.get(self.options.delete_link, multimatch=True)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)
        links = links if isinstance(links, list) else [links]
        for link in links:
            # We want to erase all occurrences of this link in protocols
            for p in self.protocols.list:
                protocol = self.protocols.get(p)
                if protocol.has_link(link):
                    if self.__confirm(MSG_CONFIRM_DELETE_LINK_FROM.format(link.url,
                                                                          protocol.name),
                                      self.options.force):
                        protocol.delete_link(link)
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
                         description: str = None, scapy_pkt: str = None,
                         raw_pkt: str = None):
        """-AP / --add-packet"""
        if self.options.add_packet:
            protocol, name = self.options.add_packet
        try:
            # packets.add checks that too but we need to do that before confirmation
            packet = self.packets.get(protocol, name)
            ERROR(ERR_PACKETEXISTS.format(packet.name, protocol.name), will_exit=True)
        except DBException: # Packet does not exist, we can continue
            pass
        if self.__confirm(MSG_CONFIRM_ADD_PACKET.format(name, protocol),
                          self.options.force):
            try:
                protocol = self.__get_protocol(protocol)
                self.packets.add(Packet(protocol=protocol.name, name=name,
                                        description=description,
                                        scapy_pkt=scapy_pkt, raw_pkt=raw_pkt))
            except DBException as dbe:
                ERROR(str(dbe), will_exit=True)

    def __cmd_read_packet(self, protocol: str = None, name: str = None) -> None:
        """-RP / --read-packet"""
        if self.options.read_packet:
            protocol, name = self.options.read_packet
        protocol = self.__get_protocol(protocol, noadd=True)
        try:
            packets = self.packets.get(protocol, name)
            packets = packets if isinstance(packets, list) else [packets]
            for packet in packets:
                self.__print_table(packet.to_dict())
        except DBException as dbe:
            ERROR(str(dbe), will_exit=False)

    def __cmd_write_packet(self, protocol: str = None, name: str = None,
                           field: str = None, value: str = None) -> None:
        """-WP / --write-packet"""
        if self.options.write_packet:
            protocol, name, field, value = self.options.write_packet
        try:
            protocol = self.protocols.get(protocol)
            packet = self.packets.get(protocol, name)
            oldvalue = packet.get(field)
            if self.__confirm(MSG_CONFIRM_WRITE.format(
                    field, value, packet.name, oldvalue),
                              self.options.force):
                packet.set(field, value)
            self.__cmd_read_packet(protocol.name, packet.name)
        except DBException as dbe:
            ERROR(str(dbe), will_exit=True)

    def __cmd_delete_packet(self):
        """-DP / --delete-packet"""
        protocol, name = self.options.delete_packet
        try:
            protocol = self.__get_protocol(protocol, noadd=True)
            packet = self.packets.get(protocol.name, name)
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
                path = md_generator.gen_protocol_page(protocol, self.links,
                                                      self.packets, write=False)
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
    # Automated fetch                                                         #
    #-------------------------------------------------------------------------#

    def __cmd_fetch(self, source: str = None, protocol: str = None) -> None:
        """-F / --fetch"""
        sources = {
            "wireshark": self.__cmd_fetch_wireshark,
            "scapy": self.__cmd_fetch_scapy,
            "cve": self.__cmd_fetch_cve,
            "youtube": self.__cmd_fetch_youtube
        }
        if not source and not protocol:
            source, protocol = self.options.fetch
        if protocol == "all":
            for p in self.protocols.all_as_objects:
                self.__cmd_fetch(source, p)
        else:
            if not isinstance(protocol, Protocol):
                protocol = self.__get_protocol(protocol)
            if source.lower() == "all":
                for src in sources:
                    sources[src.lower()](protocol)
            elif source.lower() not in sources.keys():
                ERROR(ERR_FETCHSOURCE.format(", ".join(sources.keys())), will_exit=True)
            else:
                sources[source.lower()](protocol)

    def __cmd_fetch_wireshark(self, protocol: Protocol) -> None:
        """-F wireshark / --fetch wireshark"""
        try:
            candidates = Wireshark().get_dissector(protocol)
            current_list = [self.links.get_id(x).url for x in protocol.wireshark]
            if len(candidates) < 1:
                ERROR(ERR_NODISSECTOR.format(protocol.name))
                return
            for dissector in candidates:
                if dissector.url in current_list:
                    print(MSG_DISSECTOR_EXISTS.format(dissector.name, protocol.name))
                elif self.__confirm(MSG_CONFIRM_ADDDISSECTOR.format(
                        dissector.name, protocol.name), self.options.force):
                    description = wireshark.dissector_desc.format(protocol.name)
                    link = self.__cmd_add_link(dissector.name, dissector.url,
                                               description, "tool")
                    if link:
                        protocol.set(p.wireshark, link._id, replace=True)
        except FetchException as se:
            ERROR(str(se))

    def __cmd_fetch_scapy(self, protocol: Protocol) -> None:
        """-F scapy / --fetch scapy"""
        try:
            candidates = Scapy().get_layer(protocol)
            current_list = [self.links.get_id(x).url for x in protocol.scapy]
            if len(candidates) < 1:
                ERROR(ERR_NOLAYER.format(protocol.name))
                return
            for layer in candidates:
                if layer.url in current_list:
                    print(MSG_LAYER_EXISTS.format(layer.name, protocol.name))
                elif self.__confirm(MSG_CONFIRM_ADDLAYER.format(layer.name,
                                                              protocol.name),
                                  self.options.force):
                    description = scapy.layer_desc.format(protocol.name)
                    link = self.__cmd_add_link(layer.name, layer.url,
                                               description, "tool")
                    if link:
                        protocol.set(p.scapy, link._id, replace=True)
        except FetchException as se:
            ERROR(str(se))

    def __cmd_fetch_cve(self, protocol: Protocol) -> None:
        """-F cve / --fetch cve"""
        try:
            print(MSG_CVE_WAIT)
            candidates = CVEList().fetch_by_keywords(protocol)
            current_list = [self.links.get_id(x).name for x in protocol.get(p.cve)[1]]
            if not candidates:
                ERROR(ERR_NOCVE.format(protocol.name))
        except FetchException as se:
            ERROR(str(se))
            return
        for c in candidates:
            try:
                if self.links.has(c.url) and c.id in current_list:
                    print(MSG_EXISTS.format(c.id, protocol.name))
                    continue # Skipping the ones we already have
                self.__box_print(c.id, c.url, c.description)
                if self.__confirm(MSG_CONFIRM_ADDCVE.format(c.id,
                                                            protocol.name),
                                  self.options.force):
                    link = self.__cmd_add_link(c.id, c.url, c.description,
                                               "cve")
                    if link:
                        try:
                            protocol.set(p.cve, link._id)
                        except DBException as dbe:
                            ERROR(str(dbe))
            except FetchException as se:
                ERROR(str(se))

    def __cmd_fetch_youtube(self, protocol: Protocol) -> None:
        """-F youtube / --fetch youtube"""
        try:
            candidates = Youtube().get_videos(protocol)
            current_list = [self.links.get_id(x).url for x in protocol.resources]
            if not candidates:
                ERROR(ERR_NOVID.format(protocol.name))
        except FetchException as se:
            ERROR(str(se))
            return
        except ModuleNotFoundError:
            ERROR(ERR_GOOGLEAPI)
            return
        for c in candidates:
            try:
                if c.url in current_list:
                    print(MSG_EXISTS.format(c.title, protocol.name))
                    continue
                self.__box_print(str(c), c.url, c.description)
                if self.__confirm(MSG_CONFIRM_ADDVIDEO.format(c.title,
                                                              protocol.name),
                                  self.options.force):
                    link = self.__cmd_add_link(c.title, c.url,
                                               "@ {0} ({1})".format(c.channel, c.year),
                                               "conference")
                    if link:
                        try:
                            protocol.set(p.resources, link._id)
                        except DBException as dbe:
                            ERROR(str(dbe))
            except FetchException as se:
                ERROR(str(se))

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
        try:
            subprocess_run(cmd + proto, check=True)
            subprocess_run(cmd + links, check=True)
            subprocess_run(cmd + packets, check=True)
        except CalledProcessError as cpe:
            ERROR(str(cpe))

    def __cmd_mongoexport(self) -> None:
        "-ME / --mongoexport"
        cmd = ["mongoexport", "--db=\"{0}\"".format(mongodb.database)]
        protofile = join(mongodb.dbfile_path, mongodb.dbfile_protocols)
        linksfile = join(mongodb.dbfile_path, mongodb.dbfile_links)
        packetsfile = join(mongodb.dbfile_path, mongodb.dbfile_packets)
        proto = ["--collection=protocols", "--out=\"{0}\"".format(protofile)]
        links = ["--collection=links", "--out=\"{0}\"".format(linksfile)]
        packets = ["--collection=packets", "--out=\"{0}\"".format(packetsfile)]
        try:
            subprocess_run(cmd + proto, check=True)
            subprocess_run(cmd + links, check=True)
            subprocess_run(cmd + packets, check=True)
        except CalledProcessError as cpe:
            ERROR(str(cpe))

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

    def __print_ids(self, table_format: str, key: str, ids: list) -> None:
        """Print documents from their ID."""
        full_table_size = get_terminal_size().columns
        table_size = full_table_size - 20 - 8
        key = p.NAME(key) if key in p.ALL_FIELDS else key
        if not isinstance(ids, list):
            print(table_format.format(key, ERR_BADID))
            return
        for id in ids:
            try:
                link = self.links.get_id(id)
                text = "{0}: {1}".format(link.name, link.url)
            except DBException as dbe:
                try:
                    packet = self.packets.get_id(id)
                    text = "{0}: {1}".format(packet.name, packet.description)
                except DBException as dbe:
                    text = str(dbe)
            text = text if len(text) < table_size else text[:table_size-3]+"..."
            print(table_format.format(key, text))
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
            if isinstance(v, list) and isinstance(v[0], ObjectId):
                self.__print_ids(table_format, k, v)
            else:
                v = ", ".join(v) if isinstance(v, list) else str(v)
                v = v if len(v) < table_size else v[:table_size-3]+"..."
                if k in p.ALL_FIELDS:
                    k = p.NAME(k)
                elif k in pk.FIELDS.keys(): # Packets
                    k = pk.FIELDS[k]
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
