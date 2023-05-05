# Turn/IP
# Claire-lex - 2023
# Configuration data

from types import SimpleNamespace

#-----------------------------------------------------------------------------#
# KEYS                                                                        #
#-----------------------------------------------------------------------------#

OPENAI_API_KEY = "" # Insert your OpenAI API key, don't push it.

#-----------------------------------------------------------------------------#
# LIST CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

LIST_DESCRIPTION = "List of industrial network protocols resources."

#-----------------------------------------------------------------------------#
# TOOL CONFIGURATION                                                          #
#-----------------------------------------------------------------------------#

TOOL_DESCRIPTION = "Industrial network protocols browser and more."

#-----------------------------------------------------------------------------#
# DATABASE MANAGEMENT                                                         #
#-----------------------------------------------------------------------------#

mongodb = SimpleNamespace()
mongodb.host = "127.0.0.1"
mongodb.port = 27017
mongodb.timeout = 1000
mongodb.database = "netindusdb"
mongodb.id = "_id"
# Collections
mongodb.protocols = "protocols"
mongodb.links = "links"

protocols = SimpleNamespace()
protocols.name = "name"
protocols.alias = "alias"
protocols.resources = "resources"
protocols.MANDATORY_FIELDS = (
    protocols.name,
    protocols.alias,
    "keywords",
    "port",
    "website",
    "specs",
    "nmap",
    "wireshark",
    "scapy",
    protocols.resources
)

links = SimpleNamespace()
links.TYPES = ("conference, paper, tool, other")
links.DEFAULT_TYPE = "other"

# Sensitivity for search, relying on the Levenshtein distance
# Higher threshold means less sensitivity and less precise matches
LEVENSHTEIN_THRESHOLD = 2

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
ai.has_wireshark = "has a Wireshark dissector"
ai.has_scapy = "has a Scapy layer"
# Security
ai.has_encryption = "has encryption"
ai.has_mandatory_encryption = "has mandatory encryption"
ai.has_authentication = "has authentication"
ai.has_mandatory_authentication = "has mandatory authentication"
ai.has_integrity = "has integrity checks"
ai.has_mandatory_intergrity = "has mandatory integrity checks"
