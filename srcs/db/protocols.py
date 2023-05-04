# Turn/IP
# Claire-lex - 2023
# Protocols and Protocol class

"""Classes that represent and handle protocols' info from the database.
"""

from . import MongoDB, DBException, search
from config import protocols, mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_MANDFIELD = "Missing mandatory field '{0}' for {1}."
ERR_UNKPROTO = "Protocol '{0}' not found."
ERR_EXIPROTO = "Protocol '{0}' already exists."
ERR_UNKFIELD = "Protocol {0} has no field '{1}'."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."

#-----------------------------------------------------------------------------#
# Protocol class                                                              #
#-----------------------------------------------------------------------------#

class Protocol(object):
    """Class representing a single protocol document."""
    __db = None
    name = None

    def __init__(self, **kwargs):
        """All entries from dictionary kwargs is converted to an attribute."""
        try:
            self.__db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
        for k, v in kwargs.items():
            setattr(self, k, v)

    #--- Public --------------------------------------------------------------#
            
    def create(self, **kwargs):
        """Create a new protocol object."""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__fill() # Add mandatory field to the object if missing

        
    def get(self, field:str) -> tuple:
        """Get the exact name and value associated to field.

        The research is case-insensitive.

        :raises DBException: if the field does not exist.
        """
        self.__check()
        match = search(field, self.fields, threshold=0)
        if len(match) == 1:
            return match[0], getattr(self, match[0])
        if len(match) > 1:
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKFIELD.format(self.name, field)) from None            

    def set(self, field:str, value) -> None:
        """Update existing field in protocol."""
        self.__check()
        field, _ = self.get(field)
        document = {"name": self.name}
        newvalue = {field: value}
        self.__db.protocols.update_one(document, {"$set": newvalue})

    def add(self, field:str, value) -> None:
        """Add a new field to protocol."""
        setattr(self, field, value)
        self.set(field, value)

    def add_link(self, link_id) -> None:
        """A a link using the ID from the link document in db."""
        # First make sure that resources is a list
        if not isinstance(self.resources, list):
            self.resources = []
        # Check duplicate id and add link :)
        if link_id not in self.resources:
            self.resources.append(link_id)
            self.set(protocols.resources, self.resources)
        
    def to_dict(self, exclude_id: bool=True) -> dict:
        """Convert protocol object's content to dictionary."""
        pdict = {}
        for item in self.fields:
            if exclude_id and item == mongodb.id:
                continue
            pdict[item] = getattr(self, item)
        return pdict
    
    @property
    def names(self) -> list:
        """Return all names, including aliases."""
        alias = self.alias if isinstance(self.alias, list) \
            else [self.alias]
        return [self.name] + alias

    @property
    def fields(self) -> list:
        """Return fields in protocol object (public class attributes)."""
        return [x for x in self.__dict__.keys() if not x.startswith("_Protocol_")]

    def __fill(self):
        """Check that all mandatory fields are set for protocol objects."""
        for attr in protocols.MANDATORY_FIELDS:
            try:
                getattr(self, attr)
            except AttributeError:
                setattr(self, attr, "")

    #--- Private -------------------------------------------------------------#
                
    def __check(self):
        """Check that all mandatory fields are set for protocol objects."""
        try:
            for attr in protocols.MANDATORY_FIELDS:
                getattr(self, attr)
        except AttributeError:
            raise DBException(ERR_MANDFIELD.format(attr, self.name)) from None
            
#-----------------------------------------------------------------------------#
# Protocols class                                                             #
#-----------------------------------------------------------------------------#
        
class Protocols(object):
    """Interface with database to handle the protocols' collection."""
    __db = None
    
    def __init__(self):
        try:
            self.__db = MongoDB()
        except DBException as dbe:
            ERROR(dbe)
            
    def get(self, protocol_name:str) -> Protocol:
        """Get a protocol by its name. Returns data as a Protocol object.

        The research is case-insensitive. The name also be one of the aliases.

        :raises DBException: If the protocol does not exist.
        """
        match = []
        for protocol in self.all:
            if len(search(protocol_name, protocol.names)):
                match.append(protocol)
        if len(match) == 1:
            return match[0]
        if len(match) > 1:
            match = [x.name for x in match]
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKPROTO.format(protocol_name))

    def add(self, protocol:Protocol):
        """Add a new protocol."""
        try:
            self.get(protocol.name)
        except DBException:
            pass # The protocol does not exist, we can continue
        else:
            raise DBException(ERR_EXIPROTO.format(protocol.name))
        self.__db.protocols.insert_one(protocol.to_dict())
        
    @property
    def all(self) -> list:
        """Return the complete list of protocols as Protocol objects."""
        return [Protocol(**x) for x in self.__db.protocols_all]
        
    @property
    def list(self) -> list:
        """Return the list of protocol names."""
        return [x["name"] for x in self.__db.protocols_all]

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self.__db.protocols_count
