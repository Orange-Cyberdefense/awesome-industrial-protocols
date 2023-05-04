# Turn/IP
# Claire-lex - 2023
# Links and Link class

"""Classes that represent and handle links in the database."""

from urllib.parse import urlparse, ParseResult
from urllib.request import urlopen
from urllib.error import URLError
from socket import timeout as socket_timeout
from re import match as re_match
# Internal
from . import MongoDB, DBException, search
from config import mongodb, links

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_LINKTYPE = "Invalid link type, choose between: {0}."
ERR_EMPTY = "A link must have at least a url and a description."
ERR_BADURL = "URL '{0}' cannot be accessed"
ERR_UNKURL = "URL '{0}' not found."
ERR_EXIURL = "URL '{0}' already exists."
ERR_UNKID = "This link ID does not match with any existing link ({0})."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."

#-----------------------------------------------------------------------------#
# Link class                                                              #
#-----------------------------------------------------------------------------#

class Link(object):
    """Class representing a single link."""
    __db = None
    id = None
    __url: None # ParseResult from urllib
    type: None
    description: None

    def __init__(self, **kwargs):
        try:
            self.__db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
        self.id = kwargs[mongodb.id] if mongodb.id in kwargs else None
        self.__url = self.__set_url(kwargs["url"]) if "url" in kwargs else None
        self.type = kwargs["type"] if "type" in kwargs else links.DEFAULT_TYPE
        self.description = kwargs["description"] if "description" in kwargs else None
        self.__check()

    def __str__(self):
        return "[{0}] {1}: {2}".format(self.type.capitalize(), self.description,
                                       self.url)
        
    @staticmethod
    def to_url(url: str) -> str:
        """Format URL string to match Link.url, to detect duplicates."""
        return Link.__set_url(url).geturl()

    @staticmethod
    def check_url(url: str) -> None:
        """Try to open the URL to see if it exists. Raises DBException if not."""
        try:
            urlopen(url, timeout=1)
        except (URLError, socket_timeout):
            raise DBException(ERR_BADURL.format(url)) from None
                
    #--- Private -------------------------------------------------------------#

    @staticmethod
    def __set_url(url) -> ParseResult:
        """Convert url passed as argument to a parsed url (uses urllib)."""
        url = url if re_match(r'http.*://.*', url) else "https://" + url
        url = urlparse(url)
        if not url.scheme :
            url._replace(scheme="https")
        return url
        
    def __check(self):
        if not self.__url or not self.description:
            raise DBException(ERR_EMPTY)
        if self.type not in links.TYPES:
            raise DBException(ERR_LINKTYPE.format(", ".join(links.TYPES)))

    def to_dict(self, exclude_id: bool=True) -> dict:
        """Convert link object's content to dictionary."""
        ldict = {
            "url": self.url,
            "type": self.type,
            "description": self.description
        }
        if not exclude_id:
            ldict["_id"] = self._id
        return ldict

    @property
    def url(self) -> str:
        """URL is internally handled as ParseResult (urllib), returned as str."""
        return self.__url.geturl()
    
    @property
    def fields(self) -> list:
        """Return fields in protocol object (public class attributes)."""
        return (self.url, self.description, self.type)
    
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
        """Get a link object by its URL."""
        match = []
        for link in self.all:
            if len(search(Link.to_url(url), link.url, threshold=0)):
                match.append(link)
        if len(match) == 1:
            return match[0]
        if len(match) > 1:
            match = [x.name for x in match]
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKURL.format(url))

    def get_id(self, id) -> Link:
        """Get a link object by its ID in database."""
        # TMP: replace with filter
        for link in self.all:
            if link.id == id:
                return link
        raise DBException(ERR_UNKID.format(id))
    
    def add(self, url, description, type=links.DEFAULT_TYPE) -> None:
        """Add a link to link collection."""
        try:
            self.get(url)
        except DBException:
            pass # The protocol does not exist, we can continue
        else:
            raise DBException(ERR_EXIURL.format(url))
        link = Link(url=url, description=description, type=type)
        # Check if link is valid and exists before inserting it to DB
        Link.check_url(link.url) # Will raise exception if invalid
        self.__db.links.insert_one(link.to_dict())
        # We don't return link directly because we need the updated _id after db
        # insert, so we read it again from the db
        return self.get(link.url)
    
    @property
    def all(self) -> list:
        return [Link(**x) for x in self.__db.links_all]

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self.__db.links_count
