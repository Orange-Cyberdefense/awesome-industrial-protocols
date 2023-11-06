# Turn/IP
# Claire-lex - 2023
# MongoDB database manager
# pylint: disable=invalid-name,import-error,unsubscriptable-object

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
ERR_NOSRV = "Could not connect to MongoDB server {0}:{1} (sudo systemctl start mongodb)."
ERR_DBCONNECT = "Connection to database failed."
ERR_UNKFIELD = "Field '{0}' not found."

#-----------------------------------------------------------------------------#
# Abstract classes                                                            #
#-----------------------------------------------------------------------------#

class Document(ABC):
    """Abstract class for document items."""
    _db = None
    _id = None
    fields_dict = None
    name = None

    def __init__(self, **kwargs):
        self._db = MongoDB()
        self._id = kwargs[mongodb.id] if mongodb.id in kwargs else None
    
    def get(self, field: str) -> tuple:
        """Return value associated to field with format (key, value)."""
        field = field.lower()
        if field not in self.fields_dict.keys():
            raise DBException(ERR_UNKFIELD.format(field))
        return self.fields_dict[field]

    @abstractmethod
    def set(self, field: str, value: str) -> None:
        """Set a value to a field."""
        raise NotImplementedError("Document: set")

    @abstractmethod
    def to_dict(self, exclude_id: bool = True) -> dict:
        """Convert document's content to dictionary."""
        raise NotImplementedError("Document: to_dict")

    @abstractmethod
    def check(self) -> None:
        """Check that the content of the Document is valid."""
        raise NotImplementedError("Document: check")

class Collection(ABC):
    """Abstract clas for database collections."""
    _db = None

    def __init__(self):
        self._db = MongoDB()

    @abstractmethod
    def get(self, field: str) -> Document:
        """Get the value associated to the field."""
        raise NotImplementedError("Collection: get")

    @abstractmethod
    def add(self, **kwargs) -> None:
        """Add an entry to the collection."""
        raise NotImplementedError("Collection: add")

    @abstractmethod
    def delete(self, **kwargs) -> None:
        """Delete an entry from the collection."""
        raise NotImplementedError("Collection: delete")

    def has(self, content) -> bool:
        """Return true if this content already exists."""
        try:
            self.get(content)
        except DBException:
            return False
        return True

    def check(self) -> None:
        """Check that the content of the Collection is valid."""
        print("UNLAPIN")
        for obj in self.all_as_objects:
            try:
                obj.check()
            except DBException as dbe:
                yield str(dbe)

    @property
    @abstractmethod
    def all_as_objects(self):
        raise NotImplementedError("Collection: all_as_objects")
        
#-----------------------------------------------------------------------------#
# MongoDB classes                                                             #
#-----------------------------------------------------------------------------#

# Error handling
class DBException(Exception):
    """Exception class for access to database-related errors."""

class MongoDB():
    """MongoDB manager as a singleton class."""
    _instance = None
    client = None
    db = None
    host = None
    port = 0
    timeout = 0
    database = None

    # Singleton stuff
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(MongoDB, cls).__new__(cls)
            # We only want to init the database once.
            cls._instance.__init_db(*args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        # We want to check that the connection is OK every time.
        self.__check_connection()

    @classmethod
    def reset(cls):
        cls._instance = None

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
        return self.db[mongodb.protocols].find()

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
        return self.db[mongodb.links].find()

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
        return self.db[mongodb.packets].find()

    #-------------------------------------------------------------------------#
    # Private                                                                 #
    #-------------------------------------------------------------------------#

    def __init_db(self, host: str = None, port: int = 0, timeout: int = 0,
                database: str = None):
        """Initialize database information, only called once.
        We set values that are not default ones in unittests.
        """
        self.host = host if host else mongodb.host
        self.port = port if port else mongodb.port
        self.timeout = timeout if timeout else mongodb.timeout
        self.database = database if database else mongodb.database
        try:
            self.client = MongoClient(self.host,
                                      self.port,
                                      serverSelectionTimeoutMS=self.timeout)
            databases = self.client.list_database_names()
        except ServerSelectionTimeoutError:
            raise DBException(ERR_NOSRV.format(self.host, self.port)) from None
        if self.database not in databases:
            raise DBException(ERR_NODB.format(self.database))
        self.db = self.client[self.database]

    def __check_connection(self):
        """Check that we are connected to the database server."""
        try:
            self.client.admin.command('ping')
        except ConnectionFailure:
            raise DBException(ERR_DBCONNECT) from None
