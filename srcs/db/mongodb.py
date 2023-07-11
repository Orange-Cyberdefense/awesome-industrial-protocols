# Turn/IP
# Claire-lex - 2023
# MongoDB database manager
# pylint: disable=invalid-name,import-error

"""Interface with MongoDB database

The database has two collections:
- protocols
- links

Each collection contains one document per protocol/link.
Each document contains varying fields with values.
"""

from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
# Internal
from config import mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

# Errors
ERR_NODB = "Database {0} not found, please import it with 'python turn-ip.py "\
           "--mongoimport'"
ERR_NOSRV = "Could not connect to MongoDB server {0}:{1}."
ERR_DBCONNECT = "Connection to database failed."
ERR_UNKFIELD = "Field '{0}' not found."

#-----------------------------------------------------------------------------#
# Abstract classes                                                            #
#-----------------------------------------------------------------------------#

class Document(ABC):
    """Abstract class for document items."""
    __db = None

    def get(self, field: str) -> str:
        """Return value associated to field."""
        field = field.lower()
        if field not in self.fields_dict.keys():
            raise DBException(ERR_UNKFIELD.format(field))
        return self.fields_dict[field]

    @abstractmethod
    def set(self, field: str, value: str) -> None:
        raise NotImplementedError("Document: set")

    @abstractmethod
    def to_dict(self, exclude_id: bool = True) -> dict:
        """Convert document's content to dictionary."""
        raise NotImplementedError("Document: to_dict")
    
    @abstractmethod
    def check(self) -> None:
        raise NotImplementedError("Document: check")

class Collection(ABC):
    """Abstract clas for database collections."""
    __db = None

    @abstractmethod
    def get(self, field: str) -> Document:
        raise NotImplementedError("Collection: get")

    @abstractmethod
    def add(self, **kwargs) -> None:
        raise NotImplementedError("Collection: add")
    
#-----------------------------------------------------------------------------#
# MongoDB classes                                                             #
#-----------------------------------------------------------------------------#

# Error handling
class DBException(Exception):
    """Exception class for access to database-related errors."""
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
            try:
                cls.instance.client = MongoClient(mongodb.host, mongodb.port,
                                                  serverSelectionTimeoutMS=mongodb.timeout)
                databases = cls.instance.client.list_database_names()
            except ServerSelectionTimeoutError:
                raise DBException(ERR_NOSRV.format(mongodb.host, mongodb.port)) from None
            if mongodb.database not in databases:
                raise DBException(ERR_NODB.format(mongodb.database))
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
        """Return protocols collection."""
        return self.db[mongodb.protocols]

    @property
    def protocols_count(self):
        """Return number of protocols in collection."""
        return self.db[mongodb.protocols].count_documents({})

    @property
    def protocols_all(self) -> list:
        """Return all protocols in collection."""
        return [x for x in self.db[mongodb.protocols].find()]

    @property
    def links(self):
        """Return links collection."""
        return self.db[mongodb.links]

    @property
    def links_count(self):
        """Return number of links in collection."""
        return self.db[mongodb.links].count_documents({})

    @property
    def links_all(self) -> list:
        """Return all links in collection."""
        return [x for x in self.db[mongodb.links].find()]

    @property
    def packets(self):
        """Return packets collection."""
        return self.db[mongodb.packets]

    @property
    def packets_count(self):
        """Return number of packets in collection."""
        return self.db[mongodb.packets].count_documents({})

    @property
    def packets_all(self):
        """Return all packets in collection."""
        return [x for x in self.db[mongodb.packets].find()]
    
    #-------------------------------------------------------------------------#
    # Private                                                                 #
    #-------------------------------------------------------------------------#

    def __check_connection(self):
        """Check that we are connected to the database server."""
        try:
            self.client.admin.command('ping')
        except ConnectionFailure:
            raise DBException(ERR_DBCONNECT) from None
