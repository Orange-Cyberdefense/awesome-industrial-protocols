# Awesome Industrial Protocols

Compilation of industrial network protocols resources focusing on offensive security.

![Awesome Industrial Protocols](srcs/out/templates/logo-awesome-industrial-protocols.png)

In this repository:
* You are currently viewing the **Awesome Industrial Protocols** page.
* Detailed pages for protocols are available in `protocols`.
* All data is stored in MongoDB databases in `db`.
* **Turn/IP** (in `srcs`) is a handy tool to manipulate this data, generate the
awesome list and protocol pages, and simplify the research and test process
on industrial protocols.

> Note: Sometimes it is unclear whether a name refers to a protocol, a standard,
or a complete environment, or if a protocol on a serial link can be accessed
in any way from the Ethernet link (through a dedicated implementation or a
gateway). I apologize for any confusion, and of course, I welcome any remarks
or contributions.

## Contents

- [BACnet/IP](#bacnetip)
- [CAN](#can)
- [CC-Link IE](#cc-link-ie)
- [CIP](#cip)
- [CODESYS](#codesys)
- [CSPv4](#cspv4)
- [DeviceNet](#devicenet)
- [DF1](#df1)
- [DICOM](#dicom)
- [DNP3](#dnp3)
- [Ether-S-I/O](#ether-s-io)
- [EtherCAT](#ethercat)
- [Ethernet/IP](#ethernetip)
- [ETP](#etp)
- [FF-HSE](#ff-hse)
- [FINS](#fins)
- [FL-net](#fl-net)
- [GE-SRTP](#ge-srtp)
- [HART-IP](#hart-ip)
- [HICP](#hicp)
- [HL7](#hl7)
- [ICCP](#iccp)
- [IEC-60870-5-104](#iec-60870-5-104)
- [IEC-61850](#iec-61850)
- [IEEE-C37.118](#ieee-c37118)
- [ISA100.11a](#isa10011a)
- [KNXnet/IP](#knxnetip)
- [LoRaWAN](#lorawan)
- [M-Bus](#m-bus)
- [MELSEC](#melsec)
- [Modbus](#modbus)
- [MQTT](#mqtt)
- [Niagara Fox](#niagara-fox)
- [OPC-DA](#opc-da)
- [OPC-UA](#opc-ua)
- [PC-WORX](#pc-worx)
- [PCCC](#pccc)
- [POWERLINK](#powerlink)
- [ProConOs](#proconos)
- [Profinet-DCP](#profinet-dcp)
- [Profinet-IO](#profinet-io)
- [S-Bus](#s-bus)
- [S7comm](#s7comm)
- [SECS/GEM](#secsgem)
- [SERCOS-III](#sercos-iii)
- [SLMP](#slmp)
- [TriStation](#tristation)
- [TSAA](#tsaa)
- [UMAS](#umas)
- [WITS](#wits)
- [ZigBee](#zigbee)



## BACnet/IP
| Name | BACnet/IP |
|---|---|
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
- [10 things you should know about BACnet](https://www.rtautomation.com/rtas-blog/10-things-about-bacnet/) - Blog post on RTAutomation
- [BACnet CVE-2019-12480](https://1modm.github.io/CVE-2019-12480.html) - On M's blog (2019)
- [BACnet data representation](https://www.rtautomation.com/rtas-blog/bacnet-data-representation/) - Blog post on RTAutomation
### Conferences
- [(in)Security in Building Automation: How to Create Dark Buildings with Light Speed](https://www.youtube.com/watch?v=PyOhwYgpGfM) - Thomas Brandstetter @ Black Hat USA (2017)
- [HVACking Understand the Delta Between Security and Reality](https://www.youtube.com/watch?v=uJP061PUxgY) - Douglas McKee & Mark Bereza @ DEF CON 27 (2019)
- [InSecurity in Building Automation](https://www.youtube.com/watch?v=G9ESeUWfYbs) - Thomas Brandsetter @ DEF CON 25 ICS Village (2017)
- [Mixing industrial protocols with web application security](https://www.youtube.com/watch?v=TFkm0EN3Azk) - Bertin Bervis @ DEF CON 27 IoT Village (2019)
- [Owning a Building: Exploiting Access Control and Facility Management Systems](https://www.youtube.com/watch?v=wvO3puWSGgQ) - Billy Rios @ Black Hat Asia (2014)
### Tools
- [BACnet Stack](https://github.com/bacnet-stack/bacnet-stack) - BACnet open source protocol stack


## CAN
| Name | CAN |
|---|---|
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
- [CAN Bus in Aviation Investigating CAN Bus in Avionics](https://www.youtube.com/watch?v=bydy7lbFyFU) - Patrick Kiley @ DEF CON 27 Aviation Village (2019)
- [CANSPY: Auditing CAN Devices](https://www.youtube.com/watch?v=vTsdxNGS_xc) - Jonathan Christofer Demay, Arnaud Lebrun @ DEF CON 24 (2016)
- [Cantact: An Open Tool for Automative Exploitation](https://www.youtube.com/watch?v=HzDW8ptMkDk) - Eric Evenchick @ Black Hat Asia (2016)
- [canTot A CAN Bus Hacking Framework](https://www.youtube.com/watch?v=OBC0v5KDcJg) - Jay Turla @ DEF CON 30 Car Hacking Village (2022)
- [Deep Learning on CAN BUS](https://www.youtube.com/watch?v=1QSo5sOfXtI) - Jun Li @ DEF CON 24 Car Hacking Village (2016)
- [Free-Fall: Hacking Tesla from Wireless to CAN Bus](https://www.youtube.com/watch?v=0w8J9bmCI54) - Ling Liu, Sen Nie & Yuefeng Du @ Black Hat USA (2017)
- [Fuzzing CAN / CAN FD ECU's and Network](https://www.youtube.com/watch?v=IMZ8DD4lTAY) - Samir Bhagwat @ DEF CON 29 Car Hacking Village (2021)
- [Hopping on the CAN Bus](https://www.youtube.com/watch?v=U1yecKUmnFo) - Eric Evenchick @ Black Hat USA (2015)
- [Self-Driving and Connected Cars: Fooling Sensors and Tracking Drivers](https://www.youtube.com/watch?v=C29UGFsIWVI) - Jonathan Petit @ Black Hat Europe (2015)


## CC-Link IE
| Name | CC-Link IE |
|---|---|
| Alias | CSP+, CC-Link, CC-Link IE TSN, CC-Link IE Control, CC-Link IE Field, CC-Link IE Field Basic |
| Description | Industrial Ethernet communication network developed by the CC-Link Partner Association (CLPA) |
| Keywords | Mitsubishi, CLPA |
| Access | Free |
| Specifications | [CSP+ specification](https://www.cc-link.org/en/downloads/index.html) |
| Detailed page | [cc-link-ie.md](protocols/cc-link-ie.md) |
### Documentations
- [CC-Link IE Field Network playlist](https://www.youtube.com/watch?v=h8QXlx2Xv9M&list=PL2zpUSDLjMt-J1HGOdzR1blv1z1s-eF03) - Mitsubishi Training


## CIP
| Name | CIP |
|---|---|
| Alias | Common Industrial Protocol |
| Description | ODVA's protocol suite for industrial automation communication |
| Keywords | ODVA, Ethernet/IP, DeviceNet, ControlNet, CompoNet |
| Wireshark dissector | [packet-cip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-cip.c) |
| Detailed page | [cip.md](protocols/cip.md) |
### Documentations
- [Common Industrial Protocol (CIP)](https://www.odva.org/technology-standards/key-technologies/common-industrial-protocol-cip/) - Overview on ODVA.org
- [CompoNet](https://www.odva.org/technology-standards/other-technologies/componet/) - Overview on ODVA.org
- [ControlNet](https://www.odva.org/technology-standards/other-technologies/controlnet/) - Overview on ODVA.org
- [DeviceNet](https://www.odva.org/technology-standards/key-technologies/devicenet/) - Overview on ODVA.org
- [Ethernet/IP](https://www.odva.org/technology-standards/key-technologies/ethernet-ip/) - Overview on ODVA.org
### Conferences
- [Hunting EtherNet/IP Protocol Stacks](https://www.youtube.com/watch?v=0jftEYDo0ao) - Sharon Brizinov @ SANS ICS Security Summit 2022


## CODESYS
| Name | CODESYS |
|---|---|
| Description | Programmable logic controller (PLC) development, communication protocol and runtime environment. |
| Port | 1200/tcp |
| Detailed page | [codesys.md](protocols/codesys.md) |
### Conferences
- [Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - Jimmy Wylie @ DEF CON 30 (2022)


## CSPv4
| Name | CSPv4 |
|---|---|
| Alias | AB CSPv4, AB/Ethernet |
| Description | Allen-Bradley's protocol for industrial Ethernet communication |
| Keywords | Allen-Bradley, PCCC |
| Port | 2222/tcp |
| Nmap script(s) | [cspv4-info.nse](https://github.com/digitalbond/Redpoint/blob/master/cspv4-info.nse) |
| Detailed page | [cspv4.md](protocols/cspv4.md) |



## DeviceNet
| Name | DeviceNet |
|---|---|
| Description | CAN-based industrial automation network for device-level communication |
| Keywords | CAN, CIP |
| Wireshark dissector | [packet-devicenet.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-devicenet.c) |
| Detailed page | [devicenet.md](protocols/devicenet.md) |
### Documentations
- [Common Industrial Protocol (CIP) and the family of CIP networks](https://www.odva.org/wp-content/uploads/2020/06/PUB00123R1_Common-Industrial_Protocol_and_Family_of_CIP_Networks.pdf) - ODVA publication (2016)
- [DeviceNet](https://www.odva.org/technology-standards/key-technologies/devicenet/) - Overview on ODVA.org
### Articles
- [DeviceNet and Ethernet/IP](https://www.rtautomation.com/rtas-blog/devicenet-and-ethernet-ip/) - Blog post on RTAutomation


## DF1
| Name | DF1 |
|---|---|
| Alias | DF-1 |
| Description | Allen-Bradley serial communication protocol for industrial automation devices |
| Keywords | PCCC, Allen-Bradley |
| Access | Free |
| Specifications | [DF1 specification](https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/1770-rm516_-en-p.pdf) |
| Detailed page | [df1.md](protocols/df1.md) |
### Articles
- [AB/DF1 Protocol Tips](http://iatips.com/df1_tips.html) - Lynn's Industrial Automation Protocol Tips blog
### Tools
- [abdf1](https://sourceforge.net/projects/abdf1/) - AB DF1 Protocol RS232 driver for Micrologix, SLC500, PLC 5
- [Df1](https://github.com/leicht/Df1) - Df1 protocol for Allen-Bradley PLC


## DICOM
| Name | DICOM |
|---|---|
| Alias | DCM |
| Description | Communication and management of medical imaging information |
| Keywords | Radiography, Medical |
| Port | 104/tcp |
| Access | Free |
| Specifications | [DICOM Standard](https://www.dicomstandard.org/current/) |
| Nmap script(s) | [dicom-ping.nse](https://nmap.org/nsedoc/scripts/dicom-ping.html) |
| Wireshark dissector | [packet-dcm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dcm.c) |
| Detailed page | [dicom.md](protocols/dicom.md) |
### Tools
- [DCMTK](https://dcmtk.org/en/) - DICOM ToolKit
- [dicom-server](https://github.com/microsoft/dicom-server) - Microsoft's OSS Implementation of DICOMweb standard
- [pydicom](https://github.com/pydicom/pydicom) - Python package to read, modify and write DICOM files


## DNP3
| Name | DNP3 |
|---|---|
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
| Name | Ether-S-I/O |
|---|---|
| Alias | EtherSIO, ESIO |
| Description | Proprietary protocol for Saia PCD controller I/O communication |
| Keywords | SAIA |
| Port | 6060/udp |
| Wireshark dissector | [packet-esio.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-esio.c) |
| Example Pcap(s) | [ICS-pcap Ether-S-I/O](https://github.com/automayt/ICS-pcap/tree/master/ETHERSIO) |
| Detailed page | [ether-s-io.md](protocols/ether-s-io.md) |



## EtherCAT
| Name | EtherCAT |
|---|---|
| Alias | ECATF, ECAT |
| Description | Real-time industrial Ethernet communication protocol for automation systems |
| Port | 34980/udp |
| Scapy layer | [ethercat.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/ethercat.py) |
| Example Pcap(s) | [ICS-pcap EtherCAT](https://github.com/automayt/ICS-pcap/tree/master/ETHERCAT/ethercat) |
| Detailed page | [ethercat.md](protocols/ethercat.md) |
### Articles
- [Industrial Network Options: EtherCAT Advantages, Challenges, and Specs](https://control.com/technical-articles/introduction-to-ethercat/) - Carlos Aguilar, Control Automation (2023)


## Ethernet/IP
| Name | Ethernet/IP |
|---|---|
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
### Documentations
- [Common Industrial Protocol (CIP) and the family of CIP networks](https://www.odva.org/wp-content/uploads/2020/06/PUB00123R1_Common-Industrial_Protocol_and_Family_of_CIP_Networks.pdf) - ODVA publication (2016)
- [Ethernet/IP](https://www.odva.org/technology-standards/key-technologies/ethernet-ip/) - Overview on ODVA.org
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


## ETP
| Name | ETP |
|---|---|
| Description | Energistics' protocol for interoperable oil and gas data exchange |
| Keywords | Energetics |
| Detailed page | [etp.md](protocols/etp.md) |



## FF-HSE
| Name | FF-HSE |
|---|---|
| Alias | Foundation Fieldbus HSE, FF |
| Description | Ethernet-based communication for industrial process automation devices |
| Port | 1089/tcp, 1090/tcp, 1091/tcp, 1089/udp, 1090/udp, 1091/udp |
| Wireshark dissector | [packet-ff.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-ff.c) |
| Detailed page | [ff-hse.md](protocols/ff-hse.md) |



## FINS
| Name | FINS |
|---|---|
| Alias | OMRON |
| Description | Omron's industrial communication protocol for automation systems |
| Port | 9600/udp |
| Nmap script(s) | [omrontcp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omrontcp-info.nse), [omronudp-info.nse](https://github.com/digitalbond/Redpoint/blob/master/omronudp-info.nse) |
| Wireshark dissector | [packet-omron-fins.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-omron-fins.c) |
| Detailed page | [fins.md](protocols/fins.md) |
### Conferences
- [Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - Jimmy Wylie @ DEF CON 30 (2022)


## FL-net
| Name | FL-net |
|---|---|
| Alias | Factory LAN, OPCN-2 |
| Description | Japan Electrical Manufacturers' Association's industrial-use open network |
| Keywords | JEMA |
| Port | 55000/udp, 55001/udp, 55002/udp, 55003/udp |
| Access | Free |
| Specifications | [FL-net specification](https://www.jema-net.or.jp/English/businessfields/standarization/opcn/standard/) |
| Detailed page | [fl-net.md](protocols/fl-net.md) |



## GE-SRTP
| Name | GE-SRTP |
|---|---|
| Description | General Electric's protocol for communication between GE devices and SCADA |
| Port | 18245/tcp |
| Detailed page | [ge-srtp.md](protocols/ge-srtp.md) |



## HART-IP
| Name | HART-IP |
|---|---|
| Alias | HART, WirelessHART |
| Description | IP-based communication protocol for HART (ICS) data transmission |
| Wireshark dissector | [packet-hartip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hartip.c) |
| Example Pcap(s) | [ICS-pcap HART-IP](https://github.com/automayt/ICS-pcap/tree/master/HART%20IP/hart_ip) |
| Detailed page | [hart-ip.md](protocols/hart-ip.md) |
### Articles
- [WirelessHART Radio Communication Standard](https://control.com/textbook/wireless-instrumentation/wirelesshart/) - Lessons in Industrial Automation textbook, Control Automation
### Conferences
- [Dissecting Industrial Wireless Implementations](https://www.youtube.com/watch?v=I-TCfl0Jm2M) - Blake Johnson @ DEF CON 25 ICS Village (2017)
- [DTM Components: Shadow Keys to the ICS Kingdom](https://www.youtube.com/watch?v=VeMgbC0a-u8) - Alexander Bolshev and Gleb Cherbov @ Black Hat Europe (2014)
- [ICSCorsair: How I Will PWN Your ERP Through 4-20 mA Current Loop](https://www.youtube.com/watch?v=T9tahQImuWI) - Alexander Bolshev and Gleb Cherbov @ Black Hat USA (2014)
- [It WISNt Me Attacking Industrial Wireless Mesh Networks](https://www.youtube.com/watch?v=-WfP2VVhTt0) - Paternotte and van Ommeren @ DEF CON 25 (2018)


## HICP
| Name | HICP |
|---|---|
| Alias | SHICP |
| Description | Anybus' Host Interface Control Protocol |
| Keywords | Anybus |
| Port | 3250/udp |
| Wireshark dissector | [packet-hicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hicp.c), [packet-shicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-shicp.c) |
| Detailed page | [hicp.md](protocols/hicp.md) |



## HL7
| Name | HL7 |
|---|---|
| Description | Standard for healthcare data exchange and interoperability |
| Wireshark dissector | [packet-hl7.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hl7.c) |
| Detailed page | [hl7.md](protocols/hl7.md) |
### Conferences
- [Pestilential Protocol: How Unsecure HL7 Messages Threaten Patient Lives](https://www.youtube.com/watch?v=66x3vfac8rA) - Christian Dameff, Jeffrey Tully & Maxwell Bland @ Black Hat USA (2018)
- [Playing with FHIR](https://www.youtube.com/watch?v=wrNyd60XPMg) - Alissa Knight, Mitch Parker @ DEF CON 29 Biohacking Village (2021)
- [Understanding HL7 2.X Standards, Pen Testing, and Defending HL7 2.X Messages](https://www.youtube.com/watch?v=MR7cH44fjrc) - Anirudh Duggal @ Black Hat USA (2016)


## ICCP
| Name | ICCP |
|---|---|
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
| Name | IEC-60870-5-104 |
|---|---|
| Alias | IEC-104 |
| Description | Grid communication protocol for control and monitoring |
| Port | 2404/tcp |
| Access | Paid |
| Specifications | [IEC-60870-5-104 Specification](https://webstore.iec.ch/publication/25035) |
| Nmap script(s) | [iec-identify.nse](https://nmap.org/nsedoc/scripts/iec-identify.html) |
| Wireshark dissector | [packet-iec104.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-iec104.c) |
| Scapy layer | [iec104.py](https://github.com/secdev/scapy/tree/master/scapy/contrib/scada/iec104) |
| Example Pcap(s) | [ICS-pcap IEC-60870-5-104](https://github.com/automayt/ICS-pcap/tree/master/IEC%2060870) |
| Detailed page | [iec-60870-5-104.md](protocols/iec-60870-5-104.md) |
### Conferences
- [Industroyer/Crashoverride: Zero Things Cool About a Threat Group Targeting the Power Grid](https://www.youtube.com/watch?v=TH17hSH1PGQ) - Anton Cherepanov, Ben Miller, Joe Slowik,  Robert Lee, and Robert Lipovsky @ Black Hat USA (2017)
- [Industroyer2: Sandworm&#39;s Cyberwarfare Targets Ukraine&#39;s Power Grid Again](https://www.youtube.com/watch?v=xC9iM5wVedQ) - Robert Lipovsky & Anton Cherepanov @ Black Hat USA (2022)
### Papers
- [Description and analysis of IEC 104 Protocol](https://www.fit.vut.cz/research/publication/11570/.en) - Technical report by Petr Matousek @ Faculty of Information Techology, Czech Republic (2017)
### Tools
- [FreyrSCADA IEC-60870-5-104](https://github.com/FreyrSCADA/IEC-60870-5-104) - IEC 60870-5-104 Protocol - RTU Server and Master Client Simulator
- [lib60870](https://github.com/mz-automation/lib60870) - Implementation of the IEC 60870-5-101/104 protocol


## IEC-61850
| Name | IEC-61850 |
|---|---|
| Alias | IEC-61850/GOOSE, IEC-61850/GSSE, IEC-61850/SV |
| Description | Communication networks and systems for power utility automation |
| Keywords | Power grid |
| Access | Paid |
| Specifications | [IEC 61850 Specification](https://webstore.iec.ch/publication/6028) |
| Wireshark dissector | [packet-goose.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-goose.c), [packet-sv.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sv.c) |
| Detailed page | [iec-61850.md](protocols/iec-61850.md) |
### Conferences
- [Fuzz Testing IEC 61850](https://www.youtube.com/watch?v=QehBHZyy4W4) - Markus Mahrla @ CS3STHLM 2019
### Tools
- [libiec61850](https://github.com/mz-automation/libiec61850) - Open-source library for the IEC 61850 protocols


## IEEE-C37.118
| Name | IEEE-C37.118 |
|---|---|
| Alias | C37.118, Synchrophasor, Synphasor |
| Description | Standard for synchrophasor data exchange in power systems |
| Keywords | Power |
| Wireshark dissector | [packet-synphasor.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-synphasor.c) |
| Detailed page | [ieee-c37118.md](protocols/ieee-c37118.md) |
### Tools
- [OpenPDC](https://github.com/GridProtectionAlliance/openPDC) - Open Source Phasor Data Concentrator
- [PyMU](https://github.com/iti/pymu) - Library based on the C37.118.2-2011 standard used for accessing PMU data in real-time


## ISA100.11a
| Name | ISA100.11a |
|---|---|
| Description | Wireless standard for industrial automation and control systems |
| Detailed page | [isa10011a.md](protocols/isa10011a.md) |
### Conferences
- [It WISNt Me Attacking Industrial Wireless Mesh Networks](https://www.youtube.com/watch?v=-WfP2VVhTt0) - Paternotte and van Ommeren @ DEF CON 25 (2018)


## KNXnet/IP
| Name | KNXnet/IP |
|---|---|
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
- [Sneak into buildings with KNXnet/IP](https://www.youtube.com/watch?v=QofeTV39kQE) - Claire Vacherot @ DEF CON 29 (2021)
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
| Name | LoRaWAN |
|---|---|
| Alias | LoRa |
| Description | Long-range IoT communication protocol with low power requirements |
| Keywords | Wireless |
| Access | Free |
| Specifications | [LoRaWAN specification](https://lora-alliance.org/resource_hub/lorawan-specification-v1-1/) |
| Wireshark dissector | [packet-lorawan.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-lorawan.c) |
| Detailed page | [lorawan.md](protocols/lorawan.md) |
### Conferences
- [Can you hear me now DEF CON](https://www.youtube.com/watch?v=lhHM6TX2RrI) - wasabi @ DEF CON 26 Wireless Village (2018)
- [Lora Smart Water Meter Security Analysis](https://www.youtube.com/watch?v=b7ekygjC3so) - Zeng and Panel @ DEF CON 26 (2018)
- [Outsmarting the Smart City](https://www.youtube.com/watch?v=Opjb5hPlxtY) - Daniel Crowley, Jennifer Savage and Mauro Paredes @ Black Hat USA (2018)
- [Reversting LoRa Deconstructing a Next Gen Proprietary LP](https://www.youtube.com/watch?v=KEjlkZA2olE) - Matt Knight @ DEF CON 24 Wireless Village (2016)
### Tools
- [ChirpOTLE](https://github.com/seemoo-lab/chirpotle) - LoRaWAN Security Evaluation Framework
- [ChirpStack Network Server](https://github.com/brocaar/chirpstack-network-server) - Open-source LoRaWAN network-server
- [lorawan-server](https://github.com/gotthardp/lorawan-server) - Compact server for private LoRaWAN networks
- [lorawan-stack](https://github.com/TheThingsNetwork/lorawan-stack) - Open Source LoRaWAN Network Server


## M-Bus
| Name | M-Bus |
|---|---|
| Alias | Meter-Bus, EN13757 |
| Description | Communication protocol for utility metering devices |
| Access | The old specification is free, not the current one |
| Specifications | [M-Bus specification](https://m-bus.com/documentation) |
| Detailed page | [m-bus.md](protocols/m-bus.md) |



## MELSEC
| Name | MELSEC |
|---|---|
| Alias | MEL-SEC |
| Description | Communication protocol for Mitsubishi Electric's MELSEC series of PLCs |
| Keywords | Mitsubishi, MELSOFT |
| Detailed page | [melsec.md](protocols/melsec.md) |
### Conferences
- [Taking Apart and Taking Over ICS & SCADA Ecosystems](https://www.youtube.com/watch?v=L0w_aE4jRFw) - Mars Cheng & Selmon Yang @ DEF CON 29 (2021)


## Modbus
| Name | Modbus |
|---|---|
| Alias | Modbus TCP |
| Description | Widely used industrial communication protocol |
| Port | 502/tcp |
| Specifications | [Modbus TCP Specification](https://modbus.org/specs.php) |
| Nmap script(s) | [modbus-discover.nse](https://nmap.org/nsedoc/scripts/modbus-discover.html), [modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) |
| Wireshark dissector | [packet-mbtcp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-mbtcp.c) |
| Scapy layer | [modbus.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/modbus.py) |
| Example Pcap(s) | [ICS-pcap Modbus](https://github.com/automayt/ICS-pcap/tree/master/MODBUS) |
| Detailed page | [modbus.md](protocols/modbus.md) |
### Articles
- [Introduction to Modbus and Modbus Function Codes](https://control.com/technical-articles/introduction-to-modbus-and-modbus-function-codes/) - Shawn Dietrich, Control Automation (2023)
### Conferences
- [Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - Jimmy Wylie @ DEF CON 30 (2022)
- [Fun with Modbus 0x5a Nothing New Still Relevant?](https://www.youtube.com/watch?v=A_B69Rifu1g) - Arnaud Soullié @ DEF CON 25 ICS Village (2017)
- [Industrial Control Systems : Pentesting PLCs 101 (Part 1/2)](https://www.youtube.com/watch?v=iGwm6-lyn2Y) - Arnaud Soullie @ Black Hat Europe (2014)
- [Industrial Control Systems : Pentesting PLCs 101 (Part 2/2)](https://www.youtube.com/watch?v=rP_Jys1_OJk) - Arnaud Soullie @ Black Hat Europe (2014)
- [Industrial Protocol Gateways Under Analysis](https://www.youtube.com/watch?v=Rbkw_jsTBsY) - Marco Balduzzi @ Black Hat USA (2020)
- [Modbus Enumeration | SANS ICS Concepts](https://www.youtube.com/watch?v=QO99yojavvE) - @ SANS ICS Security (2021)
- [Modbus Man-In-The-Middle | SANS ICS Concepts](https://www.youtube.com/watch?v=-1WbegoU8i0) - @ SANS ICS Security (2021)
- [ModScan: A SCADA MODBUS Network Scanner](https://www.youtube.com/watch?v=O_trNBh31lM) - Mark Bristow @ DEF CON 16 (2013)
- [Out of Control: Demonstrating SCADA device exploitation](https://www.youtube.com/watch?v=FTzAkEnwx_c) - Eric Forner & Brian Meixell @ Black Hat USA (2013)
- [The SCADA That Didn't Cry Wolf- Who's Really Attacking Your ICS Devices](https://www.youtube.com/watch?v=0M8nVv0bz6k) - Kyle Wilhoit @ Black Hat USA (2013)
- [Understanding SCADA's Modbus Protocol](https://www.youtube.com/watch?v=oVDYaG2HInU) - Justin Searle @ Black Hat Asia (2015)
- [Unraveling SCADA Protocols Using Sulley Fuzzer](https://www.youtube.com/watch?v=UUta_Ord8GI) - Ganesh Devarajan @ DEF CON 15 (2014)
### Tools
- [Malmod](https://github.com/mliras/malmod) - Scripts to attack Modicon M340 via UMAS
- [PyModbus](https://github.com/pymodbus-dev/pymodbus) - A full modbus protocol written in python


## MQTT
| Name | MQTT |
|---|---|
| Description | Publish-suscribe network protocol for message queue |
| Keywords | Telemetry |
| Nmap script(s) | [mqtt-suscribe.nse](https://nmap.org/nsedoc/scripts/mqtt-subscribe.html) |
| Wireshark dissector | [packet-mqtt.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-mqtt.c) |
| Scapy layer | [mqtt.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/mqtt.py) |
| Detailed page | [mqtt.md](protocols/mqtt.md) |
### Articles
- [Not Just Another IIoT Article: MQTT for Pneumatic Cylinder Maintenance](https://control.com/technical-articles/not-just-another-iiot-article-mqtt-for-pneumatic-cylinder-maintenance/) - Shawn Dietrich, Control Automation (2023)
### Conferences
- [Choo Choo, Network Train - The One to Rule Your Perimeter](https://www.youtube.com/watch?v=RpXoVwCSHA0) - Martin Hron @ Black Hat Europe (2022)
- [Light Weight Protocol: Critical Implications](https://www.youtube.com/watch?v=o7qDVZr0t2c) - Lucas Lundgren, Neal Hindocha @ DEF CON 24 (2016)
- [When Machines Can't Talk](https://www.youtube.com/watch?v=X3fUNWRgeao) - Federico Maggi & Davide Quarta @ Black Hat Europe (2018)


## Niagara Fox
| Name | Niagara Fox |
|---|---|
| Alias | Fox |
| Description | Communication protocol used by Tridium Niagara devices |
| Keywords | Tridium |
| Port | 1911/tcp, 3011/tcp, 4911/tcp, 5011/tcp |
| Nmap script(s) | [fox-info.nse](https://nmap.org/nsedoc/scripts/fox-info.html) |
| Detailed page | [niagara-fox.md](protocols/niagara-fox.md) |
### Tools
- [foxdissector](https://github.com/MartinoTommasini/foxdissector) - Wireshark dissector for the Niagara Fox protocol in Lua


## OPC-DA
| Name | OPC-DA |
|---|---|
| Alias | OPCDA |
| Description | Legacy protocol for real-time data exchange in industrial systems |
| Scapy layer | [opc_da.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/opc_da.py) |
| Detailed page | [opc-da.md](protocols/opc-da.md) |
### Papers
- [Exploring the OPC attack surface](https://claroty.com/team82/research/white-papers/exploring-the-opc-attack-surface) - Claroty Team82 (2021)


## OPC-UA
| Name | OPC-UA |
|---|---|
| Alias | OPCUA |
| Description | Open communication standard for industrial automation and control |
| Port | 4840/tcp, 4840/udp, 4843/tcp (TLS) |
| Wireshark dissector | [OPC-UA Plugin](https://github.com/wireshark/wireshark/tree/master/plugins/epan/opcua) |
| Detailed page | [opc-ua.md](protocols/opc-ua.md) |
### Articles
- [OPC UA Deep Dive (Part 1): History of the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-history-of-the-opc-ua-protocol) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 2): What is OPC UA?](https://claroty.com/team82/research/opc-deep-dive-part-2-what-is-opc-ua) - Claroty Team82 (2023)
- [OPC UA Deep Dive (Part 3): Exploring the OPC UA Protocol](https://claroty.com/team82/research/opc-ua-deep-dive-part-3-exploring-the-opc-ua-protocol) - Claroty Team82 (2023)
- [Practical example of fuzzing OPC UA applications](https://ics-cert.kaspersky.com/publications/reports/2020/10/19/practical-example-of-fuzzing-opc-ua-applications/) - Kaspersky ICS-CERT (2020)
- [Understanding the OPC Unified Architecture (OPC UA) Protocol](https://control.com/technical-articles/understanding-the-opc-ua-protocol/) - Anthony King Ho, Control Automation (2023)
### Conferences
- [A Broken Chain: Discovering OPC UA Attack Surface and Exploiting the Supply Chain](https://www.youtube.com/watch?v=bWJ6DY86hkc) - Eran Jacob @ Black Hat USA (2021)
- [Analyzing PIPEDREAM - Challenges in Testing an ICS Attack Toolkit](https://www.youtube.com/watch?v=_dz6VNYSSJ0) - Jimmy Wylie @ DEF CON 30 (2022)
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
| Name | PC-WORX |
|---|---|
| Description | Software suite with proprietary protocol for Phoenix Contact PLCs |
| Keywords | Phoenix Contact |
| Port | 1962/tcp |
| Nmap script(s) | [pcworx-info.nse](https://github.com/digitalbond/Redpoint/blob/master/pcworx-info.nse) |
| Detailed page | [pc-worx.md](protocols/pc-worx.md) |



## PCCC
| Name | PCCC |
|---|---|
| Alias | AB/PCCC |
| Description | Legacy command/response protocol for Allen-Bradley PLC communication |
| Keywords | Allen-Bradley |
| Detailed page | [pccc.md](protocols/pccc.md) |
### Articles
- [AB/PCCC Protocol Tips](http://iatips.com/pccc_tips.html) - Lynn's Industrial Automation Protocol Tips blog
- [Ethernet/IP PCCC Service Codes](https://iatip.blogspot.com/2008/11/ethernetip-pccc-service-codes.html) - Lynn's Industrial protocols over IP blog


## POWERLINK
| Name | POWERLINK |
|---|---|
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
| Name | ProConOs |
|---|---|
| Description | Real-time operating system with proprietary protocol for industrial automation and control |
| Port | 20547/tcp |
| Nmap script(s) | [proconos-info.nse](https://github.com/digitalbond/Redpoint/blob/master/proconos-info.nse) |
| Detailed page | [proconos.md](protocols/proconos.md) |



## Profinet-DCP
| Name | Profinet-DCP |
|---|---|
| Alias | PNDCP |
| Description | Device identification, configuration, and network management protocol |
| Port | Ethernet |
| Scapy layer | [pnio_dcp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio_dcp.py) |
| Detailed page | [profinet-dcp.md](protocols/profinet-dcp.md) |



## Profinet-IO
| Name | Profinet-IO |
|---|---|
| Alias | PNIO |
| Description | Real-time communication between controllers and I/O devices |
| Port | 34962/udp, 34963/udp, 34964/udp |
| Scapy layer | [pnio.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/pnio.py) |
| Detailed page | [profinet-io.md](protocols/profinet-io.md) |
### Articles
- [What Is the Difference Between Profibus and Profinet?](https://control.com/technical-articles/understanding-profibus-vs-profinet/) - Antonio Armenta, Control Automation (2021)


## S-Bus
| Name | S-Bus |
|---|---|
| Alias | Ether-S-Bus, SAIA S-Bus |
| Description | SAIA's communication protocol for building automation |
| Keywords | SAIA |
| Access | Free |
| Wireshark dissector | [packet-sbus.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sbus.c) |
| Example Pcap(s) | [ICS-pcap Ether-S-Bus](https://github.com/automayt/ICS-pcap/tree/master/ETHERSBUS/sbus) |
| Detailed page | [s-bus.md](protocols/s-bus.md) |



## S7comm
| Name | S7comm |
|---|---|
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


## SECS/GEM
| Name | SECS/GEM |
|---|---|
| Alias | SECS, SECS-I, SECS-II, HSMS |
| Description | Semiconductor equipment communication standard with generic equipment model |
| Keywords | Semiconductor, MES |
| Port | 5000/tcp (HSMS) |
| Detailed page | [secsgem.md](protocols/secsgem.md) |



## SERCOS-III
| Name | SERCOS-III |
|---|---|
| Alias | SERCOS |
| Description | IEC standard universal bus for Ethernet-based real-time communication |
| Wireshark dissector | [packet-sercosiii.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-sercosiii.c) |
| Detailed page | [sercos-iii.md](protocols/sercos-iii.md) |



## SLMP
| Name | SLMP |
|---|---|
| Alias | Seamless Message Protocol |
| Description | CC-Link's messaging protocol for industrial automation communication |
| Keywords | Mitsubishi, CC-Link, CLPA |
| Access | Free |
| Specifications | [SLMP specification](https://www.cc-link.org/en/downloads/nonmembers/form.html) |
| Detailed page | [slmp.md](protocols/slmp.md) |
### Tools
- [PySLMPClient](https://github.com/masahase0117/PySLMPClient) - Python client for SLMP


## TriStation
| Name | TriStation |
|---|---|
| Alias | Triconex TriStation |
| Description | Triconex's proprietary protocol for safety system communication |
| Keywords | Triconex, TRITON |
| Wireshark dissector | [TriStation.lua](https://github.com/NozomiNetworks/tricotools/blob/master/TriStation.lua) |
| Detailed page | [tristation.md](protocols/tristation.md) |
### Articles
- [Attackers Deploy New ICS Attack Framework “TRITON” and Cause Operational Disruption to Critical Infrastructure](https://www.mandiant.com/resources/blog/attackers-deploy-new-ics-attack-framework-triton) - Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer @ Mandiant (2017, updated 2022)
### Conferences
- [How TRITON Disrupted Safety Systems & Changed the Threat Landscape of Industrial Control Systems](https://www.youtube.com/watch?v=Hw2HclZV2Kw) - Andrea Carcano, Marina Krotofil & Younes Dragoni @ Black Hat USA (2018)
- [Thru the Eyes of the Attacker Designing Embedded Systems for ICS](https://www.youtube.com/watch?v=3x4MukvjEm8) - Krotofil, Wetzels @ DEF CON 26 (2018)
### Tools
- [tricotools](https://github.com/NozomiNetworks/tricotools) - Triconex TriStation utilities and tools


## TSAA
| Name | TSAA |
|---|---|
| Description | Messaging protocol to read and write data to Triconex controllers |
| Keywords | Triconex |
| Detailed page | [tsaa.md](protocols/tsaa.md) |
### Documentations
- [Triconex System Access Application (TSAA) playlist](https://www.youtube.com/playlist?list=PLFf3xtcn9d46Eq8tdpTH-cviNPv8P0blU) - What Did You Learn Today (2021)


## UMAS
| Name | UMAS |
|---|---|
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


## WITS
| Name | WITS |
|---|---|
| Alias | WITS0, WITSML |
| Description | Real-time drilling data transfer standard in oil and gas |
| Keywords | Wellsite, Drilling, Geology |
| Detailed page | [wits.md](protocols/wits.md) |



## ZigBee
| Name | ZigBee |
|---|---|
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

> All unreviewed AI-generated data is marked with `*`. ([Why?](./srcs/README.md#note-on-ai-generated-content))

**awesome-industrial-protocols** is licensed under
[CC0](https://creativecommons.org/publicdomain/zero/1.0/). **Turn/IP** is
licensed under [GPL-v3](https://www.gnu.org/licenses/gpl-3.0.en.html).
