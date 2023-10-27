# Turn/IP
# Claire-lex - 2023
# Markdown text generator
# pylint: disable=invalid-name,no-self-use,unnecessary-lambda,too-many-instance-attributes

"""Markdown text generator."""

from os.path import join, exists
from re import sub
# Internal
from config import markdown as m, LIST_TITLE, LIST_DESCRIPTION, LIST_LOGO, \
    protocols as p, types, links as l, packets as pk
from db import DBException, Protocols, Protocol, Links, Packets

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_NOTEMFILE = "Template file '{0}' does not exist."

H1 = lambda x: "# {0}".format(x)
H2 = lambda x: "## {0}".format(x)
H3 = lambda x: "### {0}".format(x)

LINK_FORMAT = lambda x: sub(r'[^0-9a-zA-Z\-]+', '', x.lower().strip().replace(" ", "-"))

INTLINK = lambda x: "[{0}](#{1})".format(x, LINK_FORMAT(x))
IMG = lambda x, y: "![{0}]({1})".format(x, y)

LINKOBJ = lambda x: "[{0}]({1})".format(x.name, x.url)
LINKOBJDESC = lambda x: "[{0}]({1}) - {2}".format(x.name, x.url, x.description)

PACKETOBJ = lambda x: "**{0}**: {1}".format(x.name, x.description)

LINK = lambda x, y: "[{0}]({1})".format(x, y)
TABLE = lambda x, y: "| {0} | {1} |".format(x, y)
BORDER_TABLE = "|---|---|"

#-----------------------------------------------------------------------------#
# Markdown class                                                              #
#-----------------------------------------------------------------------------#

class MDException(Exception):
    """Exception class for Markdown generated-related errors."""

class Markdown():
    """Class to convert data to Markdown."""
    alist_template = None
    alist_file = None
    packets = None
    ppage_template = None
    ppage_file = None
    protocols = None
    links = None
    awesome_list = None
    protocol_page = None

    def __init__(self):
        self.alist_template = join(m.templates_path, m.awesomelist_template)
        self.alist_file = join(m.awesomelist_path, m.awesomelist_name)
        self.ppage_template = join(m.templates_path, m.protocolpage_template)
        # Check files
        for md in [self.alist_template, self.ppage_template]:
            if not exists(md):
                raise MDException(ERR_NOTEMFILE.format(md))

    #--- Public --------------------------------------------------------------#

    def write_awesome(self):
        """We split the call to generator and writer to ask for confirmation."""
        with open(self.alist_file, "w") as fd:
            fd.write("\n".join(self.awesome_list))
            fd.write("\n")

    def write_protocol_page(self):
        """We split the call to generator and writer to ask for confirmation."""
        with open(self.ppage_file, "w") as fd:
            fd.write("\n".join(self.protocol_page))
            fd.write("\n")

    def gen_awesome_list(self, protocols: Protocols, links: Links, write=True) -> str:
        """Convert protocols to a nice awesome list in Markdown."""
        self.protocols = protocols.all_as_objects
        self.links = links
        keywords = {
            m.f_title: self.__f_title,
            m.f_description: self.__f_description,
            m.f_logo: self.__f_logo,
            m.f_toc: self.__f_toc,
            m.f_content: self.__f_content
        }
        final = []
        for line in self.__read(self.alist_template):
            if line in keywords.keys():
                line = keywords[line]()
            final.append(line)
        self.awesome_list = final
        # Store to file
        if write:
            self.write_awesome()
        return self.alist_file

    def gen_protocol_page(self, protocol: Protocol, links: Links, packets: Packets,
                          write=True) -> str:
        """Convert a protocol object to a nice protocol page in Markdown."""
        self.links = links
        self.packets = packets
        filename = "{0}.md".format(LINK_FORMAT(protocol.name))
        self.ppage_file = join(m.protocolpage_path, filename)
        keywords = {
            m.f_name: self.__f_name,
            m.f_table: self.__f_table,
            m.f_resources: self.__f_resources
        }
        final = []
        for line in self.__read(self.ppage_template):
            if line in keywords.keys():
                line = keywords[line](protocol)
            final.append(line)
        self.protocol_page = final
        # Store to file
        if write:
            self.write_protocol_page()
        return self.ppage_file

    #--- Private -------------------------------------------------------------#

    def __read(self, template_file: str) -> str:
        with open(template_file, 'r') as fd:
            for line in fd:
                yield line.strip()

    def __f_title(self) -> str:
        return H1(LIST_TITLE)

    def __f_description(self) -> str:
        return LIST_DESCRIPTION

    def __f_logo(self) -> str:
        return IMG(LIST_TITLE, LIST_LOGO)

    def __f_toc(self) -> str:
        toc = [H2(m.t_toc)+"\n"]
        for protocol in self.protocols:
            toc.append("- " + INTLINK(protocol.name))
        return "\n".join(toc)

    def __f_content(self) -> str:
        """Generate protocol sections in awesome list.

        Format:
        1. Main table with field information (basic fields, not extended).
        2. List of resources
        """
        content = []
        # Main table
        for protocol in self.protocols:
            current = ["\n", H2(protocol.name)]
            current.append(TABLE("Name", protocol.name))
            current.append(BORDER_TABLE)
            # Main table
            for k, v in protocol.to_dict().items():
                if not v or k == p.name:
                    continue
                if k in p.FIELDS and k != p.resources:
                    if p.TYPE(k) == types.LINKLIST:
                        current += self.__f_linklist(k, v)
                    else:
                        v = ", ".join(v) if isinstance(v, list) else v
                        current.append(TABLE(k.capitalize(), v))
            # At the end of the table we want to append the link to detailed page
            filename = "{0}.md".format(LINK_FORMAT(protocol.name))
            fileurl = join(m.protocolpage_relpath, filename)
            current.append(TABLE(m.t_details, LINK(filename, fileurl)))
            content.append("\n".join(current))
            # Resources
            content.append(self.__f_resources(protocol, H3))
        return "\n".join(content)

    def __f_linklist(self, key: str, linklist: list) -> list:
        """Format Link objects in Markdown to insert in Markdown tables."""
        key = p.ALL_FIELDS[key][0] if key in p.ALL_FIELDS.keys() else key.capitalize()
        value = [LINKOBJ(self.links.get_id(l)) for l in linklist]
        return [TABLE(key, ", ".join(value))]

    def __f_packetlist(self, key: str, pktlist: list) -> list:
        content = []
        key = pk.FIELDS[key] if key in pk.FIELDS.keys() else key.capitalize()
        for pkt in pktlist:
            pkt = self.packets.get_id(pkt)
            value = [PACKETOBJ(pkt)]
            if pkt.scapy_pkt:
                value += ["| | Scapy: `{0}`".format(pkt.scapy_pkt)]
            if pkt.raw_pkt:
                value += ["| | Raw: `{0}`".format(pkt.raw_pkt)]
            content.append(TABLE(key, "\n".join(value)))
        return content

    def __f_name(self, protocol: Protocol) -> str:
        """Return name as a head title."""
        return H1(protocol.name)

    def __f_table(self, protocol: Protocol) -> str:
        """Format a table with extended fields for protocol pages."""
        current = []
        current.append(TABLE("Protocol", protocol.name))
        current.append(BORDER_TABLE)
        for k, v in protocol.to_dict().items():
            if not v:
                continue
            if k != p.resources:
                if p.TYPE(k) == types.LINKLIST:
                    current += self.__f_linklist(k, v)
                elif p.TYPE(k) == types.PKTLIST:
                    current += self.__f_packetlist(k, v)
                else:
                    k = p.ALL_FIELDS[k][0] if k in p.ALL_FIELDS.keys() else k.capitalize()
                    v = ", ".join(v) if isinstance(v, list) else v
                    current.append(TABLE(k, v))
        return "\n".join(current)

    def __f_resources(self, protocol: Protocol, level: str = H2) -> list:
        """Format list of resources for awesome list and protocol pages."""
        rdict = {t: [] for t in l.TYPES}
        for link in protocol.resources:
            try:
                link = self.links.get_id(link)
                rdict[link.type].append(link)#"- " + link_fmt)
            except DBException:
                pass
        content = []
        for k, v in rdict.items():
            if v:
                content.append(level(k.capitalize()+"s"))
                v = sorted(v, key=lambda x: x.name.lower())
                for link in v:
                    link_fmt = LINKOBJDESC(link) if link.description else LINKOBJ(link)
                    content.append("- " + link_fmt)
        return "\n".join(content)
