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
ERR_UNKFIELD = "Protocol {0} has no field '{1}'."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."

#-----------------------------------------------------------------------------#
# Protocol classes                                                            #
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
        self.__check()

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
        """Update protocol object and document in db."""
        field, _ = self.get(field)
        document = {"name": self.name}
        newvalue = {field: value}
        self.__db.protocols.update_one(document, {"$set": newvalue})
        
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
   
    def __check(self):
        """Check that all mandatory fields are set for protocol objects."""
        try:
            for attr in protocols.MANDATORY_FIELDS:
                getattr(self, attr)
        except AttributeError:
            raise DBException(ERR_MANDFIELD.format(attr, self.name)) from None
            
    
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

    def set(self, protocol:Protocol) -> bool:
        """Update or add a protocol (as a Protocol object) to the database.

        Note: It's safer to update directly fields inside protocols than
        updating a complete protocol at once.
        """
        pass

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
