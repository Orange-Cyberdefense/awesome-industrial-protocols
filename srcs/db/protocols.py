# Turn/IP
# Claire-lex - 2023
# Protocols and Protocol class
# pylint: disable=invalid-name,no-member,arguments-differ

"""Classes that represent and handle protocols' info from the database.
"""

from config import protocols as p, types, mongodb, LEVENSHTEIN_THRESHOLD
from . import MongoDB, DBException, Collection, Document
from . import search, exact_search

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_MANDFIELD = "Missing mandatory field '{0}' for {1}."
ERR_UNKPROTO = "Protocol '{0}' not found."
ERR_EXIPROTO = "Protocol '{0}' already exists."
ERR_UNKFIELD = "Protocol '{0}' has no field '{1}'."
ERR_EXIVALUE = "Field '{0}' already contains this value."
ERR_INVVALUE = "Field '{0}' does not accept links or packets."
ERR_INVLINK = "Field '{0}' only accepts valid links."
ERR_INVPACKET = "Field '{0}' only accepts valid packets."
ERR_MULTIMATCH = "Multiple match found, please choose between {0}."
ERR_BOOLVALUE = "This field only accept 'true' or 'false'"

#-----------------------------------------------------------------------------#
# Protocol class                                                              #
#-----------------------------------------------------------------------------#

class Protocol(Document):
    """Class representing a single protocol document."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.__fill()

    def __store(self, field: str, value: object) -> None:
        """Save value to the Document in DB and in this class."""
        if isinstance(value, Document):
            raise DBException(ERR_INVVALUE.format(p.NAME(field)))
        document = {"name": self.name}
        newvalue = {field: value}
        self._db.protocols.update_one(document, {"$set": newvalue})
        setattr(self, field, value)
        
    #--- Public --------------------------------------------------------------#

    def get(self, field: str) -> tuple:
        """Get the exact name and value associated to field.

        The research is case-insensitive.

        :raises DBException: if the field does not exist or if the
        requested fields matches multiple ones.
        """
        match = search(field, self.fields, threshold=0)
        if len(match) == 1:
            return match[0], getattr(self, match[0])
        if len(match) > 1:
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKFIELD.format(self.name, field)) from None

    def has_link(self, link):
        """Check if a specific link is associated to the protocol."""
        for field in self.fields:
            if p.TYPE(field) == types.LINKLIST:
                if link._id in [x for x in self.get(field)[1]]:
                    return True
        return False
    
    def set(self, field: str, value: object, replace: bool = False) -> None:
        """Update existing field in protocol."""
        field, oldvalue = self.get(field)
        ftype = p.TYPE(field)
        # We deal with the simplest case first
        if not ftype or ftype == types.STR:
            return self.__store(field, value)
        # Is the value a link or a packet ?
        if isinstance(value, Document):
            value = value._id
            if ftype == types.LINKLIST and value not in self._db.links_id:
                raise DBException(ERR_INVLINK.format(p.NAME(field)))
            elif ftype == types.PKTLIST and value not in self._db.packets_id:
                raise DBException(ERR_INVPACKET.format(p.NAME(field)))
        # All other fields are lists (LIST, LINKLIST, PKTLIST)
        value = value if isinstance(value, list) else [value]
        if replace:
            value = value if isinstance(value, list) else [value]
        elif not replace and oldvalue:
            oldvalue = oldvalue if isinstance(oldvalue, list) else [oldvalue]
            if set(oldvalue) & set(value):
                raise DBException(ERR_EXIVALUE.format(p.NAME(field)))
            value = [x for x in oldvalue + value if x != '']
        self.__store(field, value)

    def add(self, field: str, value: object) -> None:
        """Add a new field to protocol."""
        setattr(self, field, value)
        self.set(field, value)

    def append(self, field: str, value: object) -> None:
        """Append a value to the existing value in a field."""
        _, oldvalue = self.get(field)
        oldvalue = [oldvalue] if not isinstance(oldvalue, list) else oldvalue
        if value not in oldvalue:
            value = [value] if not isinstance(value, list) else value
            self.set(field, [x for x in oldvalue + value if x != ''])
        else:
            raise DBException(ERR_EXIVALUE.format(p.NAME(field)))

    def delete_link(self, link: object) -> None:
        """Delete a link from all fields."""
        for field in self.fields:
            if p.TYPE(field) == types.LINKLIST:
                linklist = self.get(field)[1]
                for l in linklist:
                    if l == link._id: # Finding the link to delete
                        self.set(field, [x for x in linklist if x != link._id], replace=True)
        
    def check(self):
        """Check visitor."""
        # Check that all mandatory fields are set.
        for attr in p.FIELDS:
            try:
                getattr(self, attr)
            except AttributeError:
                raise DBException(ERR_MANDFIELD.format(attr, self.name)) from None
            
    def to_dict(self, exclude_id: bool = True) -> dict:
        """Convert protocol object's content to dictionary."""
        pdict = {}
        for item in self.fields:
            if exclude_id and item == mongodb.id:
                continue
            if item != mongodb.obj:
                pdict[item] = getattr(self, item)
        return pdict

    @property
    def names(self) -> list:
        """Return all names, including aliases."""
        alias = self.alias if isinstance(self.alias, list) \
            else [self.alias]
        return [x for x in [self.name] + alias if x != ""]

    @property
    def fields(self) -> list:
        """Return fields in protocol object (public class attributes)."""
        return [x for x in self.__dict__ if not x.startswith("_Protocol_")]

    def __fill(self):
        """Check that all mandatory fields are set for protocol objects."""
        for attr, _ in p.ALL_FIELDS.items():
            try:
                getattr(self, attr)
            except AttributeError:
                setattr(self, attr, "")
        self.check()

#-----------------------------------------------------------------------------#
# Protocols class                                                             #
#-----------------------------------------------------------------------------#

class Protocols(Collection):
    """Interface with database to handle the protocols' collection."""

    def __init__(self):
        super().__init__()

    def get(self, protocol_name: str, threshold: int=LEVENSHTEIN_THRESHOLD) -> Protocol:
        """Get a protocol by its name. Returns data as a Protocol object.

        The research is case-insensitive. The name also be one of the aliases.

        :raises DBException: If the protocol does not exist.
        """
        match = []
        # We extract from the db everytime even if it's heavy to be up to date
        for protocol in self.all_as_objects:
            if exact_search(protocol_name, protocol.names):
                match = [protocol]
                break # We found the exact match
            if search(protocol_name, protocol.names, threshold):
                match.append(protocol)
        if len(match) == 1:
            return match[0]
        if len(match) > 1:
            match = [x.name for x in match]
            raise DBException(ERR_MULTIMATCH.format(", ".join(match)))
        raise DBException(ERR_UNKPROTO.format(protocol_name))

    def add(self, protocol: Protocol) -> None:
        """Add a new protocol."""
        try:
            # We want a closer match here
            proto = self.get(protocol.name, threshold=1)
        except DBException:
            pass # The protocol does not exist, we can continue
        else:
            raise DBException(ERR_EXIPROTO.format(proto.name))
        self._db.protocols.insert_one(protocol.to_dict())

    def delete(self, protocol: Protocol) -> None:
        """Delete an existing protocol."""
        self.get(protocol.name) # Will raise if unknown
        self._db.protocols.delete_one({p.name: protocol.name})

    @property
    def all(self) -> list:
        """Return the list of protocols as JSON."""
        return self._db.protocols_all

    @property
    def all_as_objects(self) -> list:
        """Return the list of protocols as Protocol objects.

        We choose to rebuild it everytime even though it's slower because
        we need it to be up to date with the database.
        """
        objects = [Protocol(**x) for x in self._db.protocols_all]
        return sorted(objects, key=lambda x: x.name.lower())

    @property
    def list(self) -> list:
        """Return the list of protocol names."""
        return [x["name"] for x in self._db.protocols_all]

    @property
    def count(self) -> int:
        """Return the total number of protocols."""
        return self._db.protocols_count
