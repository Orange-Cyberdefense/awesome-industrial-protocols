# Awesome Industrial Protocols

Offensive security-oriented list of industrial network protocols resources.

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
- [CSPv4](#cspv4)
- [DICOM](#dicom)
- [DNP3](#dnp3)
- [Ether-S-I/O](#ethersio)
- [EtherCAT](#ethercat)
- [Ethernet/IP](#ethernetip)
- [FINS](#fins)
- [GE-SRTP](#gesrtp)
- [HART-IP](#hartip)
- [HL7](#hl7)
- [IEC-60870-5-104](#iec608705104)
- [IEC-61850](#iec61850)
- [KNXnet/IP](#knxnetip)
- [Modbus](#modbus)
- [Niagara Fox](#niagarafox)
- [OPC-DA](#opcda)
- [OPC-UA](#opcua)
- [PC-WORX](#pcworx)
- [POWERLINK](#powerlink)
- [ProConOs](#proconos)
- [Profinet-DCP](#profinetdcp)
- [Profinet-IO](#profinetio)
- [S-Bus](#sbus)
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
| Nmap script(s) | [bacnet-info.nse](https://nmap.org/nsedoc/scripts/bacnet-info.html) |
| Wireshark dissector | [packet-bacnet.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-bacnet.c) |
| Related CVE | [CVE-2018-10238](https://nvd.nist.gov/vuln/detail/CVE-2018-10238), [CVE-2018-18878](https://nvd.nist.gov/vuln/detail/CVE-2018-18878), [CVE-2019-12480](https://nvd.nist.gov/vuln/detail/CVE-2019-12480), [CVE-2021-41545](https://nvd.nist.gov/vuln/detail/CVE-2021-41545) |
### Articles
- [BACnet CVE-2019-12480](https://1modm.github.io/CVE-2019-12480.html) - On M's blog (2019)
### Tools
- [BACnet Stack](https://github.com/bacnet-stack/bacnet-stack) - BACnet open source protocol stack


## CAN
| Protocol | CAN |
|---|---|
| Name | CAN |
| Alias | CANbus, CANopen |
| Description | Communication protocol enabling data exchange between electronic components in vehicles |
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
| Nmap script(s) | [codesys-v2-discover.nse](https://github.com/digitalbond/Redpoint/blob/master/codesys-v2-discover.nse) |
| Related CVE | [CVE-2012-4704](https://nvd.nist.gov/vuln/detail/CVE-2012-4704), [CVE-2012-4705](https://nvd.nist.gov/vuln/detail/CVE-2012-4705), [CVE-2012-4706](https://nvd.nist.gov/vuln/detail/CVE-2012-4706), [CVE-2012-4707](https://nvd.nist.gov/vuln/detail/CVE-2012-4707), [CVE-2012-4708](https://nvd.nist.gov/vuln/detail/CVE-2012-4708), [CVE-2013-2781](https://nvd.nist.gov/vuln/detail/CVE-2013-2781), [CVE-2014-0769](https://nvd.nist.gov/vuln/detail/CVE-2014-0769), [CVE-2015-6460](https://nvd.nist.gov/vuln/detail/CVE-2015-6460), [CVE-2015-6482](https://nvd.nist.gov/vuln/detail/CVE-2015-6482), [CVE-2018-5459](https://nvd.nist.gov/vuln/detail/CVE-2018-5459), [CVE-2018-8836](https://nvd.nist.gov/vuln/detail/CVE-2018-8836), [CVE-2019-5105](https://nvd.nist.gov/vuln/detail/CVE-2019-5105), [CVE-2019-9009](https://nvd.nist.gov/vuln/detail/CVE-2019-9009), [CVE-2019-9010](https://nvd.nist.gov/vuln/detail/CVE-2019-9010), [CVE-2019-9012](https://nvd.nist.gov/vuln/detail/CVE-2019-9012), [CVE-2020-6081](https://nvd.nist.gov/vuln/detail/CVE-2020-6081), [CVE-2020-7052](https://nvd.nist.gov/vuln/detail/CVE-2020-7052), [CVE-2021-29242](https://nvd.nist.gov/vuln/detail/CVE-2021-29242), [CVE-2021-34593](https://nvd.nist.gov/vuln/detail/CVE-2021-34593), [CVE-2021-34595](https://nvd.nist.gov/vuln/detail/CVE-2021-34595), [CVE-2021-34596](https://nvd.nist.gov/vuln/detail/CVE-2021-34596), [CVE-2021-36764](https://nvd.nist.gov/vuln/detail/CVE-2021-36764), [CVE-2022-22515](https://nvd.nist.gov/vuln/detail/CVE-2022-22515), [CVE-2022-22517](https://nvd.nist.gov/vuln/detail/CVE-2022-22517), [CVE-2022-31804](https://nvd.nist.gov/vuln/detail/CVE-2022-31804), [CVE-2022-31805](https://nvd.nist.gov/vuln/detail/CVE-2022-31805) |



## CSPv4
| Protocol | CSPv4 |
|---|---|
| Name | CSPv4 |
| Alias | AB CSPv4, AB/Ethernet |
| Description | Allen-Bradley's protocol for industrial Ethernet communication |
| Keywords | Allen-Bradley |
| Port | 2222/tcp |
| Nmap script(s) | [cspv4-info.nse](https://github.com/digitalbond/Redpoint/blob/master/cspv4-info.nse) |



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
| Nmap script(s) | [dicom-ping.nse](https://nmap.org/nsedoc/scripts/dicom-ping.html) |
| Wireshark dissector | [packet-dcm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dcm.c) |
### Tools
- [pydicom](https://github.com/pydicom/pydicom) - Python package to read, modify and write DICOM files


## DNP3
| Protocol | DNP3 |
|---|---|
| Name | DNP3 |
| Alias | Distributed Network Protocol |
| Description | Industrial communication protocol for remote monitoring and control of automation systems |
| Keywords | Power grid, Water |
| Port | 20000/tcp, 20000/udp |
| Access | Paid |
| Specifications | [IEEE 1815-2012](https://standards.ieee.org/ieee/1815/5414/) |
| Security | Optional authentication, optional encryption with TLS |
| Nmap script(s) | [dnp3-info.nse](https://github.com/digitalbond/Redpoint/blob/master/dnp3-info.nse) |
| Wireshark dissector | [packet-dnp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dnp.c) |
| Example Pcap(s) | [ICS-pcap DNP3](https://github.com/automayt/ICS-pcap/tree/master/DNP3) |
### Tools
- [dnp-info](https://github.com/sjhilt/Nmap-NSEs/blob/master/dnp3-info.nse) - Nmap discovery script for DNP3
- [FreyrSCADA DNP3](https://github.com/FreyrSCADA/DNP3) - DNP3 Protocol - Outstation Server and Client Master Simulator


## Ether-S-I/O
| Protocol | Ether-S-I/O |
|---|---|
| Name | Ether-S-I/O |
| Alias | EtherSIO, ESIO |
| Description | Proprietary protocol for Saia PCD controller I/O communication |
| Keywords | SAIA |
| Port | 6060/udp |
| Wireshark dissector | [packet-esio.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-esio.c) |
| Example Pcap(s) | [ICS-pcap Ether-S-I/O](https://github.com/automayt/ICS-pcap/tree/master/ETHERSIO) |



## EtherCAT
| Protocol | EtherCAT |
|---|---|
| Name | EtherCAT |
| Alias | ECATF, ECAT |
| Description | Real-time industrial Ethernet communication protocol for automation systems |
| Scapy layer | [ethercat.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/ethercat.py) |
| Example Pcap(s) | [ICS-pcap EtherCAT](https://github.com/automayt/ICS-pcap/tree/master/ETHERCAT/ethercat) |



## Ethernet/IP
| Protocol | Ethernet/IP |
|---|---|
| Name | Ethernet/IP |
| Alias | Enip |
| Description | Ethernet-based industrial communication protocol for industrial automation systems |
| Keywords | CIP |
| Port | 44818/tcp, 2222/udp |
| Access | Paid |
| Specifications | [Ethernet/IP Specifications](https://www.odva.org/subscriptions-services/specifications) |
| Nmap script(s) | [enip-info.nse](https://nmap.org/nsedoc/scripts/enip-info.html), [enip-enumerate.nse](https://github.com/digitalbond/Redpoint/blob/master/enip-enumerate.nse) |
| Wireshark dissector | [packet-enip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-enip.c) |
| Scapy layer | [enipTCP.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/enipTCP.py) |
| Example Pcap(s) | [ICS-pcap Ethernet/IP](https://github.com/automayt/ICS-pcap/tree/master/ETHERNET_IP), [ICS-pcap EIP](https://github.com/automayt/ICS-pcap/tree/master/EIP) |
| Related CVE | [CVE-2012-6435](https://nvd.nist.gov/vuln/detail/CVE-2012-6435), [CVE-2012-6436](https://nvd.nist.gov/vuln/detail/CVE-2012-6436), [CVE-2012-6438](https://nvd.nist.gov/vuln/detail/CVE-2012-6438), [CVE-2012-6439](https://nvd.nist.gov/vuln/detail/CVE-2012-6439), [CVE-2012-6441](https://nvd.nist.gov/vuln/detail/CVE-2012-6441), [CVE-2012-6442](https://nvd.nist.gov/vuln/detail/CVE-2012-6442), [CVE-2018-14827](https://nvd.nist.gov/vuln/detail/CVE-2018-14827), [CVE-2019-6815](https://nvd.nist.gov/vuln/detail/CVE-2019-6815), [CVE-2020-13530](https://nvd.nist.gov/vuln/detail/CVE-2020-13530), [CVE-2020-13556](https://nvd.nist.gov/vuln/detail/CVE-2020-13556), [CVE-2020-13573](https://nvd.nist.gov/vuln/detail/CVE-2020-13573), [CVE-2020-25159](https://nvd.nist.gov/vuln/detail/CVE-2020-25159), [CVE-2020-6083](https://nvd.nist.gov/vuln/detail/CVE-2020-6083), [CVE-2020-6084](https://nvd.nist.gov/vuln/detail/CVE-2020-6084), [CVE-2020-6085](https://nvd.nist.gov/vuln/detail/CVE-2020-6085), [CVE-2020-6086](https://nvd.nist.gov/vuln/detail/CVE-2020-6086), [CVE-2020-6087](https://nvd.nist.gov/vuln/detail/CVE-2020-6087), [CVE-2020-6088](https://nvd.nist.gov/vuln/detail/CVE-2020-6088), [CVE-2021-20987](https://nvd.nist.gov/vuln/detail/CVE-2021-20987), [CVE-2021-21777](https://nvd.nist.gov/vuln/detail/CVE-2021-21777), [CVE-2021-27478](https://nvd.nist.gov/vuln/detail/CVE-2021-27478), [CVE-2021-27482](https://nvd.nist.gov/vuln/detail/CVE-2021-27482), [CVE-2021-27498](https://nvd.nist.gov/vuln/detail/CVE-2021-27498), [CVE-2021-27500](https://nvd.nist.gov/vuln/detail/CVE-2021-27500), [CVE-2021-34754](https://nvd.nist.gov/vuln/detail/CVE-2021-34754), [CVE-2021-36765](https://nvd.nist.gov/vuln/detail/CVE-2021-36765), [CVE-2022-1737](https://nvd.nist.gov/vuln/detail/CVE-2022-1737), [CVE-2022-3752](https://nvd.nist.gov/vuln/detail/CVE-2022-3752), [CVE-2022-43604](https://nvd.nist.gov/vuln/detail/CVE-2022-43604), [CVE-2022-43605](https://nvd.nist.gov/vuln/detail/CVE-2022-43605), [CVE-2022-43606](https://nvd.nist.gov/vuln/detail/CVE-2022-43606) |
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


## FINS
| Protocol | FINS |
|---|---|
| Name | FINS |
| Alias | OMRON |
| Description | Omron's industrial communication protocol for automation systems |
| Port | 9600/udp |
| Nmap script(s) | [omrontcp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omrontcp-info.nse), [omronudp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omronudp-info.nse) |
| Wireshark dissector | [packet-omron-fins.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-omron-fins.c) |



## GE-SRTP
| Protocol | GE-SRTP |
|---|---|
| Name | GE-SRTP |
| Description | General Electric's protocol for communication between GE devices and SCADA |
| Port | 18245/tcp |



## HART-IP
| Protocol | HART-IP |
|---|---|
| Name | HART-IP |
| Alias | HART |
| Description | IP-based communication protocol for HART (ICS) data transmission |
| Wireshark dissector | [packet-hartip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hartip.c) |
| Example Pcap(s) | [ICS-pcap HART-IP](https://github.com/automayt/ICS-pcap/tree/master/HART%20IP/hart_ip) |



## HL7
| Protocol | HL7 |
|---|---|
| Name | HL7 |
| Description | Standard for healthcare data exchange and interoperability |
| Wireshark dissector | [packet-hl7.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hl7.c) |



## IEC-60870-5-104
| Protocol | IEC-60870-5-104 |
|---|---|
| Name | IEC-60870-5-104 |
| Alias | IEC-104 |
| Description | Grid communication protocol for control and monitoring |
| Port | 2404/tcp |
| Access | Paid |
| Specifications | [IEC-60870-5-104 Specification](https://webstore.iec.ch/publication/25035) |
| Nmap script(s) | [iec-identify.nse](https://nmap.org/nsedoc/scripts/iec-identify.html) |
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
| Description | Protocol for home and building automation systems |
| Keywords | BMS, BAS, Building |
| Port | 3671/udp |
| Access | Free |
| Specifications | [KNXnet/IP Specifications](https://my.knx.org/en/shop/knx-specifications) |
| Security | Optional, Security extensions available |
| Nmap script(s) | [knx-gateway-discover.nse](https://nmap.org/nsedoc/scripts/knx-gateway-discover.html) |
| Wireshark dissector | [packet-knxip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-knxip.c) |
| Scapy layer | [knx.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/knx.py) |
| Related CVE | [CVE-2015-8299](https://nvd.nist.gov/vuln/detail/CVE-2015-8299), [CVE-2021-37740](https://nvd.nist.gov/vuln/detail/CVE-2021-37740) |
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
| Description | Widely used industrial communication protocol |
| Port | 502/tcp |
| Specifications | [Modbus TCP Specification](https://modbus.org/specs.php) |
| Nmap script(s) | [modbus-discover.nse](https://nmap.org/nsedoc/scripts/modbus-discover.html), [modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) |
| Wireshark dissector | [packet-mbtcp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-mbtcp.c) |
| Scapy layer | [modbus.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/modbus.py) |
| Example Pcap(s) | [ICS-pcap Modbus](https://github.com/automayt/ICS-pcap/tree/master/MODBUS) |
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
| Nmap script(s) | [fox-info.nse](https://nmap.org/nsedoc/scripts/fox-info.html) |
### Tools
- [foxdissector](https://github.com/MartinoTommasini/foxdissector) - Wireshark dissector for the Niagara Fox protocol in Lua


## OPC-DA
| Protocol | OPC-DA |
|---|---|
| Name | OPC-DA |
| Alias | OPCDA |
| Description | Legacy protocol for real-time data exchange in industrial systems |
| Scapy layer | [opc_da.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/opc_da.py) |
### Papers
- [Exploring the OPC attack surface](https://claroty.com/team82/research/white-papers/exploring-the-opc-attack-surface) - Claroty Team82 (2021)


## OPC-UA
| Protocol | OPC-UA |
|---|---|
| Name | OPC-UA |
| Alias | OPCUA |
| Description | Open communication standard for industrial automation and control |
| Port | 4840/tcp, 4840/udp, 4843/tcp (TLS) |
| Wireshark dissector | [OPC-UA Plugin](https://github.com/wireshark/wireshark/tree/master/plugins/epan/opcua) |
| Related CVE | [CVE-2019-13542](https://nvd.nist.gov/vuln/detail/CVE-2019-13542) |
### Articles
- [OPC UA Deep Dive (Part 1): History of the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-history-of-the-opc-ua-protocol) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 2): What is OPC UA?](https://claroty.com/team82/research/opc-deep-dive-part-2-what-is-opc-ua) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 3): Exploring the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-part-3-exploring-the-opc-ua-protocol) - Claroty Team82 (2023)
- [Practical example of fuzzing OPC UA applications](https://ics-cert.kaspersky.com/publications/reports/2020/10/19/practical-example-of-fuzzing-opc-ua-applications/) - Kaspersky ICS-CERT (2020)
### Papers
- [Exploring the OPC attack surface](https://claroty.com/team82/research/white-papers/exploring-the-opc-attack-surface) - Claroty Team82 (2021)
### Tools
- [python-opcua](https://github.com/FreeOpcUa/python-opcua) - OPC UA Client and Server in Python


## PC-WORX
| Protocol | PC-WORX |
|---|---|
| Name | PC-WORX |
| Description | Software suite with proprietary protocol for Phoenix Contact PLCs |
| Keywords | Phoenix Contact |
| Port | 1962/tcp |
| Nmap script(s) | [pcworx-info.nse](https://github.com/digitalbond/Redpoint/blob/master/pcworx-info.nse) |



## POWERLINK
| Protocol | POWERLINK |
|---|---|
| Name | POWERLINK |
| Alias | Ethernet PowerLink, EPL |
| Description | Real-time Ethernet protocol for industrial automation and control |
| Port | Ethernet |
| Wireshark dissector | [packet-epl.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-epl.c) |
### Articles
- [Quick Start - POWERLINK on Raspberry Pi2](https://www.kalycito.com/quick-start-powerlink-on-raspberry-pi2/) - Kalycito (2018)
### Tools
- [openCONFIGURATOR](https://sourceforge.net/projects/openconf/) - Open-source POWERLINK network configuration toolkit
- [openPOWERLINK](https://openpowerlink.sourceforge.net/web/) - Open-source POWERLINK protocol stack
- [openPOWERLINK_V2](https://github.com/OpenAutomationTechnologies/openPOWERLINK_V2) - GitHub page to openPOWERLINK protocol stack release 2


## ProConOs
| Protocol | ProConOs |
|---|---|
| Name | ProConOs |
| Description | Real-time operating system with proprietary protocol for industrial automation and control |
| Port | 20547/tcp |
| Nmap script(s) | [proconos-info.nse](https://github.com/digitalbond/Redpoint/blob/master/proconos-info.nse) |



## Profinet-DCP
| Protocol | Profinet-DCP |
|---|---|
| Name | Profinet-DCP |
| Alias | PNDCP |
| Description | Device identification, configuration, and network management protocol |
| Port | Ethernet |
| Scapy layer | [pnio_dcp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio_dcp.py) |



## Profinet-IO
| Protocol | Profinet-IO |
|---|---|
| Name | Profinet-IO |
| Alias | PNIO |
| Description | Real-time communication between controllers and I/O devices |
| Scapy layer | [pnio.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio.py) |



## S-Bus
| Protocol | S-Bus |
|---|---|
| Name | S-Bus |
| Alias | Ether-S-Bus, SAIA S-Bus |
| Description | SAIA's communication protocol for building automation |
| Keywords | SAIA |
| Access | Free |
| Wireshark dissector | [packet-sbus.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sbus.c) |
| Example Pcap(s) | [ICS-pcap Ether-S-Bus](https://github.com/automayt/ICS-pcap/tree/master/ETHERSBUS/sbus) |



## S7comm
| Protocol | S7comm |
|---|---|
| Name | S7comm |
| Alias | S7 |
| Description | Communication protocol for Siemens S7 PLCs |
| Port | 102/tcp |
| Nmap script(s) | [s7-info.nse](https://nmap.org/nsedoc/scripts/s7-info.html), [s7-enumerate.nse](https://github.com/digitalbond/Redpoint/blob/master/s7-enumerate.nse) |
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
| Description | Schneider Electric's proprietary protocol for communication systems |
| Nmap script(s) | [modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) |
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
