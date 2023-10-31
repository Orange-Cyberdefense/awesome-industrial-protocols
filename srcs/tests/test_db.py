# Turn/IP
# Claire-lex - 2023
# unittest : Database management (MongoDB)

import unittest
from os import system

from db import MongoDB, DBException, Protocols, Protocol, Links, Link, Packets
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
TEST_COLL_PACKETS = ("Seagull", "Owl")

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
# Base class for tests on test-aip database                                   #
#-----------------------------------------------------------------------------#

class DBAbstract(unittest.TestCase):
    """Every test relying on the TestDB must inherit this one."""
    @classmethod
    def setUpClass(self):
        """Create database and collections if they don't exist."""
        # Not very pretty sorry :(
        system(DB_CREATE)
        self.db = MongoDB(DB_HOST, DB_PORT, DB_TIMEOUT, DB_DATABASE)
        # Empty the test database
        for coll in TEST_COLL_PROTOCOLS:
            self.db.protocols.delete_one({"name": coll})
        for coll in TEST_COLL_LINKS:
            if "url" in coll.keys():
                self.db.links.delete_one({"url": coll["url"]})
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
        
class Test02DBTest(DBAbstract):
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

class Test03DBAdd(DBAbstract):
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
    def test_0303_addlink(self):
        """A new link can be added."""
        self.links.add(Link(**TEST_COLL_LINKS[0]))
        link = self.links.get(TEST_COLL_LINKS[0]["url"])
        self.assertEqual(link.name, TEST_COLL_LINKS[0]["name"])
        self.assertEqual(link.url, TEST_COLL_LINKS[0]["url"])
        self.assertEqual(link.description, TEST_COLL_LINKS[0]["description"])
    def test_0304_addprotocol_exists(self):
        """We can't add a link that already exists."""
        with self.assertRaises(DBException):
            self.links.add(Link(**TEST_COLL_LINKS[0]))
