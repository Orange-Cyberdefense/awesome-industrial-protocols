# Turn/IP
# Claire-lex - 2023
# Configuration data

from types import SimpleNamespace
from os import pardir
from os.path import abspath, dirname, join

#-----------------------------------------------------------------------------#
# KEYS                                                                        #
#-----------------------------------------------------------------------------#

with open("openai_api_key") as fd:
    key = fd.read().strip()
OPENAI_API_KEY = key # Insert your OpenAI API key, don't push it.

#-----------------------------------------------------------------------------#
# LIST CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

LIST_TITLE = "Awesome Industrial Protocols"
LIST_DESCRIPTION = "Security-oriented list of industrial network protocols resources."
LIST_LOGO = "srcs/out/templates/logo-awesome-industrial-protocols.png"

# Markdown pages
markdown = SimpleNamespace()
markdown.awesomelist_name = "README.md"
markdown.awesomelist_path = abspath(join(dirname(abspath(__file__)), pardir))
markdown.protocolpage_path = abspath(join(dirname(abspath(__file__)), pardir, "protocols"))

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

#-----------------------------------------------------------------------------#
# TOOL CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

TOOL_DESCRIPTION = "Industrial network protocols browser and more."

# Sensitivity for search engine, relying on the Levenshtein distance.
# Higher threshold means less sensitivity and less precise matches.
LEVENSHTEIN_THRESHOLD = 2

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

# Database files
mongodb.dbfile_path = abspath(join(dirname(abspath(__file__)), pardir, "db"))
mongodb.dbfile_protocols = "protocols.json"
mongodb.dbfile_links = "links.json"

# Protocols collection types
types = SimpleNamespace()
types.STR = "str"
types.LIST = "list"
types.LINKLIST = "linklist"

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
    protocols.cve: ("Related CVE", types.LINKLIST),
    protocols.resources: ("Resources", types.LINKLIST)
}
protocols.NAME = lambda x: protocols.FIELDS[x][0] if x in protocols.FIELDS else x
protocols.TYPE = lambda x: protocols.FIELDS[x][1] if x in protocols.FIELDS else None

# Links collection content
links = SimpleNamespace()
links.id = "_id"
links.url = "url"
links.description = "description"
links.type = "type"
links.TYPES = ("documentation", "conference", "paper", "tool", "article", "other")
links.DEFAULT_TYPE = "other"

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
# Security
ai.has_encryption = "has encryption"
ai.has_mandatory_encryption = "has mandatory encryption"
ai.has_authentication = "has authentication"
ai.has_mandatory_authentication = "has mandatory authentication"
ai.has_integrity = "has integrity checks"
ai.has_mandatory_integrity = "has mandatory integrity checks"

#--- Data extracted from Wireshark dissectors --------------------------------#

wireshark = SimpleNamespace()
# URL to Wireshark data using Github's REST API
wireshark.api_trees = "https://api.github.com/repos/wireshark/wireshark/git/trees/"
wireshark.api_epan_folder = "https://api.github.com/repositories/21329550/contents/epan"
# Search data in Wireshark repository's tree
wireshark.dissector_folder = "dissectors"
wireshark.regex_dissector_name = "^packet-([^\.]+)\.c$" # packet-*.c
wireshark.naming_function = "proto_register_protocol"
wireshark.regex_function_param = "[^\(]\((.*?)\);" # (*)
