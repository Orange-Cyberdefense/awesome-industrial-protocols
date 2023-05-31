# Turn/IP
# Claire-lex - 2023
# Protocols and Protocol class

"""Classes that represent and handle protocols' info from the database.
"""

from . import MongoDB, DBException, search, exact_search
from config import protocols as p, types, mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_MANDFIELD = "Missing mandatory field '{0}' for {1}."
ERR_UNKPROTO = "Protocol '{0}' not found."
ERR_EXIPROTO = "Protocol '{0}' already exists."
ERR_UNKFIELD = "Protocol '{0}' has no field '{1}'."
ERR_EXIVALUE = "Field '{0}' already contains this value."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."
ERR_BOOLVALUE = "This field only accept 'true' or 'false'"
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
        return self
        
    def get(self, field:str) -> tuple:
        """Get the exact name and value associated to field.

        The research is case-insensitive.

        :raises DBException: if the field does not exist.
        """
        match = search(field, self.fields, threshold=0)
        if len(match) == 1:
            return match[0], getattr(self, match[0])
        if len(match) > 1:
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKFIELD.format(self.name, field)) from None            

    def set(self, field:str, value) -> None:
        """Update existing field in protocol."""
        field, _ = self.get(field)
        # Store
        document = {"name": self.name}
        newvalue = {field: value}
        self.__db.protocols.update_one(document, {"$set": newvalue})
        self.__check()

    def add(self, field:str, value) -> None:
        """Add a new field to protocol."""
        setattr(self, field, value)
        self.set(field, value)

    def append(self, field:str, value) -> None:
        """Append a value to the existing value in a field."""
        _, oldvalue = self.get(field)
        oldvalue = [oldvalue] if not isinstance(oldvalue, list) else oldvalue
        if value not in oldvalue:
            value = [value] if not isinstance(value, list) else value
            self.set(field, [x for x in oldvalue + value if x != ''])
        else:
            raise DBException(ERR_EXIVALUE.format(p.NAME(field)))

    def check(self):
        """Check visitor."""
        self.__check()
        
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
        for attr,_ in p.FIELDS.items():
            try:
                getattr(self, attr)
            except AttributeError:
                setattr(self, attr, "")
        self.__check()

    #--- Private -------------------------------------------------------------#
                
    def __check(self):
        """Check that all mandatory fields are set for protocol objects."""
        try:
            for attr in p.FIELDS:
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
        self.__db = MongoDB()
            
    def get(self, protocol_name:str) -> Protocol:
        """Get a protocol by its name. Returns data as a Protocol object.

        The research is case-insensitive. The name also be one of the aliases.

        :raises DBException: If the protocol does not exist.
        """
        def all_names(protocol:dict):
            alias = protocol[p.alias] if isinstance(protocol[p.alias], list) \
                    else [protocol[p.alias]]
            return [protocol[p.name]] + alias
        
        match = []
        # We do that all the time (I know it sucks) to be up to date with db
        for protocol in self.all:
            if len(exact_search(protocol_name, all_names(protocol))):
                match = [Protocol(**protocol)]
                break # We found the exact match
            elif len(search(protocol_name, all_names(protocol))):
                match.append(Protocol(**protocol))
        if len(match) == 1:
            return match[0]
        if len(match) > 1:
            match = [x.name for x in match]
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKPROTO.format(protocol_name))

    def add(self, protocol:Protocol):
        """Add a new protocol."""
        try:
            proto2 = self.get(protocol.name)
        except DBException:
            pass # The protocol does not exist, we can continue
        else:
            raise DBException(ERR_EXIPROTO.format(proto2.name))
        self.__db.protocols.insert_one(protocol.to_dict())
        
    def delete(self, protocol:Protocol) -> None:
        """Delete an existing protocol."""
        self.get(protocol.name) # Will raise if unknown
        self.__db.protocols.delete_one({p.name: protocol.name})

    def check(self):
        """Check generator."""
        for protocol in self.all_as_objects:
            try:
                protocol.check()
            except DBException as dbe:
                yield str(dbe)
        
    @property
    def all(self) -> list:
        """Return the complete list of protocols as JSON."""
        return [x for x in self.__db.protocols_all]

    @property
    def all_as_objects(self) -> list:
        objects = [Protocol(**x) for x in self.__db.protocols_all]
        return sorted(objects, key=lambda x: x.name)
        
    @property
    def list(self) -> list:
        """Return the list of protocol names."""
        return [x["name"] for x in self.__db.protocols_all]

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self.__db.protocols_count
