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
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."

#-----------------------------------------------------------------------------#
# Protocol classes                                                            #
#-----------------------------------------------------------------------------#

class Protocol(object):
    """Class representing a single protocol document."""
    name = None

    def __init__(self, **kwargs):
        """All entries from dictionary kwargs is converted to an attribute."""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__check()

    def __check(self):
        """Check that all mandatory fields are set for protocol objects."""
        try:
            for attr in protocols.MANDATORY_FIELDS:
                getattr(self, attr)
        except AttributeError:
            raise DBException(ERR_MANDFIELD.format(attr, self.name)) from None

    def to_dict(self, exclude_id=True):
        """Convert protocol object's content to dictionary."""
        pdict = {}
        for item in self.__dict__:
            if exclude_id and item == mongodb.id:
                continue
            pdict[item] = getattr(self, item)
        return pdict

    @property
    def names(self):
        """Return all names, including aliases."""
        alias = self.alias if isinstance(self.alias, list) \
            else [self.alias]
        return [self.name] + alias
        
    
class Protocols(object):
    """Interface with database to handle the protocols' collection."""
    db = None
    
    def __init__(self):
        try:
            self.db = MongoDB()
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
        raise DBException(ERR_UNKPROTO.format(name))

    def set(self, protocol:Protocol) -> bool:
        """Update or add a protocol (as a Protocol object) to the database.

        Note: It's safer to update directly fields inside protocols than
        updating a complete protocol at once.
        """
        pass

    @property
    def all(self) -> list:
        """Return the complete list of protocols as Protocol objects."""
        return [Protocol(**x) for x in self.db.protocols_all]
        
    @property
    def list(self) -> list:
        """Return the list of protocol names."""
        pass

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self.db.protocols_count
