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
