Turn/IP
=======

Turn/IP provides features to help the research process on industrial network
protocols. It is also used to manage the protocols' data written to the awesome
list.

Features:
- Manage and search through protocols' data
- Generate awesome list and protocols' pages
- Scrap information about protocols from various sources

Soon:
- Add personal research notes on protocols
- Get enough data to send basic discovery commands on the network
- Get enough data to run a basic Scapy-based fuzzer

Install
-------

* Install MongoDB following the [official
  documentation](https://www.mongodb.com/docs/manual/installation/).

> Note: You may need libgconf: `sudo apt-get install gconf-service`

* Install the pymongo library: `pip install pymongo`

* Start daemon with `sudo systemctl start mongod`

> Note: Replace `start` with `enable` to run it automatically on startup.

* Import database and collections to MongoDB :

```
python turn-ip.py --mongoimport
```

> Files located in awesome-industrial-protocols/db/*.json will be imported.

Now you're all set!

Usage
-----

TODO

Contribute
----------

Instructions are in [CONTRIBUTING.md](../CONTRIBUTING.md).

If you made changes to the database and want to contribute, export the new
database:

```
python turn-ip.py --mongoexport
```

> Files will be exported to awesome-industrial-protocols/db/*.json
