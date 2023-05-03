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
from pymongo.errors import ConnectionFailure
# Internal
from config import mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

# Errors
ERR_DBCONNECT = "Connection to database failed."

#-----------------------------------------------------------------------------#
# MongoDB classes                                                             #
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
            cls.instance.client = MongoClient(mongodb.host, mongodb.port,
                                              serverSelectionTimeoutMS=mongodb.timeout)
            cls.instance.db = cls.instance.client[mongodb.database]
        return cls.instance

    def __init__(self):
        # We want to check that the connection is OK every time.
        self.__check_connection()
    
    #-------------------------------------------------------------------------#
    # Properties                                                              #
    #-------------------------------------------------------------------------#

    @property
    def protocols(self):
        return self.db[mongodb.protocols]

    @property
    def protocols_count(self):
        return self.db[mongodb.protocols].count_documents({})

    @property
    def protocols_all(self) -> list:
        return [x for x in self.db[mongodb.protocols].find()]
    
    @property
    def links(self):
        return self.db[mongodb.links]

    @property
    def links_count(self):
        return self.db[mongodb.links].count_documents({})

    @property
    def links_all(self) -> list:
        return [x for x in self.db[mongodb.protocols].find()]
    
    #-------------------------------------------------------------------------#
    # Private                                                                 #
    #-------------------------------------------------------------------------#

    def __check_connection(self):
        try:
            self.client.admin.command('ping')
        except ConnectionFailure:
            raise DBException(ERR_DBCONNECT)

        
