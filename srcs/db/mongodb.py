# Turn/IP
# Claire-lex - 2023
# MongoDB database manager

"""Interface with MongoDB database

The database has two collections:
- protocols
- links

Each collection contains one document per protocol/link.
Each document contains varying fields with values.
"""

from pymongo import MongoClient
from re import sub
# Internal
from config import MONGODB_HOST, MONGODB_PORT, MONGODB_DATABASE

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

def FORMAT(value: str) -> str:
    """Standardize input to make case and character independent match."""
    if isinstance(value, str):
        return sub('[^0-9a-zA-Z]+', '', value.lower().strip())
    return value

#-----------------------------------------------------------------------------#
# MongoDB class                                                               #
#-----------------------------------------------------------------------------#

# Error handling
class DBException(Exception):
    pass

class MongoDB(object):
    """MongoDB manager as a singleton class."""
    client = None
    db = None

    # Singleton stuff
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoDB, cls).__new__(cls)
            # Setting only one MongoDB Client
            cls.instance.client = MongoClient(MONGODB_HOST, MONGODB_PORT)
            cls.instance.db = cls.instance.client[MONGODB_DATABASE]
        return cls.instance

    #-------------------------------------------------------------------------#
    # Public                                                                 #
    #-------------------------------------------------------------------------#
    
    def get_protocol(self, name: str=None) -> dict:
        """Return the document associated to the protocol "name" as a dict.

        The research is case-insensitive. The name also be one of the aliases.

        :raises DBException: If the protocol does not exist.
        """
        # No argument == return all protocols :)
        if not name:
            return [x for x in self.protocols.find()]
        # We cannot just use find_one() / find(): we want case insensitive search
        for proto in self.protocols.find():
            names = [FORMAT(x) for x in self.__get_all_names(proto)]
            if name in names:
                return proto
        raise DBException("Protocol '{0}' not found.".format(name))

    @property
    def protocols(self):
        return self.db["protocols"]
    
    #-------------------------------------------------------------------------#
    # Private                                                                 #
    #-------------------------------------------------------------------------#
    
    def __get_all_names(self, protocol: dict) -> list:
        names = [protocol["name"]]
        names += protocol["alias"] if isinstance(protocol["alias"], list) else \
                 [protocol["alias"]]
        return list(filter(None, names)) # Removing empty items

        
