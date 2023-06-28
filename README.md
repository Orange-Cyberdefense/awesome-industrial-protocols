# Awesome Industrial Protocols

Offensive security-oriented list of industrial network protocols resources.

![Awesome Industrial Protocols](srcs/out/templates/logo-awesome-industrial-protocols.png)

In this repository:
* You are currently viewing the **Awesome Industrial Protocols** page.
* Detailed pages for protocols are available in `protocols`.
* All data is stored in MongoDB databases in `db`.
* **Turn/IP** (in `srcs`) is a handy tool to manipulate this data and simplify
the research and test process on industrial protocols.

> All unreviewed AI-generated data is marked with `*`.

## Contents

- [BACnet/IP](#bacnetip)
- [CAN](#can)
- [CC-Link](#cclink)
- [CSPv4](#cspv4)
- [DF1](#df1)
- [DICOM](#dicom)
- [DNP3](#dnp3)
- [Ether-S-I/O](#ethersio)
- [EtherCAT](#ethercat)
- [Ethernet/IP](#ethernetip)
- [FF-HSE](#ffhse)
- [FINS](#fins)
- [FL-net](#flnet)
- [GE-SRTP](#gesrtp)
- [HART-IP](#hartip)
- [HL7](#hl7)
- [ICCP](#iccp)
- [IEC-60870-5-104](#iec608705104)
- [IEC-61850](#iec61850)
- [IEEE-C37.118](#ieeec37118)
- [ISA100.11a](#isa10011a)
- [KNXnet/IP](#knxnetip)
- [LoRaWAN](#lorawan)
- [M-Bus](#mbus)
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
- [SERCOS-III](#sercosiii)
- [SLMP](#slmp)
- [TriStation](#tristation)
- [TSAA](#tsaa)
- [UMAS](#umas)
- [ZigBee](#zigbee)



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
| Detailed page | [bacnetip.md](protocols/bacnetip.md) |
### Articles
- [BACnet CVE-2019-12480](https://1modm.github.io/CVE-2019-12480.html) - On M's blog (2019)
### Conferences
- [(in)Security in Building Automation: How to Create Dark Buildings with Light Speed](https://www.youtube.com/watch?v=PyOhwYgpGfM) - Thomas Brandstetter @ Black Hat USA (2017)
- [HVACking Understand the Delta Between Security and Reality](https://www.youtube.com/watch?v=uJP061PUxgY) - Douglas McKee & Mark Bereza @ DEF CON 27 (2019)
- [InSecurity in Building Automation](https://www.youtube.com/watch?v=G9ESeUWfYbs) - Thomas Brandsetter @ DEF CON 25 ICS Village (2017)
- [Mixing industrial protocols with web application security](https://www.youtube.com/watch?v=TFkm0EN3Azk) - Bertin Bervis @ DEF CON 27 IoT Village (2019)
- [Owning a Building: Exploiting Access Control and Facility Management Systems](https://www.youtube.com/watch?v=wvO3puWSGgQ) - Billy Rios @ Black Hat Asia (2014)
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
| Detailed page | [can.md](protocols/can.md) |
### Conferences
- [(Pen)Testing Vehicles with CANToolz](https://www.youtube.com/watch?v=-p47IYz-H-k) - Alexey Sintsov @ Black Hat Europe (2016)
- [All Aboard the CAN Bus or Motorcycle](https://www.youtube.com/watch?v=YSApvBDIVCM) - Derrick @ DEF CON Safe Mode Car Hacking Village (2020)
- [CANSPY: Auditing CAN Devices](https://www.youtube.com/watch?v=vTsdxNGS_xc) - Jonathan Christofer Demay, Arnaud Lebrun @ DEF CON 24 (2016)
- [Cantact: An Open Tool for Automative Exploitation](https://www.youtube.com/watch?v=HzDW8ptMkDk) - Eric Evenchick @ Black Hat Asia (2016)
- [canTot A CAN Bus Hacking Framework](https://www.youtube.com/watch?v=OBC0v5KDcJg) - Jay Turla @ DEF CON 30 Car Hacking Village (2022)
- [Deep Learning on CAN BUS](https://www.youtube.com/watch?v=1QSo5sOfXtI) - Jun Li @ DEF CON 24 Car Hacking Village (2016)
- [Free-Fall: Hacking Tesla from Wireless to CAN Bus](https://www.youtube.com/watch?v=0w8J9bmCI54) - Ling Liu, Sen Nie & Yuefeng Du @ Black Hat USA (2017)
- [Fuzzing CAN / CAN FD ECU's and Network](https://www.youtube.com/watch?v=IMZ8DD4lTAY) - Samir Bhagwat @ DEF CON 29 Car Hacking Village (2021)
- [Hopping on the CAN Bus](https://www.youtube.com/watch?v=U1yecKUmnFo) - Eric Evenchick @ Black Hat USA (2015)
- [Patrick Kiley - CAN Bus in Aviation Investigating CAN Bus in Avionics - DEF CON 27 Aviation Village](https://www.youtube.com/watch?v=bydy7lbFyFU) - @ DEF CON (2019)
- [Self-Driving and Connected Cars: Fooling Sensors and Tracking Drivers](https://www.youtube.com/watch?v=C29UGFsIWVI) - Jonathan Petit @ Black Hat Europe (2015)


## CC-Link
| Protocol | CC-Link |
|---|---|
| Name | CC-Link |
| Alias | CSP+ |
| Description | CC-Link IE communication profile for industrial automation networks |
| Keywords | Mitsubishi, CC-Link, CC-Link IE, CLPA |
| Access | Free |
| Specifications | [CSP+ specification](https://www.cc-link.org/en/downloads/index.html) |
| Detailed page | [cclink.md](protocols/cclink.md) |



## CSPv4
| Protocol | CSPv4 |
|---|---|
| Name | CSPv4 |
| Alias | AB CSPv4, AB/Ethernet |
| Description | Allen-Bradley's protocol for industrial Ethernet communication |
| Keywords | Allen-Bradley |
| Port | 2222/tcp |
| Nmap script(s) | [cspv4-info.nse](https://github.com/digitalbond/Redpoint/blob/master/cspv4-info.nse) |
| Detailed page | [cspv4.md](protocols/cspv4.md) |



## DF1
| Protocol | DF1 |
|---|---|
| Name | DF1 |
| Alias | DF-1 |
| Description | Allen-Bradley serial communication protocol for industrial automation devices |
| Access | Free |
| Specifications | [DF1 specification](https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/1770-rm516_-en-p.pdf) |
| Detailed page | [df1.md](protocols/df1.md) |
### Tools
- [abdf1](https://sourceforge.net/projects/abdf1/) - AB DF1 Protocol RS232 driver for Micrologix, SLC500, PLC 5
- [Df1](https://github.com/leicht/Df1) - Df1 protocol for Allen-Bradley PLC


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
| Detailed page | [dicom.md](protocols/dicom.md) |
### Conferences
- [Healthscare – An Insider's Biopsy of Healthcare Application Security](https://www.youtube.com/watch?v=33dQhsIcp7U) - Seth Fogie @ Black Hat USA (2020)
### Tools
- [DCMTK](https://dcmtk.org/en/) - DICOM ToolKit
- [dicom-server](https://github.com/microsoft/dicom-server) - Microsoft's OSS Implementation of DICOMweb standard
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
| Detailed page | [dnp3.md](protocols/dnp3.md) |
### Conferences
- [NSM 101 for ICS](https://www.youtube.com/watch?v=H6AWRziR028) - Chris Sistrunk @ DEF CON 23 101 Track (2015)
- [SCADA Protocol Implementation Considerations | SANS ICS Concepts](https://www.youtube.com/watch?v=Fi7JhLm4vjY) - @ SANS ICS Security (2022)
- [Sniffing SCADA](https://www.youtube.com/watch?v=4vPptUmyv4U) - Karl Koscher @ DEF CON 23 Packet Capture Village (2015)
- [Unraveling SCADA Protocols Using Sulley Fuzzer](https://www.youtube.com/watch?v=UUta_Ord8GI) - Ganesh Devarajan @ DEF CON 15 (2014)
### Tools
- [dnp-info](https://github.com/sjhilt/Nmap-NSEs/blob/master/dnp3-info.nse) - Nmap discovery script for DNP3
- [dnp3-simulator](https://github.com/dnp3/dnp3-simulator) - .NET DNP3 simulator with GUI 
- [FreyrSCADA DNP3](https://github.com/FreyrSCADA/DNP3) - DNP3 Protocol - Outstation Server and Client Master Simulator
- [opendnp3](https://github.com/dnp3/opendnp3) - DNP3 (IEEE-1815) protocol stack. Modern C++ with bindings for .NET and Java
- [Step Function I/O DNP3](https://github.com/stepfunc/dnp3) - Rust implementation of DNP3 (IEEE 1815) with idiomatic bindings for C, .NET, C++, and Java


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
| Detailed page | [ethersio.md](protocols/ethersio.md) |



## EtherCAT
| Protocol | EtherCAT |
|---|---|
| Name | EtherCAT |
| Alias | ECATF, ECAT |
| Description | Real-time industrial Ethernet communication protocol for automation systems |
| Scapy layer | [ethercat.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/ethercat.py) |
| Example Pcap(s) | [ICS-pcap EtherCAT](https://github.com/automayt/ICS-pcap/tree/master/ETHERCAT/ethercat) |
| Detailed page | [ethercat.md](protocols/ethercat.md) |



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
| Detailed page | [ethernetip.md](protocols/ethernetip.md) |
### Articles
- [Fuzzing and PR’ing: How We Found Bugs in a Popular Third-Party EtherNet/IP Protocol Stack](https://claroty.com/team82/research/opener-enip-stack-vulnerabilities) - Sharon Brizinov, Tal Keren (Claroty, 2021)
### Conferences
- [Hunting EtherNet/IP Protocol Stacks](https://www.youtube.com/watch?v=0jftEYDo0ao) - Sharon Brizinov @ SANS ICS Security Summit 2022
### Tools
- [CIPster](https://github.com/liftoff-sr/CIPster) - Ethernet/IP (Common Industrial Protocol) stack in C++
- [cpppo](https://github.com/pjkundert/cpppo) - Communications Protocol Python Parser and Originator -- EtherNet/IP CIP
- [enip-stack-detector](https://github.com/claroty/enip-stack-detector) - EtherNet/IP & CIP Stack Detector
- [OpENer](https://github.com/EIPStackGroup/OpENer) - EtherNet/IP stack for I/O adapter devices
- [pycomm3](https://github.com/ottowayi/pycomm3) - A Python Ethernet/IP library for communicating with Allen-Bradley PLCs
- [scapy-cip-enip](https://github.com/scy-phy/scapy-cip-enip) - Ethernet/IP dissectors for Scapy


## FF-HSE
| Protocol | FF-HSE |
|---|---|
| Name | FF-HSE |
| Alias | Foundation Fieldbus HSE, FF |
| Description | Ethernet-based communication for industrial process automation devices |
| Port | 1089/tcp, 1090/tcp, 1091/tcp, 1089/udp, 1090/udp, 1091/udp |
| Wireshark dissector | [packet-ff.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-ff.c) |
| Detailed page | [ffhse.md](protocols/ffhse.md) |



## FINS
| Protocol | FINS |
|---|---|
| Name | FINS |
| Alias | OMRON |
| Description | Omron's industrial communication protocol for automation systems |
| Port | 9600/udp |
| Nmap script(s) | [omrontcp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omrontcp-info.nse), [omronudp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omronudp-info.nse) |
| Wireshark dissector | [packet-omron-fins.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-omron-fins.c) |
| Detailed page | [fins.md](protocols/fins.md) |
### Conferences
- [DEF CON 30 -  Jimmy Wylie - Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - @ DEF CON (2022)


## FL-net
| Protocol | FL-net |
|---|---|
| Name | FL-net |
| Alias | Factory LAN, OPCN-2 |
| Description | Japan Electrical Manufacturers' Association's industrial-use open network |
| Keywords | JEMA |
| Access | Free |
| Specifications | [FL-net specification](https://www.jema-net.or.jp/English/businessfields/standarization/opcn/standard/) |
| Detailed page | [flnet.md](protocols/flnet.md) |



## GE-SRTP
| Protocol | GE-SRTP |
|---|---|
| Name | GE-SRTP |
| Description | General Electric's protocol for communication between GE devices and SCADA |
| Port | 18245/tcp |
| Detailed page | [gesrtp.md](protocols/gesrtp.md) |



## HART-IP
| Protocol | HART-IP |
|---|---|
| Name | HART-IP |
| Alias | HART, WirelessHART |
| Description | IP-based communication protocol for HART (ICS) data transmission |
| Wireshark dissector | [packet-hartip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hartip.c) |
| Example Pcap(s) | [ICS-pcap HART-IP](https://github.com/automayt/ICS-pcap/tree/master/HART%20IP/hart_ip) |
| Detailed page | [hartip.md](protocols/hartip.md) |
### Conferences
- [Dissecting Industrial Wireless Implementations](https://www.youtube.com/watch?v=I-TCfl0Jm2M) - Blake Johnson @ DEF CON 25 ICS Village (2017)
- [DTM Components: Shadow Keys to the ICS Kingdom](https://www.youtube.com/watch?v=VeMgbC0a-u8) - Alexander Bolshev and Gleb Cherbov @ Black Hat Europe (2014)
- [ICSCorsair: How I Will PWN Your ERP Through 4-20 mA Current Loop](https://www.youtube.com/watch?v=T9tahQImuWI) - Alexander Bolshev and Gleb Cherbov @ Black Hat USA (2014)
- [It WISNt Me Attacking Industrial Wireless Mesh Networks](https://www.youtube.com/watch?v=-WfP2VVhTt0) - Paternotte and van Ommeren @ DEF CON 25 (2018)


## HL7
| Protocol | HL7 |
|---|---|
| Name | HL7 |
| Description | Standard for healthcare data exchange and interoperability |
| Wireshark dissector | [packet-hl7.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hl7.c) |
| Detailed page | [hl7.md](protocols/hl7.md) |
### Conferences
- [DEF CON 29 Biohacking Village - Alissa Knight, Mitch Parker - Playing with FHIR](https://www.youtube.com/watch?v=wrNyd60XPMg) - @ DEF CON (2021)
- [Healthscare – An Insider's Biopsy of Healthcare Application Security](https://www.youtube.com/watch?v=33dQhsIcp7U) - Seth Fogie @ Black Hat USA (2020)
- [Pestilential Protocol: How Unsecure HL7 Messages Threaten Patient Lives](https://www.youtube.com/watch?v=66x3vfac8rA) - @ Black Hat (2020)
- [Understanding HL7 2.X Standards, Pen Testing, and Defending HL7 2.X Messages](https://www.youtube.com/watch?v=MR7cH44fjrc) - @ Black Hat (2016)


## ICCP
| Protocol | ICCP |
|---|---|
| Name | ICCP |
| Alias | IEC 60870-6, TASE.2 |
| Description | Real-time data exchange between power system control centers |
| Keywords | Power |
| Port | 102/tcp |
| Access | Paid |
| Specifications | [ICCP (TASE.2) specification](https://webstore.iec.ch/publication/3760) |
| Detailed page | [iccp.md](protocols/iccp.md) |
### Conferences
- [Unraveling SCADA Protocols Using Sulley Fuzzer](https://www.youtube.com/watch?v=UUta_Ord8GI) - Ganesh Devarajan @ DEF CON 15 (2014)


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
| Detailed page | [iec608705104.md](protocols/iec608705104.md) |
### Conferences
- [Industroyer/Crashoverride: Zero Things Cool About a Threat Group Targeting the Power Grid](https://www.youtube.com/watch?v=TH17hSH1PGQ) - @ Black Hat (2020)
- [Industroyer2: Sandworm&#39;s Cyberwarfare Targets Ukraine&#39;s Power Grid Again](https://www.youtube.com/watch?v=xC9iM5wVedQ) - @ Black Hat (2022)
### Papers
- [Description and analysis of IEC 104 Protocol](https://www.fit.vut.cz/research/publication/11570/.en) - Technical report by Petr Matousek @ Faculty of Information Techology, Czech Republic (2017)
### Tools
- [FreyrSCADA IEC-60870-5-104](https://github.com/FreyrSCADA/IEC-60870-5-104) - IEC 60870-5-104 Protocol - RTU Server and Master Client Simulator
- [lib60870](https://github.com/mz-automation/lib60870) - Implementation of the IEC 60870-5-101/104 protocol


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
| Detailed page | [iec61850.md](protocols/iec61850.md) |
### Tools
- [libiec61850](https://github.com/mz-automation/libiec61850) - Open-source library for the IEC 61850 protocols


## IEEE-C37.118
| Protocol | IEEE-C37.118 |
|---|---|
| Name | IEEE-C37.118 |
| Alias | C37.118, Synchrophasor, Synphasor |
| Description | Standard for synchrophasor data exchange in power systems |
| Keywords | Power |
| Wireshark dissector | [packet-synphasor.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-synphasor.c) |
| Detailed page | [ieeec37118.md](protocols/ieeec37118.md) |
### Tools
- [OpenPDC](https://github.com/GridProtectionAlliance/openPDC) - Open Source Phasor Data Concentrator
- [PyMU](https://github.com/iti/pymu) - Library based on the C37.118.2-2011 standard used for accessing PMU data in real-time


## ISA100.11a
| Protocol | ISA100.11a |
|---|---|
| Name | ISA100.11a |
| Description | Wireless standard for industrial automation and control systems |
| Detailed page | [isa10011a.md](protocols/isa10011a.md) |
### Conferences
- [It WISNt Me Attacking Industrial Wireless Mesh Networks](https://www.youtube.com/watch?v=-WfP2VVhTt0) - Paternotte and van Ommeren @ DEF CON 25 (2018)


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
| Detailed page | [knxnetip.md](protocols/knxnetip.md) |
### Documentations
- [knx.org](https://www.knx.org/knx-en/for-professionals/index.php) - KNX official website
### Conferences
- [(in)Security in Building Automation: How to Create Dark Buildings with Light Speed](https://www.youtube.com/watch?v=PyOhwYgpGfM) - Thomas Brandstetter @ Black Hat USA (2017)
- [InSecurity in Building Automation](https://www.youtube.com/watch?v=G9ESeUWfYbs) - Thomas Brandsetter @ DEF CON 25 ICS Village (2017)
- [Learn how to control every room at a luxury hotel remotely](https://www.youtube.com/watch?v=RX-O4XuCW1Y) - Jesus Molina @ DEF CON 22 (2015)
- [Learn How to Control Every Room at a Luxury Hotel Remotely](https://www.youtube.com/watch?v=xomtYrcTSgU) - Jesus Nomeames @ Black Hat USA (2014)
- [Sneak into buildings with KNXnetIP](https://www.youtube.com/watch?v=QofeTV39kQE) - Claire Vacherot @ DEF CON 29 (2020)
### Papers
- [An Overview of Wireless IoT Protocol Security in the Smart Home Domain](https://arxiv.org/abs/1801.07090) - Stefan Marksteiner, Víctor Juan Expósito Jiménez, Heribert Vallant, Herwig Zeiner (2018)
### Tools
- [BOF](https://github.com/Orange-Cyberdefense/bof) - Testing framework for industrial protocols
- [ETS](https://www.knx.org/knx-en/for-professionals/software/ets-professional/) - Engineering Tool Software for KNXnet/IP (ETS Demo is free)
- [KNX Virtual](https://www.knx.org/knx-en/for-professionals/get-started/knx-virtual/index.php) - Windows-based application simulating a KNX installation
- [knxd](https://github.com/knxd/knxd) - KNXd service
- [KNXmap](https://github.com/takeshixx/knxmap) - KNXnet/IP scanning and auditing tool
- [XKNX](https://github.com/XKNX/xknx) - A KNX library written in Python


## LoRaWAN
| Protocol | LoRaWAN |
|---|---|
| Name | LoRaWAN |
| Alias | LoRa |
| Description | Long-range IoT communication protocol with low power requirements |
| Keywords | Wireless |
| Access | Free |
| Specifications | [LoRaWAN specification](https://lora-alliance.org/resource_hub/lorawan-specification-v1-1/) |
| Wireshark dissector | [packet-lorawan.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-lorawan.c) |
| Detailed page | [lorawan.md](protocols/lorawan.md) |
### Conferences
- [DEF CON 24 Wireless Village - Matt Knight - Reversting LoRa Deconstructing a Next Gen Proprietary LP](https://www.youtube.com/watch?v=KEjlkZA2olE) - @ DEF CON (2016)
- [DEF CON 26 - Zeng and Panel -  Lora Smart Water Meter Security Analysis](https://www.youtube.com/watch?v=b7ekygjC3so) - @ DEF CON (2018)
- [DEF CON 26 WIRELESS VILLAGE - wasabi - Can you hear me now DEF CON](https://www.youtube.com/watch?v=lhHM6TX2RrI) - @ DEF CON (2018)
- [Outsmarting the Smart City](https://www.youtube.com/watch?v=Opjb5hPlxtY) - @ Black Hat (2020)
### Tools
- [ChirpOTLE](https://github.com/seemoo-lab/chirpotle) - LoRaWAN Security Evaluation Framework
- [ChirpStack Network Server](https://github.com/brocaar/chirpstack-network-server) - Open-source LoRaWAN network-server
- [lorawan-server](https://github.com/gotthardp/lorawan-server) - Compact server for private LoRaWAN networks
- [lorawan-stack](https://github.com/TheThingsNetwork/lorawan-stack) - Open Source LoRaWAN Network Server


## M-Bus
| Protocol | M-Bus |
|---|---|
| Name | M-Bus |
| Alias | Meter-Bus, EN13757 |
| Description | Communication protocol for utility metering devices |
| Access | The old specification is free, not the current one |
| Specifications | [M-Bus specification](https://m-bus.com/documentation) |
| Detailed page | [mbus.md](protocols/mbus.md) |



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
| Detailed page | [modbus.md](protocols/modbus.md) |
### Tools
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS
- [PyModbus](https://github.com/pymodbus-dev/pymodbus) - A full modbus protocol written in python


## Niagara Fox
| Protocol | Niagara Fox |
|---|---|
| Name | Niagara Fox |
| Alias | Fox |
| Description | Communication protocol used by Tridium Niagara devices |
| Keywords | Tridium |
| Port | 1911/tcp, 3011/tcp, 4911/tcp, 5011/tcp |
| Nmap script(s) | [fox-info.nse](https://nmap.org/nsedoc/scripts/fox-info.html) |
| Detailed page | [niagarafox.md](protocols/niagarafox.md) |
### Tools
- [foxdissector](https://github.com/MartinoTommasini/foxdissector) - Wireshark dissector for the Niagara Fox protocol in Lua


## OPC-DA
| Protocol | OPC-DA |
|---|---|
| Name | OPC-DA |
| Alias | OPCDA |
| Description | Legacy protocol for real-time data exchange in industrial systems |
| Scapy layer | [opc_da.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/opc_da.py) |
| Detailed page | [opcda.md](protocols/opcda.md) |
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
| Detailed page | [opcua.md](protocols/opcua.md) |
### Articles
- [OPC UA Deep Dive (Part 1): History of the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-history-of-the-opc-ua-protocol) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 2): What is OPC UA?](https://claroty.com/team82/research/opc-deep-dive-part-2-what-is-opc-ua) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 3): Exploring the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-part-3-exploring-the-opc-ua-protocol) - Claroty Team82 (2023)
- [Practical example of fuzzing OPC UA applications](https://ics-cert.kaspersky.com/publications/reports/2020/10/19/practical-example-of-fuzzing-opc-ua-applications/) - Kaspersky ICS-CERT (2020)
### Conferences
- [Resting on Feet of Clay: Securely Bootstrapping OPC UA Deployments](https://www.youtube.com/watch?v=8RUVB9eeITQ) - Alessandro Erba & Nils Ole Tippenhauer @ Black Hat Europe (2021)
### Papers
- [Exploring the OPC attack surface](https://claroty.com/team82/research/white-papers/exploring-the-opc-attack-surface) - Claroty Team82 (2021)
- [Security Analysis of Vendor Implementations of the OPC UA Protocol for Industrial Control Systems](https://arxiv.org/abs/2104.06051) - Alessandro Erba, Anne Müller, Nils Ole Tippenhauer (2021)
### Tools
- [freeopcua](https://github.com/FreeOpcUa/freeopcua) - Open Source C++ OPC-UA Server and Client Library
- [opcua-client-gui](https://github.com/FreeOpcUa/opcua-client-gui) - Simple OPC-UA GUI client
- [python-opcua](https://github.com/FreeOpcUa/python-opcua) - OPC UA Client and Server in Python
- [UA-.NETStandard](https://github.com/OPCFoundation/UA-.NETStandard) - Official OPC UA .NET Standard Stack from the OPC Foundation


## PC-WORX
| Protocol | PC-WORX |
|---|---|
| Name | PC-WORX |
| Description | Software suite with proprietary protocol for Phoenix Contact PLCs |
| Keywords | Phoenix Contact |
| Port | 1962/tcp |
| Nmap script(s) | [pcworx-info.nse](https://github.com/digitalbond/Redpoint/blob/master/pcworx-info.nse) |
| Detailed page | [pcworx.md](protocols/pcworx.md) |



## POWERLINK
| Protocol | POWERLINK |
|---|---|
| Name | POWERLINK |
| Alias | Ethernet PowerLink, EPL |
| Description | Real-time Ethernet protocol for industrial automation and control |
| Port | Ethernet |
| Wireshark dissector | [packet-epl.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-epl.c) |
| Detailed page | [powerlink.md](protocols/powerlink.md) |
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
| Detailed page | [proconos.md](protocols/proconos.md) |



## Profinet-DCP
| Protocol | Profinet-DCP |
|---|---|
| Name | Profinet-DCP |
| Alias | PNDCP |
| Description | Device identification, configuration, and network management protocol |
| Port | Ethernet |
| Scapy layer | [pnio_dcp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio_dcp.py) |
| Detailed page | [profinetdcp.md](protocols/profinetdcp.md) |



## Profinet-IO
| Protocol | Profinet-IO |
|---|---|
| Name | Profinet-IO |
| Alias | PNIO |
| Description | Real-time communication between controllers and I/O devices |
| Scapy layer | [pnio.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio.py) |
| Detailed page | [profinetio.md](protocols/profinetio.md) |



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
| Detailed page | [sbus.md](protocols/sbus.md) |



## S7comm
| Protocol | S7comm |
|---|---|
| Name | S7comm |
| Alias | S7, S7commPlus |
| Description | Communication protocol for Siemens S7 PLCs |
| Port | 102/tcp |
| Nmap script(s) | [s7-info.nse](https://nmap.org/nsedoc/scripts/s7-info.html), [s7-enumerate.nse](https://github.com/digitalbond/Redpoint/blob/master/s7-enumerate.nse) |
| Wireshark dissector | [packet-s7comm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-s7comm.c) |
| Example Pcap(s) | [ICS-pcap S7](https://github.com/automayt/ICS-pcap/tree/master/S7) |
| Detailed page | [s7comm.md](protocols/s7comm.md) |
### Articles
- [The Siemens S7 Communication - Part 1 General Structure](http://gmiru.com/article/s7comm/) - On GyM's Personal Blog (2016)
- [The Siemens S7 Communication - Part 2 Job Requests and Ack Data](http://gmiru.com/article/s7comm-part2/) - On GyM's Personal Blog (2017)
### Conferences
- [Fuzzing and Breaking Security Functions of SIMATIC PLCs](https://www.youtube.com/watch?v=XeSSuWR5PaU) - Gao Jian @ Black Hat Europe (2022)
- [PLC-Blaster: A worm Living Solely In The PLC](https://www.youtube.com/watch?v=NNAKaAKRUow) - Ralf Spenneberg, Maik Brueggemann & Hendrik Schwartke @ Black Hat Asia (2016)
- [Rogue7: Rogue Engineering-Station Attacks on S7 Simatic PLCs](https://www.youtube.com/watch?v=dHxsctLBUEI) - Uriel Malin, Sara Bitan, Avishai Wool and Eli Biham @ Black Hat USA (2019)
- [The spear to break the security wall of S7CommPlus](https://www.youtube.com/watch?v=93lyRgZYxKw) - Cheng Lei @ DEF CON 25 (2017)
### Tools
- [python-snap7](https://github.com/gijzelaerr/python-snap7) - A Python wrapper for the snap7 PLC communication library
- [s7scan](https://github.com/klsecservices/s7scan) - Scan networks to gather basic information about Siemens PLCs
- [Snap7](https://snap7.sourceforge.net/) - Step7 Open Source Ethernet Communication Suite


## SERCOS-III
| Protocol | SERCOS-III |
|---|---|
| Name | SERCOS-III |
| Alias | SERCOS |
| Description | IEC standard universal bus for Ethernet-based real-time communication |
| Wireshark dissector | [packet-sercosiii.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sercosiii.c) |
| Detailed page | [sercosiii.md](protocols/sercosiii.md) |



## SLMP
| Protocol | SLMP |
|---|---|
| Name | SLMP |
| Alias | Seamless Message Protocol |
| Description | CC-Link's messaging protocol for industrial automation communication |
| Keywords | Mitsubishi, CC-Link, CLPA |
| Access | Free |
| Specifications | [SLMP specification](https://www.cc-link.org/en/downloads/nonmembers/form.html) |
| Detailed page | [slmp.md](protocols/slmp.md) |
### Tools
- [PySLMPClient](https://github.com/masahase0117/PySLMPClient) - Python client for SLMP


## TriStation
| Protocol | TriStation |
|---|---|
| Name | TriStation |
| Alias | Triconex TriStation |
| Description | Triconex's proprietary protocol for safety system communication |
| Keywords | Triconex, TRITON |
| Wireshark dissector | [TriStation.lua](https://github.com/NozomiNetworks/tricotools/blob/master/TriStation.lua) |
| Detailed page | [tristation.md](protocols/tristation.md) |
### Articles
- [Attackers Deploy New ICS Attack Framework “TRITON” and Cause Operational Disruption to Critical Infrastructure](https://www.mandiant.com/resources/blog/attackers-deploy-new-ics-attack-framework-triton) - Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer @ Mandiant (2017, updated 2022)
### Conferences
- [How TRITON Disrupted Safety Systems & Changed the Threat Landscape of Industrial Control Systems](https://www.youtube.com/watch?v=Hw2HclZV2Kw) - Andrea Carcano, Marina Krotofil & Younes Dragoni @ Black Hat USA (2018)
### Tools
- [tricotools](https://github.com/NozomiNetworks/tricotools) - Triconex TriStation utilities and tools


## TSAA
| Protocol | TSAA |
|---|---|
| Name | TSAA |
| Description | Messaging protocol to read and write data to Triconex controllers |
| Keywords | Triconex |
| Detailed page | [tsaa.md](protocols/tsaa.md) |
### Documentations
- [Triconex System Access Application (TSAA) playlist](https://www.youtube.com/playlist?list=PLFf3xtcn9d46Eq8tdpTH-cviNPv8P0blU) - What Did You Learn Today (2021)


## UMAS
| Protocol | UMAS |
|---|---|
| Name | UMAS |
| Description | Schneider Electric's proprietary protocol for communication systems |
| Nmap script(s) | [modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) |
| Detailed page | [umas.md](protocols/umas.md) |
### Articles
- [The secrets of Schneider Electric’s UMAS protocol](https://ics-cert.kaspersky.com/publications/reports/2022/09/29/the-secrets-of-schneider-electrics-umas-protocol/) - Kaspersky ICS CERT (2022)
- [The Unity (UMAS) protocol (Part I)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-i.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part II)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-ii.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part III)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-iii.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part IV)](http://lirasenlared.blogspot.com/2017/08/the-unity-umas-protocol-part-iv.html) - Liras en la red (2017)
- [The Unity (UMAS) protocol (Part V)](http://lirasenlared.blogspot.com/2017/09/the-unity-umas-protocol-part-v.html) - Liras en la red (2017)
### Tools
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS


## ZigBee
| Protocol | ZigBee |
|---|---|
| Name | ZigBee |
| Alias | ZBee |
| Description | Wireless communication protocol for low-power IoT devices. |
| Wireshark dissector | [packet-zbee-nwk.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-zbee-nwk.c) |
| Scapy layer | [zigbee.py](https://github.com/secdev/scapy/blob/master/scapy/layers/zigbee.py) |
| Detailed page | [zigbee.md](protocols/zigbee.md) |
### Conferences
- [A Lightbulb Worm?](https://www.youtube.com/watch?v=R3ZVeBWNSIY) - Colin O'Flynn @ Black Hat USA (2016)
- [Dont Be Silly It's Only a Lightbulb](https://www.youtube.com/watch?v=iMxquCdAMWI) - Eyal Itkin @ DEF CON Safe Mode (2020)
- [Exploring the 802 15 4 Attack Surface](https://www.youtube.com/watch?v=sU7PlIM-nEE) - FAZ @ DEF CON 26 WIRELESS VILLAGE (2018)
- [Im A Newbie Yet I Can Hack ZigBee](https://www.youtube.com/watch?v=xgNT05l6Jlw) - Qing Yang @ DEF CON 23 (2015)
- [ZigBee Exploited The Good, The Bad, And The Ugly](https://www.youtube.com/watch?v=9xzXp-zPkjU) - Tobias Zillner & Sebastian Strobl @ Black Hat USA (2015)
### Papers
- [An Overview of Wireless IoT Protocol Security in the Smart Home Domain](https://arxiv.org/abs/1801.07090) - Stefan Marksteiner, Víctor Juan Expósito Jiménez, Heribert Vallant, Herwig Zeiner (2018)
### Tools
- [KillerBee](https://github.com/riverloopsec/killerbee) - IEEE 802.15.4/ZigBee Security Research Toolkit

> **awesome-industrial-protocols** is licensed under
[CC0](https://creativecommons.org/publicdomain/zero/1.0/). **Turn/IP** is
licensed under [GPL-v3](https://www.gnu.org/licenses/gpl-3.0.en.html).
