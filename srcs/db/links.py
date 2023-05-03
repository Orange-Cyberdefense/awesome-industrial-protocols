# Turn/IP
# Claire-lex - 2023
# Links and Link class

"""Classes that represent and handle links in the database."""

from . import MongoDB, DBException, search
from config import links

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_LINKTYPE = "Invalid link type, choose between: {0}."
ERR_EMPTY = "A link must have at least a url and a description."

#-----------------------------------------------------------------------------#
# Link class                                                              #
#-----------------------------------------------------------------------------#

class Link(object):
    """Class representing a single link."""
    __db = None
    url: None
    type: None
    description: None

    def __init__(self, **kwargs):
        try:
            self.__db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
        self.url = kwargs["name"] if "name" in kwargs else None
        self.type = kwargs["type"] if "type" in kwargs else links.DEFAULT_TYPE
        self.description = kwargs["description"] if "description" in kwargs else None
        self.__check()
        
    #--- Private -------------------------------------------------------------#
        
    def __check(self):
        if not self.url or self.description:
            raise DBException(ERR_EMPTY)
        if self.type not in links.TYPES:
            raise DBException(ERR_LINKTYPE.format(", ".join(links.TYPES)))

    def to_dict(self, exclude_id: bool=True) -> dict:
        """Convert link object's content to dictionary."""
        ldict = {}
        for item in self.fields:
            if exclude_id and item == mongodb.id:
                continue
            ldict[item] = getattr(self, item)
        return ldict
        
#-----------------------------------------------------------------------------#
# Links class                                                                 #
#-----------------------------------------------------------------------------#

class Links(object):
    """Interface with database to handle the links' collection"""
    __db = None

    def __init__(self):
        try:
            self.__db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)

    def get(self, url) -> Link:
        # TODO
        for link in self.all:
            print(link.to_dict())
            
    @property
    def all(self) -> list:
        return [Link(**x) for x in self.__db.links_all]

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self.__db.links_count
