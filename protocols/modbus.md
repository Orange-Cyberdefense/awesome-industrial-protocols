# Modbus

| Protocol | Modbus |
|---|---|
| Name | Modbus |
| Aliases | Modbus TCP |
| Description | Widely used industrial communication protocol |
| Port(s) | 502/tcp |
| Specifications | [Modbus TCP Specification](https://modbus.org/specs.php) |
| Nmap script(s) | [modbus-discover.nse](https://nmap.org/nsedoc/scripts/modbus-discover.html), [modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) |
| Wireshark dissector | [packet-mbtcp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-mbtcp.c) |
| Scapy layer | [modbus.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/modbus.py) |
| Example Pcap(s) | [ICS-pcap Modbus](https://github.com/automayt/ICS-pcap/tree/master/MODBUS), [S4x15 ICS Village PCAP Files](https://www.netresec.com/?page=DigitalBond_S4) |

## Documentations
- [Modbus Mesulog Standard Functions Help](http://www.mesulog.fr/help/modbus/index.html?page=read-device-identification-f43.html) - Description for Modbus standard functions
## Articles
- [Articles about Modbus](https://ozeki.hu/p_5841-modbus-protocol.html) - Ozeki
- [Introduction to Modbus and Modbus Function Codes](https://control.com/technical-articles/introduction-to-modbus-and-modbus-function-codes/) - Shawn Dietrich, Control Automation (2023)
## Conferences
- [Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - Jimmy Wylie @ DEF CON 30 (2022)
- [Common Flaws in ICS Network Protocols](https://www.youtube.com/watch?v=Bhq4kC52Qg8) - Mars Cheng & Selmon Yang @ Hack In The Box (2020)
- [DEF CON 33 - There and Back Again: Detecting OT Devices Across Protocol Gateways - Rob King](https://www.youtube.com/watch?v=YBPYYk8FIkc) - @ DEF CON (2025)
- [From Pass-the-Hash to Code Execution on Schneider Electric M340 PLCs](https://www.youtube.com/watch?v=RL7vtbm03Os) - @ Black Hat (2025)
- [Fun with Modbus 0x5a Nothing New Still Relevant?](https://www.youtube.com/watch?v=A_B69Rifu1g) - Arnaud Soullié @ DEF CON 25 ICS Village (2017)
- [Industrial Control Systems : Pentesting PLCs 101 (Part 1/2)](https://www.youtube.com/watch?v=iGwm6-lyn2Y) - Arnaud Soullie @ Black Hat Europe (2014)
- [Industrial Control Systems : Pentesting PLCs 101 (Part 2/2)](https://www.youtube.com/watch?v=rP_Jys1_OJk) - Arnaud Soullie @ Black Hat Europe (2014)
- [Industrial Protocol Gateways Under Analysis](https://www.youtube.com/watch?v=Rbkw_jsTBsY) - Marco Balduzzi @ Black Hat USA (2020)
- [Industrial Protocol Gateways: A Deep-Dive of Moxa MGate 5105-MB-EIP](https://www.youtube.com/watch?v=tRi2te9yBuk) - Philippe Lin @ Hack In The Box (2020)
- [Modbus Enumeration | SANS ICS Concepts](https://www.youtube.com/watch?v=QO99yojavvE) - @ SANS ICS Security (2021)
- [Modbus Man-In-The-Middle | SANS ICS Concepts](https://www.youtube.com/watch?v=-1WbegoU8i0) - @ SANS ICS Security (2021)
- [Modbus Traffic Analysis | SANS ICS Concepts](https://www.youtube.com/watch?v=OAsLdXzKQo8) - @ SANS ICS Security (2021)
- [ModScan: A SCADA MODBUS Network Scanner](https://www.youtube.com/watch?v=O_trNBh31lM) - Mark Bristow @ DEF CON 16 (2013)
- [Out of Control: Demonstrating SCADA device exploitation](https://www.youtube.com/watch?v=FTzAkEnwx_c) - Eric Forner & Brian Meixell @ Black Hat USA (2013)
- [Stealing PLC Intellectual Property: A Red Teaming Story](https://www.youtube.com/watch?v=SWFt9T8sGX0) - Matteo Beccaro @ Hack In The Box (2017)
- [The SCADA That Didn't Cry Wolf- Who's Really Attacking Your ICS Devices](https://www.youtube.com/watch?v=0M8nVv0bz6k) - Kyle Wilhoit @ Black Hat USA (2013)
- [Understanding SCADA's Modbus Protocol](https://www.youtube.com/watch?v=oVDYaG2HInU) - Justin Searle @ Black Hat Asia (2015)
- [Unraveling SCADA Protocols Using Sulley Fuzzer](https://www.youtube.com/watch?v=UUta_Ord8GI) - Ganesh Devarajan @ DEF CON 15 (2014)
## Tools
- [ctmodbus](https://github.com/ControlThings-io/ctmodbus) - A tool to interact with the Modbus protocol
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS
- [mbtget](https://github.com/sourceperl/mbtget) - A simple Modbus/TCP client in Perl
- [PyModbus](https://github.com/pymodbus-dev/pymodbus) - A full modbus protocol written in python
