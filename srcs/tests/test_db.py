# Turn/IP
# Claire-lex - 2023
# unittest : Database management (MongoDB)

import unittest
from os import system

from db import MongoDB, DBException
from config import mongodb

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

DB_HOST = mongodb.host
DB_PORT = mongodb.port
DB_TIMEOUT = mongodb.timeout
DB_DATABASE = mongodb.test_database

DB_CREATE = "/usr/bin/mongo --eval 'db=db.getSiblingDB(\"test-aip\");db.createCollection(\"protocols\");db.createCollection(\"links\");db.createCollection(\"packets\");' > /dev/null 2>&1"

#-----------------------------------------------------------------------------#
# Tests                                                                   #
#-----------------------------------------------------------------------------#

class Test01MongoDBProd(unittest.TestCase):
    """Test class to check that the production database loads.

    All the other tests are on test database.
    """
    def test_0101_loaddefaultdb_init(self):
        instance = MongoDB()
        self.assertIsNotNone(instance)
        self.assertIsNotNone(instance.client)
        self.assertIsNotNone(instance.db)

    def test_0102_loaddefaultdb_content(self):
        instance = MongoDB()
        self.assertEqual(instance.host, mongodb.host)
        self.assertEqual(instance.port, mongodb.port)
        self.assertEqual(instance.timeout, mongodb.timeout)
        self.assertEqual(instance.database, mongodb.database)

    @classmethod
    def tearDownClass(self):
        """Reset mongodb instance to use test db instead."""
        MongoDB.reset()
        
class Test02MongoDBTest(unittest.TestCase):
    """Test class to check interaction with the database (test)."""
    @classmethod
    def setUpClass(self):
        """Create database and collections if they don't exist."""
        # Not very pretty sorry :(
        system(DB_CREATE)

    def test_0201_loadtestdb_init(self):
        """Prerequisite: create test database in mongodb."""
        instance = MongoDB(DB_HOST, DB_PORT, DB_TIMEOUT, DB_DATABASE)
        self.assertIsNotNone(instance)
        self.assertIsNotNone(instance.client)
        self.assertIsNotNone(instance.db)

    def test_0202_loadtestdb_content(self):
        instance = MongoDB(DB_HOST, DB_PORT, DB_TIMEOUT, DB_DATABASE)
        self.assertEqual(instance.host, mongodb.host)
        self.assertEqual(instance.port, mongodb.port)
        self.assertEqual(instance.timeout, mongodb.timeout)
        self.assertEqual(instance.database, mongodb.test_database)

    @classmethod
    def tearDownClass(self):
        MongoDB.reset()
