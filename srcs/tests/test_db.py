# Turn/IP
# Claire-lex - 2023
# unittest : Database management (MongoDB)

import unittest
from os import system

from db import MongoDB, DBException
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

TEST_COLL_PROTOCOLS = ("Seagull", "Owl")
TEST_COLL_LINKS = (
    {"name": "Oh shit git", "url": "https://ohshitgit.com/", "description": "Very useful"},
    {}
)
TEST_COLL_PACKETS = (
    {"protocol": TEST_COLL_PROTOCOLS[0], "name": "ANicePacket",
     "description": "ANiceDescription", "scapy_pkt": "A()/Nice()/Pkt()",
     "raw_pkt": "0xANicePacket"},
    {}
)

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
        db.protocols.delete_one({"name": coll})
    for coll in TEST_COLL_LINKS:
        if "url" in coll.keys():
            db.links.delete_one({"url": coll["url"]})
    for coll in TEST_COLL_PACKETS:
        if "name" in coll.keys():
            db.packets.delete_one({"protocol": coll["protocol"],
                                   "name": coll["name"]})
    
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

class Test03DBAddProtocols(DBTest):
    """Test class to check that we can add data to the database."""
    def test_0301_addprotocol(self):
        """A new protocol can be added."""
        self.protocols.add(Protocol(name=TEST_COLL_PROTOCOLS[0]))
        protocol = self.protocols.get(TEST_COLL_PROTOCOLS[0])
        self.assertEqual(protocol.names, [TEST_COLL_PROTOCOLS[0]])
    def test_0302_addprotocol_exists(self):
        """We can't add a protocol that already exists."""
        with self.assertRaises(DBException):
            self.protocols.add(Protocol(name=TEST_COLL_PROTOCOLS[0]))
    def test_0303_addprotocol_prefield(self):
        """Content can be added to protocol's predefined fields."""
        pass # TODO multiple tests : append, replace, etc.
    def test_0304_addprotocol_newfield(self):
        """Content can be added to protocol in new fields."""
        pass # TODO multiple tests

class Test04DBAddLinks(DBTest):
    def test_0401_addlink(self):
        """A new link can be added."""
        self.links.add(Link(**TEST_COLL_LINKS[0]))
        link = self.links.get(TEST_COLL_LINKS[0]["url"])
        self.assertEqual(link.name, TEST_COLL_LINKS[0]["name"])
        self.assertEqual(link.url, TEST_COLL_LINKS[0]["url"])
        self.assertEqual(link.description, TEST_COLL_LINKS[0]["description"])
    def test_0402_addlink_exists(self):
        """We can't add a link that already exists."""
        with self.assertRaises(DBException):
            self.links.add(Link(**TEST_COLL_LINKS[0]))
    def test_0403_addlink_protocol(self):
        """A link can be added to a protocol."""
        pass # TODO
    def test_0404_addlink_prefield(self):
        """Content can be added to a link's predefined fields."""
        pass # TODO multiple tests
    def test_0405_addlink_badprefield(self):
        """Fields do not accept unallowed values."""
        pass # TODO unknown type, invalid url
    def test_0406_addlink_field(self):
        """Content cannot be added to link in unknown fields."""
        pass # TODO

class Test05DBAddPackets(DBTest):
    def test_0501_addpacket(self):
        """A new packet can be added."""
        self.packets.add(Packet(**TEST_COLL_PACKETS[0]))
        packet = self.packets.get(TEST_COLL_PACKETS[0]["protocol"],
                                  TEST_COLL_PACKETS[0]["name"])
        self.assertEqual(packet.name, TEST_COLL_PACKETS[0]["name"])
    def test_0502_addpacket_exists(self):
        """We can't add a packet that already exists."""
        with self.assertRaises(DBException):
            self.packets.add(Packet(**TEST_COLL_PACKETS[0]))
    def test_0503_addpacket_noproto(self):
        """We can't add a packet with an unknown protocol."""
        pass # TODO
    def test_0504_addpacket_prefield(self):
        """Content can be added to a packet's predefined fields."""
        pass # TODO
    def test_0505_addpacket_badprefield(self):
        """Fields do not accept unallowed values."""
        pass # TODO
    def test_0506_addpacket_field(self):
        """Content cannot be added to packet in unknown fields."""
        pass # TODO

class Test06DBGetProtocols(DBTest):
    def test_0601_getprotocol_properties(self):
        """Protocols info can be retrieved from DB class properties."""
        pass # TODO protocols, protocols_count, protocols_all
    def test_0602_getprotocol(self):
        """A protocol can be retrieved with collection methods."""
        pass # TODO get()
    def test_0603_getprotocol_noexists(self):
        """We can't get a protocol that does not exists."""
        pass # TODO get()
    def test_0604_hasprotocol(self):
        """Method has tells us if the protocol exists or not."""
        pass # TODO has()
    def test_0605_getprotocol_todict(self):
        """Protocol document can be returned as a dictionary."""
        pass # TODO to_dict()
    def test_0606_getprotocol_byalias(self):
        """A protocol can be found using one if its aliases."""
        pass # TODO
    def test_0607_getprotocol_multi(self):
        """A search can return several protocols."""
        pass # TODO

class Test07DBGetLinks(DBTest):
    def test_0701_getlinks_properties(self):
        """Links info can be retrieved from DB class properties."""
        pass # TODO links, links_count, links_all
    def test_0702_getlink(self):
        """A link can be retrieved with collection methods."""
        pass # TODO get()
    def test_0703_getlink_noexists(self):
        """We can't get a link that does not exists."""
        pass # TODO get()
    def test_0704_haslink(self):
        """Method has tells us if the link exists or not."""
        pass # TODO has()
    def test_0705_getlink_todict(self):
        """Link document can be returned as a dictionary."""
        pass # TODO to_dict()

class Test08DBGetPackets(DBTest):
    def test_0801_getpackets_properties(self):
        """Packets info can be retrieved from DB class properties."""
        pass # TODO packets, packets_count, packets_all
    def test_0802_getpacket(self):
        """A packet can be retrieved with collection methods."""
        pass # TODO get()
    def test_0803_getpacket_noexists(self):
        """We can't get a packet that does not exists."""
        pass # TODO get()
    def test_0804_haspacket(self):
        """Method has tells us if the packet exists or not."""
        pass # TODO has()
    def test_0805_getpacket_todict(self):
        """Packet document can be returned as a dictionary."""
        pass # TODO to_dict()

class Test09DelProtocols(DBTest):
    def test_0901_delprotocol(self):
        """A protocol can be deleted."""
        pass # TODO delete()
    def test_0902_delprotocol_noexist(self):
        """We can't delete a protocol that does not exist."""
        pass # TODO delete()

class Test10DelLinks(DBTest):
    def test_1001_dellink(self):
        """A link can be deleted, all the references to it are deleted."""
        pass # TODO delete()
    def test_1002_dellink_noexist(self):
        """We can't delete a protocol that does not exist."""
        pass # TODO delete()

class Test11DelProtocols(DBTest):
    def test_1101_delpacket(self):
        """A packet and its reference in a protocol can be deleted"""
        pass # TODO delete()
    def test_1102_delpacket_noexist(self):
        """We can't delete a packet that does not exist."""
        pass # TODO delete()
