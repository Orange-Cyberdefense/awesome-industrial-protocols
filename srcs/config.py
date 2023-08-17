# Turn/IP
# Claire-lex - 2023
# Configuration data
# pylint: disable=invalid-name

"""Configuration file for Turn/IP.

Most of the constants are here and can be modified by the user.
"""

from types import SimpleNamespace
from os import pardir, environ
from os.path import abspath, dirname, join

#-----------------------------------------------------------------------------#
# KEYS                                                                        #
#-----------------------------------------------------------------------------#

# Used to query OpenAI models to gather information about protocols
with open("openai_api_key") as fd:
    key = fd.read().strip()
OPENAI_API_KEY = key # Insert your OpenAI API key, don't push it.

# Used for searching videos on Youtube
with open("google_api_key") as fd:
    key = fd.read().strip()
GOOGLE_API_KEY = key # Insert your Google API key, don't push it.

#-----------------------------------------------------------------------------#
# LIST CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

LIST_TITLE = "Awesome Industrial Protocols"
LIST_DESCRIPTION = "Compilation of industrial network protocols resources focusing on offensive security."
LIST_LOGO = "srcs/out/templates/logo-awesome-industrial-protocols.png"

# Markdown pages
markdown = SimpleNamespace()
markdown.awesomelist_name = "README.md"
markdown.awesomelist_path = abspath(join(dirname(abspath(__file__)), pardir))
markdown.protocolpage_path = abspath(join(dirname(abspath(__file__)), pardir, "protocols"))
markdown.protocolpage_relpath = join("protocols")

# Templates for Markdown pages
markdown.awesomelist_template = "template-awesome-industrial-protocols.md"
markdown.protocolpage_template = "template-protocol-page.md"
markdown.templates_path = join(dirname(abspath(__file__)), "out", "templates")

# Format for Markdown templates and files
markdown.f_title = "%title%"
markdown.f_description = "%description%"
markdown.f_logo = "%logo%"
markdown.f_toc = "%toc%"
markdown.f_content = "%content%"
markdown.f_name = "%name%"
markdown.f_table = "%table%"
markdown.f_resources = "%resources%"

markdown.t_toc = "Contents"
markdown.t_details = "Detailed page"

#-----------------------------------------------------------------------------#
# TOOL CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

TOOL_TITLE = "Turn/IP (awesome-industrial-protocols)"
TOOL_DESCRIPTION = "Industrial network protocols browser and more."

# Sensitivity for search engine, relying on the Levenshtein distance.
# Higher threshold means less sensitivity and less precise matches.
LEVENSHTEIN_THRESHOLD = 2

#-----------------------------------------------------------------------------#
# USER INTERFACE CONFIGURATION                                                #
#-----------------------------------------------------------------------------#

# Avoid delay when pressing ESC to exit
environ.setdefault('ESCDELAY', '25')

tui = SimpleNamespace()
tui.min_height = 20 # Arbitrary
tui.min_width = 100 # Arbitrary
tui.title_search = "Search"
tui.title_filter = "Filter"
tui.title_list_prot = "Protocols"
tui.title_info_prot = "Details"
tui.title_menu = "Menu"
tui.menu_view = "View"
tui.menu_edit = "Edit"
tui.menu_quit = "Quit"
tui.footer_fmt = "{0}/{1} protocols"

#-----------------------------------------------------------------------------#
# DATABASE MANAGEMENT                                                         #
#-----------------------------------------------------------------------------#

# Connection
mongodb = SimpleNamespace()
mongodb.host = "127.0.0.1"
mongodb.port = 27017
mongodb.timeout = 1000
mongodb.database = "awesome-industrial-protocols"
mongodb.id = "_id"

# Collections
mongodb.protocols = "protocols"
mongodb.links = "links"
mongodb.packets = "packets"

# Database files
mongodb.dbfile_path = abspath(join(dirname(abspath(__file__)), pardir, "db"))
mongodb.dbfile_protocols = "protocols.json"
mongodb.dbfile_links = "links.json"
mongodb.dbfile_packets = "packets.json"

# Protocols collection types
types = SimpleNamespace()
types.STR = "str"
types.LIST = "list"
types.LINKLIST = "linklist"
types.PKTLIST = "pktlist"

# Protocols collection content
protocols = SimpleNamespace()
protocols.name = "name"
protocols.alias = "alias"
protocols.description = "description"
protocols.keywords = "keywords"
protocols.resources = "resources"
protocols.port = "port"
protocols.access = "access"
protocols.specs = "specs"
protocols.security = "security"
protocols.nmap = "nmap"
protocols.wireshark = "wireshark"
protocols.scapy = "scapy"
protocols.pcap = "pcap"
protocols.cve = "cve"
protocols.multicast = "multicast"
protocols.discovery = "discovery"
protocols.FIELDS = {
    protocols.name: ("Name", types.STR),
    protocols.alias: ("Aliases", types.LIST),
    protocols.description: ("Description", types.STR),
    protocols.keywords: ("Keywords", types.LIST),
    protocols.port: ("Port(s)", types.STR),
    protocols.access: ("Access to specs", types.STR),
    protocols.specs: ("Specifications", types.LINKLIST),
    protocols.security: ("Security features", types.STR),
    protocols.nmap: ("Nmap script(s)", types.LINKLIST),
    protocols.wireshark: ("Wireshark dissector", types.LINKLIST),
    protocols.scapy: ("Scapy layer", types.LINKLIST),
    protocols.pcap: ("Example Pcap(s)", types.LINKLIST),
    protocols.resources: ("Resources", types.LINKLIST)
}
protocols.EXTENDED_FIELDS = {
    protocols.cve: ("Related CVE", types.LINKLIST),
    protocols.multicast: ("Multicast address", types.STR),
    protocols.discovery: ("Discovery packet", types.PKTLIST)
}
protocols.ALL_FIELDS = {**protocols.FIELDS, **protocols.EXTENDED_FIELDS}
protocols.NAME = lambda x: protocols.ALL_FIELDS[x][0] if x in protocols.ALL_FIELDS else x
protocols.TYPE = lambda x: protocols.ALL_FIELDS[x][1] if x in protocols.ALL_FIELDS else None

# Links collection content
links = SimpleNamespace()
links.id = "_id"
links.name = "name"
links.url = "url"
links.description = "description"
links.type = "type"
links.TYPES = ("documentation", "article", "conference", "paper", "tool", "other", "cve")
links.DEFAULT_TYPE = "other"

# Packets collection content
packets = SimpleNamespace()
packets.id = "_id"
packets.name = "name"
packets.protocol = "protocol"
packets.description = "description"
packets.scapy_pkt = "scapy_pkt"
packets.raw_pkt = "raw_pkt"
packets.FIELDS = {
    packets.name: "Name",
    packets.protocol: "Protocol",
    packets.description: "Description",
    packets.scapy_pkt: "Scapy format",
    packets.raw_pkt: "Raw format"
}

#-----------------------------------------------------------------------------#
# AUTOMATED SEARCH                                                            #
#-----------------------------------------------------------------------------#

#--- OpenAI-generated data ---------------------------------------------------#

AI_WARNING = "WARNING: AI-generated data is not reliable.\n" \
"All AI-generated data is marked with *, please double-check it."

ai = SimpleNamespace()
ai.key = OPENAI_API_KEY
ai.model = "text-davinci-003"
ai.temperature = 0.5
ai.max_tokens = 100

ai.yes_no_question = "{0} {1}? yes or no"
ai.is_protocol = "is a network protocol"
ai.description = "description in 10 words"
ai.default_port = "default port"
# Documentation
ai.is_spec_free = "specification is available for free"

#--- Data extracted from Wireshark dissectors --------------------------------#

wireshark = SimpleNamespace()
# URL to Wireshark data using Github's REST API
wireshark.api_epan_folder = "https://api.github.com/repositories/21329550/contents/epan"
wireshark.dissectors_url = "https://github.com/wireshark/wireshark/blob/master/epan/dissectors/"
# Search data in Wireshark repository's tree
wireshark.dissectors_folder = "dissectors"
wireshark.regex_dissector_name = r"^packet-([^\.]+)\.c$" # packet-*.c
wireshark.naming_function = "proto_register_protocol"
wireshark.regex_function_param = r"[^\(]\((.*?)\);" # (*)
wireshark.dissector_desc = "Wireshark dissector for {0}"

scapy = SimpleNamespace()
# URL to Wireshark data using Github's REST API
scapy.api_layers_folder = "https://api.github.com/repos/secdev/scapy/contents/scapy/layers"
scapy.api_contrib_folder = "https://api.github.com/repos/secdev/scapy/contents/scapy/contrib"
scapy.layer_desc = "Scapy layer for {0}"

cvelist = SimpleNamespace()
# URL to NIST's NVD CVE database's API
cvelist.api_keywords_search = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={0}"
cvelist.nvd_detail = "https://nvd.nist.gov/vuln/detail/"

youtube = SimpleNamespace()
# URL to Youtube site and API
youtube.api_service_name = "youtube"
youtube.api_version = "v3"
youtube.watch_url = "https://www.youtube.com/watch?v="
# Selected channels
youtube.selected_channels = {
    "UC6Om9kAkl32dWlDSNlDS9Iw": "DEF CON",
    "UCJ6q9Ie29ajGqKApbLqfBOg": "Black Hat",
    "UCcA_TRQ5sLtFC3pAkaVot3Q": "SANS ICS Security"
}
