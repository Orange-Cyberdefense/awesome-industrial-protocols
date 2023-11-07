# Turn/IP
# Claire-lex - 2023
# unittest : Database management (MongoDB)

import unittest
from os import system

from db import MongoDB, DBException, ERR_MULTIMATCH
from db import Protocols, Protocol, Links, Link, Packets, Packet
from config import mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

DB_HOST = mongodb.host
DB_PORT = mongodb.port
DB_TIMEOUT = mongodb.timeout
DB_DATABASE = mongodb.test_database

DB_CREATE = "/usr/bin/mongo --eval 'db=db.getSiblingDB(\"test-aip\");" \
    "db.createCollection(\"protocols\");db.createCollection(\"links\");" \
    "db.createCollection(\"packets\");' > /dev/null 2>&1"

TEST_COLL_PROTOCOLS = (
    {"name": "Petere", "alias": "Dustiff Hoffman", "port": 1},
    {"name": "Stevene", "alias": "Robert Redford", "port": 2},
    {"name": "Hugues", "alias": "James Stewart", "port": 3},
    {"name": "Dave", "alias": "Paul Newman", "port": 4}
)
PROTOCOLS = [x["name"] for x in TEST_COLL_PROTOCOLS]

TEST_COLL_LINKS = (
    {"name": "A successful Git branching model", "url": "https://nvie.com/posts/a-successful-git-branching-model/", "description": "Trying to follow this"},
    {"name": "Oh shit git", "url": "https://ohshitgit.com/", "description": "Very useful"},
    {"name": "George Abitbol", "url": "http://george-abitbol.fr/", "description": "Inspiration"},
    {"name": "Magic button", "url": "http://make-everything-ok.com/", "description": "Make everything OK"},
)
LINKS = [x["name"] for x in TEST_COLL_LINKS]

TEST_COLL_PACKETS = (
    {"protocol": PROTOCOLS[0], "name": "Seagull",
     "description": "Noisy", "scapy_pkt": "Seagull()",
     "raw_pkt": "0xAMOI"},
    {"protocol": PROTOCOLS[0], "name": "Owl",
     "description": "Surprised", "scapy_pkt": "Owl()",
     "raw_pkt": "0xHOU"},
    {"protocol": PROTOCOLS[0], "name": "Raven",
     "description": "Dark", "scapy_pkt": "Raven()",
     "raw_pkt": "0xCROA"},
)
PACKETS = [x["name"] for x in TEST_COLL_PACKETS]

#-----------------------------------------------------------------------------#
# Simple check on prod database before moving to tests on test database       #
#-----------------------------------------------------------------------------#

class Test01DBProd(unittest.TestCase):
    """Test class to check that the production database loads.
    All the other tests are on test database.
    """
    def test_0101_loaddefaultdb_init(self):
        """MongDB client and database load."""
        instance = MongoDB()
        self.assertIsNotNone(instance)
        self.assertIsNotNone(instance.client)
        self.assertIsNotNone(instance.db)
    def test_0102_loaddefaultdb_content(self):
        """Database information is correct."""
        instance = MongoDB()
        self.assertEqual(instance.host, mongodb.host)
        self.assertEqual(instance.port, mongodb.port)
        self.assertEqual(instance.timeout, mongodb.timeout)
        self.assertEqual(instance.database, mongodb.database)
    @classmethod
    def tearDownClass(self):
        """Reset mongodb instance to use test db instead."""
        MongoDB.reset()

#-----------------------------------------------------------------------------#
# Base class and functions for tests on test-aip database                     #
#-----------------------------------------------------------------------------#

def set_test_database() -> object:
    """Create database and collection if they don't exist, then use them."""
    system(DB_CREATE)
    return MongoDB(DB_HOST, DB_PORT, DB_TIMEOUT, DB_DATABASE)

def empty_test_database(db: object):
    # Empty the test database
    for coll in TEST_COLL_PROTOCOLS:
        db.protocols.delete_one({"name": coll["name"]})
    for coll in TEST_COLL_LINKS:
        if "url" in coll.keys():
            db.links.delete_one({"url": coll["url"]})
    for coll in TEST_COLL_PACKETS:
        if "name" in coll.keys():
            db.packets.delete_one({"protocol": coll["protocol"],
                                   "name": coll["name"]})
def populate(item):
    if isinstance(item, Protocols):
        collection = TEST_COLL_PROTOCOLS
        obj = Protocol
    if isinstance(item, Links):
        collection = TEST_COLL_LINKS
        obj = Link
    if isinstance(item, Packets):
        collection = TEST_COLL_PACKETS
        obj = Packet
    for p in collection:
        try:
            item.add(obj(**p))
        except DBException:
            pass # We don't care if it already exists

class DBTest(unittest.TestCase):
    """Every test class that uses the test database must inherit this one."""
    @classmethod
    def setUpClass(self):
        """Create database and collections if they don't exist."""
        # Not very pretty sorry :(
        self.db = set_test_database()
        empty_test_database(self.db)
        # Init database objects
        self.protocols = Protocols()
        self.links = Links()
        self.packets = Packets()
    @classmethod
    def tearDownClass(self):
        # We don't remove the test database content to be able to check it.
        MongoDB.reset()

#-----------------------------------------------------------------------------#
# Testing database features                                                   #
#-----------------------------------------------------------------------------#
        
class Test02DBTest(DBTest):
    """Test class to check interaction with the database (test)."""
    def test_0201_loadtestdb_init(self):
        """MongDB client and database load."""        
        self.assertIsNotNone(self.db)
        self.assertIsNotNone(self.db.client)
        self.assertIsNotNone(self.db.db)
    def test_0202_loadtestdb_content(self): 
        """Database information is correct."""
        self.assertEqual(self.db.host, mongodb.host)
        self.assertEqual(self.db.port, mongodb.port)
        self.assertEqual(self.db.timeout, mongodb.timeout)
        self.assertEqual(self.db.database, mongodb.test_database)

class Test03DBProtocolsCollection(DBTest):
    """Test class to get and set data in protocols' collection."""
    def test_0301_addprotocols(self):
        """A new protocol can be added."""
        self.protocols.add(Protocol(**TEST_COLL_PROTOCOLS[0]))
        protocol = self.protocols.get(TEST_COLL_PROTOCOLS[0]["name"])
        self.assertEqual(protocol.name, PROTOCOLS[0])
    def test_0302_addprotocols_exists(self):
        """We can't add a protocol that already exists."""
        with self.assertRaises(DBException):
            self.protocols.add(Protocol(**TEST_COLL_PROTOCOLS[0]))
    def test_0303_getprotocols_all(self):
        """All protocols can be returned as JSON."""
        self.assertEqual(self.protocols.all[0]["name"], PROTOCOLS[0])
    def test_0304_getprotocols_all(self):
        """All protocols can be returned as JSON."""
        self.assertTrue(isinstance(self.protocols.all_as_objects[0], Protocol))
        self.assertEqual(self.protocols.all_as_objects[0].name, PROTOCOLS[0])
    def test_0305_getprotocols_list(self):
        """All protocols can be returned as JSON."""
        self.assertEqual(self.protocols.list[0], PROTOCOLS[0])
    def test_0306_getprotocols_count(self):
        """All protocols can be returned as JSON."""
        self.assertEqual(self.protocols.count, 1)
    def test_0307_getprotocols(self):
        """We can get a protocol by its name."""
        protocol = self.protocols.get(PROTOCOLS[0])
        self.assertEqual(protocol.name, PROTOCOLS[0])
    def test_0308_getprotocols_alias(self):
        """We can get a protocol by its name."""
        p = self.protocols.get(PROTOCOLS[0])
        p.set("alias", "ANiceAlias")
        protocol = self.protocols.get("ANiceAlias")
        self.assertEqual(protocol.name, PROTOCOLS[0])
    def test_0309_getprotocols_noexists(self):
        """We can't get a protocol that does not exists."""
        with self.assertRaises(DBException):
            protocol = self.protocols.get("poulet")
    def test_0310_getprotocols_multi(self):
        """A search can return several protocols."""
        populate(self.protocols)
        self.protocols.get(PROTOCOLS[2]).set("alias", "Toto")
        self.protocols.get(PROTOCOLS[3]).set("alias", "Toti")
        try:
            protocol = self.protocols.get("Tot")
        except DBException as e:
            self.assertEqual(str(e)[:44], ERR_MULTIMATCH[:44])
    def test_0311_hasprotocols(self):
        """Method has() tells us if the protocol exists or not."""
        self.assertTrue(self.protocols.has(PROTOCOLS[0]))
        self.assertFalse(self.protocols.has("poulet"))
    def test_0312_checkprotocols(self):
        """An complete protocol passes check()."""
        self.protocols.check()
    def test_0313_deleteprotocols(self):
        """We can delete an existing protocol."""
        protocol = self.protocols.get(PROTOCOLS[0])
        self.protocols.delete(protocol)
        with self.assertRaises(DBException):
            self.protocols.get(PROTOCOLS[0])
    def test_0314_deleteprotocols_noexist(self):
        """We cannot delete a protocol that does not exist."""
        with self.assertRaises(DBException):
            self.protocols.delete(Protocol(name="pigeon"))

class Test04DBProtocolDocument(DBTest):
    """Test class to get and set data in protocols' collection."""
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # We need to init protocols because a packet is attached to one.
        populate(self.protocols)
    def test_0401_getprotocol_field(self):
        """We can get a value from its field."""
        protocol = self.protocols.get(PROTOCOLS[1])
        key, value = protocol.get("alias")
        self.assertEqual(value, TEST_COLL_PROTOCOLS[1]["alias"])
    def test_0402_getprotocol_nofield(self):
        """We can't get a field that does not exist."""
        protocol = self.protocols.get(PROTOCOLS[1])
        with self.assertRaises(DBException):
            protocol.get("pinguin")
    def test_0403_getprotocol_todict(self):
        """Protocol document can be returned as a dictionary."""
        pdict = self.protocols.get(PROTOCOLS[1]).to_dict()
        self.assertEqual(TEST_COLL_PROTOCOLS[1]["name"], pdict["name"])
        self.assertEqual(TEST_COLL_PROTOCOLS[1]["alias"], pdict["alias"])
        self.assertEqual(TEST_COLL_PROTOCOLS[1]["port"], pdict["port"])
    def test_0404_setprotocol_defaultfield(self):
        """Content can be added to protocol in default fields."""
        protocol = self.protocols.get(PROTOCOLS[1])
        protocol.set("description", "Isometric")
        self.assertEqual(protocol.get("description"), ("description", "Isometric"))
    def test_0405_setprotocol_nofield(self):
        """Content cannot be added to fields that don't already exist."""
        protocol = self.protocols.get(PROTOCOLS[1])
        with self.assertRaises(DBException):
            protocol.set("newfield", "content")
    def test_0406_setprotocol_newfield(self):
        """We can add new fields to protocols."""
        protocol = self.protocols.get(PROTOCOLS[1])
        protocol.add("newfield", "content")
        self.assertEqual(protocol.get("newfield"), ("newfield", "content"))
    def test_0407_setprotocol_strlist(self):
        """Content we add to list fields are appended to the previous value."""
        protocol = self.protocols.get(PROTOCOLS[1])
        protocol.set("alias", "Bob Woodward")
        self.assertEqual(protocol.get("alias")[1],
                         [TEST_COLL_PROTOCOLS[1]["alias"], "Bob Woodward"])
    def test_0408_setprotocol_strlistrep(self):
        """Content can be replaced in list fields if replace=True."""
        protocol = self.protocols.get(PROTOCOLS[1])
        protocol.set("alias", "Bob Woodward", replace=True)
        self.assertEqual(protocol.get("alias")[1], ["Bob Woodward"])
    def test_0408_setprotocol_strlistdup(self):
        """We cannot add a value that already exist in a list field."""
        protocol = self.protocols.get(PROTOCOLS[1])
        with self.assertRaises(DBException):
            protocol.set("alias", "Bob Woodward")
    def test_0409_setprotocol_link(self):
        """We can set a link to a link list field."""
        populate(self.links)
        protocol = self.protocols.get(PROTOCOLS[1])
        link = self.links.get(LINKS[0])
        protocol.set("nmap", link)
        self.assertEqual(protocol.get("nmap"), ("nmap", [link._id]))
    def test_0410_setprotocol_nolink(self):
        """We cannot set a link to a field that is not a link list."""
        protocol = self.protocols.get(PROTOCOLS[1])
        link = self.links.get(LINKS[0])
        with self.assertRaises(DBException):
            protocol.set("port", link)
    def test_0411_setprotocol_linklist(self):
        """A new link is appended to existing values in a link list."""
        protocol = self.protocols.get(PROTOCOLS[1])
        link0 = self.links.get(LINKS[0])
        link1 = self.links.get(LINKS[1])
        protocol.set("nmap", link1)
        self.assertEqual(protocol.get("nmap")[1], [link0._id, link1._id])
    def test_0412_setprotocol_linklistrep(self):
        """Content can be replaced in link list fields if replace=True."""
        protocol = self.protocols.get(PROTOCOLS[1])
        link2 = self.links.get(LINKS[2])
        protocol.set("nmap", link2, replace=True)
        self.assertEqual(protocol.get("nmap")[1], [link2._id])
    def test_0413_setprotocol_pkt(self):
        """We can set a packet to a packet list field."""
        populate(self.packets)
        protocol = self.protocols.get(PROTOCOLS[0])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[0])
        protocol.set("discovery", packet)
        self.assertEqual(protocol.get("discovery"), ("discovery", [packet._id]))
    def test_0414_setprotocol_nopkt(self):
        """We cannot set a link to a field that is not a link list."""
        protocol = self.protocols.get(PROTOCOLS[0])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[0])
        with self.assertRaises(DBException):
            protocol.set("port", packet)
    def test_0415_setprotocol_pktlist(self):
        """A new packet is appended to existing values in a packet list."""
        protocol = self.protocols.get(PROTOCOLS[0])
        packet0 = self.packets.get(PROTOCOLS[0], PACKETS[0])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[1])
        protocol.set("discovery", packet)
        self.assertEqual(protocol.get("discovery"),
                         ("discovery", [packet0._id, packet._id]))
    def test_0417_setprotocol_pktlistrep(self):
        """Content can be replaced in packet list fields if replace=True."""
        protocol = self.protocols.get(PROTOCOLS[0])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[2])
        protocol.set("discovery", packet, replace=True)
        self.assertEqual(protocol.get("discovery"),
                         ("discovery", [packet._id]))
    def test_0418_setprotocol_pktlistdup(self):
        """We cannot add a packet that already exist in a protocol."""
        protocol = self.protocols.get(PROTOCOLS[0])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[2])
        with self.assertRaises(DBException):
            protocol.set("discovery", packet)
    def test_0419_setprotocol_nopktlink(self):
        """We cannot add a packet to a link list."""
        protocol = self.protocols.get(PROTOCOLS[1])
        packet = self.packets.get(PROTOCOLS[0], PACKETS[0])
        with self.assertRaises(DBException):
            protocol.set("nmap", packet)
    def test_0420_setprotocol_nolinkpkt(self):
        """We cannot add a link to a packet list."""
        protocol = self.protocols.get(PROTOCOLS[1])
        link = self.links.get(LINKS[0])
        with self.assertRaises(DBException):
            protocol.set("nmap", link)
