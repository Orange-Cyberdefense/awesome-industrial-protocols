Turn/IP
=======

Turn/IP provides features to help the research process on industrial network
protocols. It is also used to manage the protocols' data written to the awesome
list.

Features:
- Manage and search through protocols' data
- Generate awesome list and protocols' pages
- Fetch information about protocols from various sources

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

So far, Turn/IP can be used only via command-line and it is not very convenient,
but the (almost) graphical interface is under development. Here is an overview
of the options (described below).

```
Usage: turn-ip.py [-h] [-f] [-S search] [-V field] [-L] [-A protocol] [-R
                  protocol] [-W protocol field value] [-D protocol] [-LL] [-AL
                  name url] [-RL url] [-WL url field value] [-DL url] [-LP] [-RP
                  protocol name] [-AP protocol name] [-WP protocol name field
                  value] [-DP protocol name] [-G] [-C] [-N protocol] [-F method
                  protocol] [-MI] [-ME]

Industrial network protocols browser and more.

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           never ask for confirmation
  -S search, --search search
                        list protocols matching the search
  -V field, --view field
                        view only a field of each protocol
  -L, --list            list all protocols
  -A protocol, --add protocol
                        add a new protocol
  -R protocol, --read protocol
                        read data of a protocol
  -W protocol field value, --write protocol field value
                        write data to a protocol
  -D protocol, --delete protocol
                        delete a protocol
  -LL, --list-links     list all links
  -AL name url, --add-link name url
                        add a new link
  -RL url, --read-link url
                        read data of a link
  -WL url field value, --write-link url field value
                        change data of a link
  -DL url, --delete-link url
                        delete a link
  -LP, --list-packets   list all packets
  -RP protocol name, --read-packet protocol name
                        read a packet from a protocol
  -AP protocol name, --add-packet protocol name
                        add a new packet
  -WP protocol name field value, --write-packet protocol name field value
                        change data of a packet
  -DP protocol name, --delete-packet protocol name
                        delete a packet
  -G, --gen             generate Markdown files with protocols' data
  -C, --check           check the database's content
  -N protocol, --note protocol
                        add personal notes for a protocol
  -F source protocol, --fetch source protocol
                        fetch data from various sources
  -MI, --mongoimport    Import database from JSON files in repository.
  -ME, --mongoexport    Export database to JSON files in repository.
```

### Protocols

#### View a protocol

A link can be referred to by its name or an alias, the name specified may not be
an exact match.

```
python turn-ip.py -R myproto
python turn-ip.py -R MyProt
```

Protocol data can be filtered:

- Option `-V` displays the value of one specific field for each protocol.
- Option `-S` displays the protocol avec value matching with the search text.

#### Add and modify a protocol

```
python turn-ip.py -A myproto # Add
python turn-ip.py -W myproto description "This is a nice protocol"
```

There are a few predefined fields, but setting a field that does not already
exist will create it. Predefined fields:
- `name` : Main name for the protocol
- `alias` : List of alternative names
- `description` : Short description
- `keywords` : List of words associated to the protocol
- `port` : If TCP/IP (prefer format 1234/tcp or 5678/udp)
- `access` : Is the specification available, for free or not
- `specs` : Link to the specifications
- `security` : Basic info about security features
- `nmap` : List of links to nmap scripts
- `wireshark` : Link to the wireshark dissector(s)
- `scapy` : Link to the scapy layer(s)
- `pcap` : List of links to PCAP samples
- `resources` : List of links related to that protocol


Some fields are strings, some others are array. For them, setting a value to the
field will actually append it to the existing one.

```
python turn-ip.py -W myproto keywords nice      # keywords: nice
python turn-ip.py -W myproto keywords protocol  # keywords: nice, protocol
```

Other fields take links as arguments (either one or an array of links). A link
is an object that can be refered to by its URL or name.

```
python turn-ip.py -W myproto wireshark https://link.to.wireshark/myproto
python turn-ip.py -W myproto wireshark "Wireshark dissector for Myproto"
```

If the URL does not match with an existing link object, it will create it.

### Links

#### View a link

A link can be referred to by its `name`or `url`:

```
python turn-ip.py -RL https//link.to/mylink
python turn-ip.py -RL mylink
```

#### Add or change a link

```
python turn-ip.py -AL mylink https//link.to/mylink # Add
python turn-ip.py -WL mylink description "This is a nice link"
```

A link object has predefined fields, only them can be changed.

- `name`: String
- `url`: Valid and reachable URL
- `description`: String
- `type`: Type of link, to choose between : "documentation", "article",
  "conference", "paper", "tool", "other" and "cve".

### Generators

The option `-G` generates the Markdown documentation from the database.  The
main Awesome List is created in `README.md` along with one page per protocol in
`protocols/<name>.md`. Protocol pages contain additional data.

Pages are built relying on a template in `srcs/out/templates`.

### Fetch

The option `-F` can be used to fetch data from various websites. Format:
`-F <source> <protocol>`. `source` is the source to use. Currently, the
following sources are supported:

- `wireshark`: Fetch a dissector on Wireshark's GitHub repository
- `scapy`: Fetch a layer on Scapy's GitHub repository
- `cve`: Fetch associated CVE on NIST's vulnerability database (slow)
- `youtube`: Fetch Youtube videos on selected channels (list in `config.py`)
- `openai`: Ask basic questions to OpenAI's models (not so reliable, more
  information [below](#note-on-ai-generated-content))
- `all`: Run all modes except OpenAI

> Sources `youtube` and `openai` require API keys for Google API (free) and OpenAI
  (chargeable).

Note on AI-generated content
----------------------------

Turn/IP contains code to gather AI-generated data using OpenAI's API. That's why
every page contains this warning: `All unreviewed AI-generated data is marked
with *`. However, you might notice that no data is actually marked with `*`.
What is AI used for then?

**TL;DR: AI is used for what it is: a search engine with an extra step and a
  text generator. It is never used to find resources because it does not find
  them, it invents them.**

The list of queries to OpenAI is [here](config.py#L174). It has been narrowed
down to 4 queries due to the inconsistency of responses. The remaining ones are
closed questions related to some basic characteristics of the protocols.

AI-generated data is mostly found in two types of fields:

- Description: AI is a fine text generator, so it generates fine descriptions.

- Port: AI helps restricting the search. It's much easier to find out if
  protocol A uses port 1234 rather than blindly searching for the port it uses
  (try it, you'll see). However, this really needs to be double-checked.

Also, my mother tongue is not English so I sometimes rely on it to correct some
mistakes, and I used Dall-e to generate the cool turnip in the logo.

> In the beginning there were also queries to retrieve basic information about
  the security of a protocol but the results were terrible so I removed it.

Contribute
----------

Instructions are in [CONTRIBUTING.md](../CONTRIBUTING.md).

If you made changes to the database and want to contribute, export the new
database:

```
python turn-ip.py --mongoexport
```

Files will be exported to `awesome-industrial-protocols/db/*.json`, you can send
them as a Pull Request.

Roadmap
-------

### Improvements

* [ ] Search option (search by name, port, number of CVE, etc.)
* [ ] Graphical user interface
* [ ] Add general notes (public) and personal notes (private) about protocols
* [ ] Add Scapy-based discovery packets for each protocol
* [ ] Add information about how to set up a test environment for each protocol
* [ ] Automatically fetch research papers databases (arxiv, else ?)
* [ ] Improve the "Security features" field (or replace it)
* [ ] Methods from Collection and Document-inherited objects can be refactored

### Fixes

* [ ] CLI: `-DL` should delete all references to the deleted link in protocols.
