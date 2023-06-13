# Awesome Industrial Protocols

Security-oriented list of industrial network protocols resources.

![Awesome Industrial Protocols](srcs/out/templates/logo-awesome-industrial-protocols.png)

In this repository:
* You are currently viewing the **Awesome Industrial Protocols** page.
* Detailed pages for protocols are available in `protocols`.
* All data is stored in MongoDB databases in `db`.
* **Turn/IP** (in `srcs`) is a handy tool to manipulate this data and simplify
the research and test process on industrial protocols.

> All AI-generated data is marked with `*`.

## Contents

- [BACnet/IP](#bacnetip)
- [CAN](#can)
- [CODESYS](#codesys)
- [DICOM](#dicom)
- [DNP3](#dnp3)
- [Ethernet/IP](#ethernetip)
- [IEC-60870-5-104](#iec608705104)
- [IEC-61850](#iec61850)
- [KNXnet/IP](#knxnetip)
- [Modbus](#modbus)
- [Niagara Fox](#niagarafox)
- [OPC-UA](#opcua)
- [S7comm](#s7comm)
- [UMAS](#umas)



## BACnet/IP
| Protocol | BACnet/IP |
|---|---|
| Name | BACnet/IP |
| Alias | BACnet |
| Description | Building automation and control network communication protocol for HVAC systems |
| Keywords | HVAC |
| Port | 47808/udp |
| Access | Paid |
| Specifications | [BACnet/IP Specification](https://bacnet.org/buy/) |
| Nmap script(s) | [bacnet-info](https://nmap.org/nsedoc/scripts/bacnet-info.html) |
| Wireshark dissector | [packet-bacnet.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-bacnet.c) |
### Articles
- [BACnet CVE-2019-12480](https://1modm.github.io/CVE-2019-12480.html) - On M's blog (2019)
### Tools
- [BACnet Stack](https://github.com/bacnet-stack/bacnet-stack) - BACnet open source protocol stack


## CAN
| Protocol | CAN |
|---|---|
| Name | CAN |
| Alias | CANbus, CANopen |
| Description | Communication protocol enabling data exchange between electronic components in vehicles. |
| Keywords | CANbus |
| Specifications | [ISO-11898](https://www.iso.org/standard/63648.html) |
| Wireshark dissector | [packet-canopen.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-canopen.c) |
| Scapy layer | [can.py](https://github.com/secdev/scapy/blob/master/scapy/layers/can.py) |



## CODESYS
| Protocol | CODESYS |
|---|---|
| Name | CODESYS |
| Alias | IEC-61131-3 |
| Description | PLC programming and runtime environment for industrial automation systems |
| Port | 1200/tcp, 2455/tcp |
| Access | Paid |
| Specifications | [CODESYS Specification](https://webstore.iec.ch/publication/4552) |



## DICOM
| Protocol | DICOM |
|---|---|
| Name | DICOM |
| Alias | DCM |
| Description | Communication and management of medical imaging information |
| Keywords | Radiography, Medical |
| Port | 104/tcp |
| Access | Free |
| Specifications | [DICOM Standard](https://www.dicomstandard.org/current/) |
| Nmap script(s) | [dicom-ping](https://nmap.org/nsedoc/scripts/dicom-ping.html) |
| Wireshark dissector | [packet-dcm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dcm.c) |
### Tools
- [pydicom](https://github.com/pydicom/pydicom) - Python package to read, modify and write DICOM files


## DNP3
| Protocol | DNP3 |
|---|---|
| Name | DNP3 |
| Alias | Distributed Network Protocol |
| Description | Industrial communication protocol for remote monitoring and control of automation systems. |
| Keywords | Power grid, Water |
| Port | 20000/tcp, 20000/udp |
| Access | Paid |
| Specifications | [IEEE 1815-2012](https://standards.ieee.org/ieee/1815/5414/) |
| Security | Optional authentication, optional encryption with TLS |
| Wireshark dissector | [packet-dnp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dnp.c) |
| Example Pcap(s) | [ICS-pcap DNP3](https://github.com/automayt/ICS-pcap/tree/master/DNP3) |
### Tools
- [dnp-info](https://github.com/sjhilt/Nmap-NSEs/blob/master/dnp3-info.nse) - Nmap discovery script for DNP3
- [FreyrSCADA DNP3](https://github.com/FreyrSCADA/DNP3) - DNP3 Protocol - Outstation Server and Client Master Simulator


## Ethernet/IP
| Protocol | Ethernet/IP |
|---|---|
| Name | Ethernet/IP |
| Alias | Enip |
| Description | Ethernet-based industrial communication protocol for industrial automation systems. |
| Keywords | CIP |
| Port | 44818/tcp, 2222/udp |
| Access | Paid |
| Specifications | [Ethernet/IP Specifications](https://www.odva.org/subscriptions-services/specifications) |
| Nmap script(s) | [enip-info](https://nmap.org/nsedoc/scripts/enip-info.html) |
| Wireshark dissector | [packet-enip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-enip.c) |
| Scapy layer | [enipTCP.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/enipTCP.py) |
| Example Pcap(s) | [ICS-pcap Ethernet/IP](https://github.com/automayt/ICS-pcap/tree/master/ETHERNET_IP) |
### Articles
- [Fuzzing and PR’ing: How We Found Bugs in a Popular Third-Party EtherNet/IP Protocol Stack](https://claroty.com/team82/research/opener-enip-stack-vulnerabilities) - Sharon Brizinov, Tal Keren (Claroty, 2021)
### Conferences
- [Hunting EtherNet/IP Protocol Stacks](https://www.youtube.com/watch?v=0jftEYDo0ao) - Conference by Sharon Brizinov @ SANS ICS Security Summit 2022
### Tools
- [CIPster](https://github.com/liftoff-sr/CIPster) - Ethernet/IP (Common Industrial Protocol) stack in C++
- [enip-stack-detector](https://github.com/claroty/enip-stack-detector) - EtherNet/IP & CIP Stack Detector
- [OpENer](https://github.com/EIPStackGroup/OpENer) - EtherNet/IP stack for I/O adapter devices
- [Redpoint](https://github.com/digitalbond/Redpoint) - Digital Bond's ICS enumeration tools (nmap scripts)
- [scapy-cip-enip](https://github.com/scy-phy/scapy-cip-enip) - Ethernet/IP dissectors for Scapy


## IEC-60870-5-104
| Protocol | IEC-60870-5-104 |
|---|---|
| Name | IEC-60870-5-104 |
| Alias | IEC-104 |
| Description | Grid communication protocol for control and monitoring. |
| Port | 2404/tcp |
| Access | Paid |
| Specifications | [IEC-60870-5-104 Specification](https://webstore.iec.ch/publication/25035) |
| Nmap script(s) | [iec-identify](https://nmap.org/nsedoc/scripts/iec-identify.html) |
| Wireshark dissector | [packet-iec104.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-iec104.c) |
| Scapy layer | [iec104.py](https://github.com/secdev/scapy/tree/master/scapy/contrib/scada/iec104) |
| Example Pcap(s) | [ICS-pcap IEC-60870-5-104](https://github.com/automayt/ICS-pcap/tree/master/IEC%2060870) |
### Papers
- [Description and analysis of IEC 104 Protocol](https://www.fit.vut.cz/research/publication/11570/.en) - Technical report by Petr Matousek @ Faculty of Information Techology, Czech Republic (2017)
### Tools
- [FreyrSCADA IEC-60870-5-104](https://github.com/FreyrSCADA/IEC-60870-5-104) - IEC 60870-5-104 Protocol - RTU Server and Master Client Simulator


## IEC-61850
| Protocol | IEC-61850 |
|---|---|
| Name | IEC-61850 |
| Alias | IEC-61850/GOOSE, IEC-61850/GSSE, IEC-61850/SV |
| Description | Communication networks and systems for power utility automation |
| Keywords | Power grid |
| Access | Paid |
| Specifications | [IEC 61850 Specification](https://webstore.iec.ch/publication/6028) |
| Wireshark dissector | [packet-goose.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-goose.c), [packet-sv.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sv.c) |



## KNXnet/IP
| Protocol | KNXnet/IP |
|---|---|
| Name | KNXnet/IP |
| Alias | KNX, KNX/IP, Konnex |
| Description | Protocol for home and building automation systems. |
| Keywords | BMS, BAS, Building |
| Port | 3671/udp |
| Access | Free |
| Specifications | [KNXnet/IP Specifications](https://my.knx.org/en/shop/knx-specifications) |
| Security | Optional, Security extensions available |
| Nmap script(s) | [knx-gateway-discover](https://nmap.org/nsedoc/scripts/knx-gateway-discover.html) |
| Wireshark dissector | [packet-knxip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-knxip.c) |
| Scapy layer | [knx.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/knx.py) |
### Documentations
- [knx.org](https://www.knx.org/knx-en/for-professionals/index.php) - KNX official website
### Conferences
- [Learn how to control every room at a luxury hotel remotely](https://www.youtube.com/watch?v=RX-O4XuCW1Y) - Conference by Jesus Molina @ DEF CON 22 (2014)
- [Sneak into buildings with KNXnet/IP](https://www.youtube.com/watch?v=QofeTV39kQE) - Conference by Claire Vacherot @ DEF CON 29 (2020)
### Tools
- [BOF](https://github.com/Orange-Cyberdefense/bof) - Testing framework for industrial protocols
- [ETS](https://www.knx.org/knx-en/for-professionals/software/ets-professional/) - Engineering Tool Software for KNXnet/IP (ETS Demo is free)
- [KNX Virtual](https://www.knx.org/knx-en/for-professionals/get-started/knx-virtual/index.php) - Windows-based application simulating a KNX installation
- [knxd](https://github.com/knxd/knxd) - KNXd service
- [KNXmap](https://github.com/takeshixx/knxmap) - KNXnet/IP scanning and auditing tool
- [XKNX](https://github.com/XKNX/xknx) - A KNX library written in Python


## Modbus
| Protocol | Modbus |
|---|---|
| Name | Modbus |
| Alias | Modbus TCP |
| Port | 502/tcp |
| Specifications | [Modbus TCP Specification](https://modbus.org/specs.php) |
| Nmap script(s) | [modbus-discover](https://nmap.org/nsedoc/scripts/modbus-discover.html) |
| Wireshark dissector | [packet-mbtcp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-mbtcp.c) |
| Scapy layer | [modbus.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/modbus.py) |
### Tools
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS


## Niagara Fox
| Protocol | Niagara Fox |
|---|---|
| Name | Niagara Fox |
| Alias | Fox |
| Description | Communication protocol used by Tridium Niagara devices |
| Keywords | Tridium |
| Port | 1911/tcp, 3011/tcp, 4911/tcp, 5011/tcp |
| Nmap script(s) | [fox-info](https://nmap.org/nsedoc/scripts/fox-info.html) |
### Tools
- [foxdissector](https://github.com/MartinoTommasini/foxdissector) - Wireshark dissector for the Niagara Fox protocol in Lua


## OPC-UA
| Protocol | OPC-UA |
|---|---|
| Name | OPC-UA |
| Alias | OPCUA |
| Port | 4840/tcp, 4840/udp, 4843/tcp (TLS)  |
| Wireshark dissector | [OPC-UA Plugin](https://github.com/wireshark/wireshark/tree/master/plugins/epan/opcua) |
### Tools
- [python-opcua](https://github.com/FreeOpcUa/python-opcua) - OPC UA Client and Server in Python


## S7comm
| Protocol | S7comm |
|---|---|
| Name | S7comm |
| Alias | S7 |
| Port | 102/tcp |
| Nmap script(s) | [s7-info](https://nmap.org/nsedoc/scripts/s7-info.html) |
| Wireshark dissector | [packet-s7comm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-s7comm.c) |
| Example Pcap(s) | [ICS-pcap S7](https://github.com/automayt/ICS-pcap/tree/master/S7) |
### Articles
- [The Siemens S7 Communication - Part 1 General Structure](http://gmiru.com/article/s7comm/) - On GyM's Personal Blog (2016)
- [The Siemens S7 Communication - Part 2 Job Requests and Ack Data](http://gmiru.com/article/s7comm-part2/) - On GyM's Personal Blog (2017)
### Tools
- [s7scan](https://github.com/klsecservices/s7scan) - Scan networks to gather basic information about Siemens PLCs


## UMAS
| Protocol | UMAS |
|---|---|
| Name | UMAS |
### Articles
- [The secrets of Schneider Electric’s UMAS protocol](https://ics-cert.kaspersky.com/publications/reports/2022/09/29/the-secrets-of-schneider-electrics-umas-protocol/) - Kaspersky ICS CERT (2022)
- [The Unity (UMAS) protocol (Part I)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-i.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part II)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-ii.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part III)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-iii.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part IV)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-iv.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part V)](http://lirasenlared.blogspot.com/2017/09/the-unity-umas-protocol-part-v.html) - Liras en la red (2017)
### Tools
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS

> **awesome-industrial-protocols** is licensed under
[CC0](https://creativecommons.org/publicdomain/zero/1.0/). **Turn/IP** is
licensed under [GPL-v3](https://www.gnu.org/licenses/gpl-3.0.en.html).
