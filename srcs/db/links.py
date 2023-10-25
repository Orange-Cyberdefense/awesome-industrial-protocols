# Turn/IP
# Claire-lex - 2023
# Links and Link class
# pylint: disable=invalid-name,redefined-builtin,arguments-differ

"""Classes that represent and handle links in the database."""

from urllib.parse import urlparse, ParseResult
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from http.client import InvalidURL
from socket import timeout as socket_timeout
from re import match as re_match
# Internal
from config import mongodb, links as l
from . import MongoDB, DBException, Collection, Document, search

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

TIMEOUT = 2

ERR_LINKTYPE = "Invalid link type, choose between: {0}."
ERR_EMPTY = "A link must have at least a name and a url."
ERR_BADURL = "URL '{0}' cannot be accessed."
ERR_HTTP = "URL '{0}' returned error: {1}."
ERR_UNKURL = "Link '{0}' not found."
ERR_EXIURL = "URL '{0}' already exists."
ERR_UNKID = "This ID does not match with any existing link ({0})."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."
ERR_UNKFIELD = "Field '{0}' not found."

#-----------------------------------------------------------------------------#
# Link class                                                              #
#-----------------------------------------------------------------------------#

class Link(Document):
    """Class representing a single link."""
    __url: None # ParseResult from urllib
    type: None
    description: None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs[l.name] if l.name in kwargs else None
        self.__url = self.__set_url(kwargs[l.url]) if l.url in kwargs else None
        self.type = kwargs[l.type] if l.type in kwargs else l.DEFAULT_TYPE
        self.description = kwargs[l.description] if l.description in kwargs else None
        self.fields_dict = {
            l.name: self.name,
            l.url: self.url,
            l.description: self.description,
            l.type: self.type
        }
        self.__check()

    def __str__(self):
        return "[{0}] {1}: {2}: {3}".format(self.type.capitalize(), self.name,
                                            self.description, self.url)

    def set(self, field: str, value: str) -> None:
        """Set value to field."""
        field = field.lower()
        if field not in self.fields_dict.keys():
            raise DBException(ERR_UNKFIELD.format(field))
        if field == l.type:
            value = value.lower()
            if value not in l.TYPES:
                raise DBException(ERR_LINKTYPE.format(", ".join(l.TYPES)))
        self.fields_dict[field] = value
        document = {l.url: self.url}
        newvalue = {field: value}
        self._db.links.update_one(document, {"$set": newvalue})

    @staticmethod
    def to_url(url: str) -> str:
        """Format URL string to match Link.url, to detect duplicates."""
        return Link.__set_url(url).geturl()

    @staticmethod
    def check_url(url: str) -> None:
        """Try to open the URL to see if it exists. Raises DBException if not."""
        try:
            request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            urlopen(request, timeout=TIMEOUT)
        except HTTPError as he:
            raise DBException(ERR_HTTP.format(url, str(he))) from None
        except (URLError, InvalidURL, socket_timeout):
            raise DBException(ERR_BADURL.format(url)) from None

    def check(self):
        """Check visitor."""
        self.__check()
        self.check_url(self.url)

    def to_dict(self, exclude_id: bool = True) -> dict:
        """Convert link object's content to dictionary."""
        ldict = {
            l.name: self.name,
            l.url: self.url,
            l.description: self.description,
            l.type: self.type
        }
        if not exclude_id:
            ldict[l.id] = self._id
        return ldict

    @property
    def url(self) -> str:
        """URL is internally handled as ParseResult (urllib), returned as str."""
        return self.__url.geturl()

    #--- Private -------------------------------------------------------------#

    @staticmethod
    def __set_url(url: str) -> ParseResult:
        """Convert url passed as argument to a parsed url (uses urllib)."""
        url = url if re_match(r'http.*://.*', url) else "https://" + url
        url = urlparse(url)
        if not url.scheme:
            url._replace(scheme="https")
        return url

    def __check(self):
        if not self.name or not self.__url:
            raise DBException(ERR_EMPTY)

#-----------------------------------------------------------------------------#
# Links class                                                                 #
#-----------------------------------------------------------------------------#

class Links(Collection):
    """Interface with database to handle the links' collection"""

    def __init__(self):
        super().__init__()

    def get(self, url: str, multimatch: bool = False) -> Link:
        """Get a link object by its URL."""
        match = []
        for link in self.all_as_objects:
            if search(Link.to_url(url), link.url, threshold=0):
                match.append(link)
            # We also search by name
            elif search(url, link.name, threshold=0):
                match.append(link)
        if len(match) == 1:
            return match[0]
        if len(match) > 1:
            if multimatch:
                return match
            match = [x.name for x in match]
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKURL.format(url))

    def get_id(self, iddb: object) -> Link:
        """Get a link object by its ID in database."""
        for link in self.all:
            if link[l.id] == iddb:
                return Link(**link)
        raise DBException(ERR_UNKID.format(iddb))

    def add(self, name: str, url: str, description: str,
            type: str = l.DEFAULT_TYPE) -> Link:
        """Add a link to link collection."""
        try:
            self.get(url)
        except DBException:
            pass # The link does not exist, we can continue
        else:
            raise DBException(ERR_EXIURL.format(url))
        link = Link(name=name, url=url, description=description, type=type)
        # Check if link is valid and exists before inserting it to DB
        Link.check_url(link.url) # Will raise exception if invalid
        self._db.links.insert_one(link.to_dict())
        # We don't return link directly because we need the updated _id after db
        # insert, so we read it again from the db
        return self.get(link.url)

    def delete(self, link: Link) -> None:
        """Delete an existing link."""
        self.get(link.url) # Will raise if unknown
        self._db.links.delete_one({l.url: link.url})

    def check(self):
        """Check generator."""
        for link in self.all_as_objects:
            try:
                link.check()
            except DBException as dbe:
                yield str(dbe)

    @property
    def all(self) -> list:
        """Return the list of links as JSON."""
        return self._db.links_all

    @property
    def all_as_objects(self) -> list:
        """Return the list of links as Link objects."""
        objects = [Link(**x) for x in self._db.links_all]
        return sorted(objects, key=lambda x: x.name.lower())

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self._db.links_count
