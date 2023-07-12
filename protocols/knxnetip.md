# KNXnet/IP

| Protocol | KNXnet/IP |
|---|---|
| Name | KNXnet/IP |
| Aliases | KNX, KNX/IP, Konnex |
| Description | Protocol for home and building automation systems |
| Keywords | BMS, BAS, Building |
| Port(s) | 3671/udp |
| Access to specs | Free |
| Specifications | [KNXnet/IP Specifications](https://my.knx.org/en/shop/knx-specifications) |
| Security features | Optional, Security extensions available |
| Nmap script(s) | [knx-gateway-discover.nse](https://nmap.org/nsedoc/scripts/knx-gateway-discover.html) |
| Wireshark dissector | [packet-knxip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-knxip.c) |
| Scapy layer | [knx.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/knx.py) |
| Related CVE | [CVE-2015-8299](https://nvd.nist.gov/vuln/detail/CVE-2015-8299), [CVE-2021-37740](https://nvd.nist.gov/vuln/detail/CVE-2021-37740) |
| Multicast address | 224.0.23.12 |
| Discovery | **Search Request**: Send on KNXnet/IP's multicast address to discover devices |

## Documentations
- [knx.org](https://www.knx.org/knx-en/for-professionals/index.php) - KNX official website
## Conferences
- [(in)Security in Building Automation: How to Create Dark Buildings with Light Speed](https://www.youtube.com/watch?v=PyOhwYgpGfM) - Thomas Brandstetter @ Black Hat USA (2017)
- [InSecurity in Building Automation](https://www.youtube.com/watch?v=G9ESeUWfYbs) - Thomas Brandsetter @ DEF CON 25 ICS Village (2017)
- [Learn how to control every room at a luxury hotel remotely](https://www.youtube.com/watch?v=RX-O4XuCW1Y) - Jesus Molina @ DEF CON 22 (2015)
- [Learn How to Control Every Room at a Luxury Hotel Remotely](https://www.youtube.com/watch?v=xomtYrcTSgU) - Jesus Nomeames @ Black Hat USA (2014)
- [Sneak into buildings with KNXnet/IP](https://www.youtube.com/watch?v=QofeTV39kQE) - Claire Vacherot @ DEF CON 29 (2021)
## Papers
- [An Overview of Wireless IoT Protocol Security in the Smart Home Domain](https://arxiv.org/abs/1801.07090) - Stefan Marksteiner, Víctor Juan Expósito Jiménez, Heribert Vallant, Herwig Zeiner (2018)
## Tools
- [BOF](https://github.com/Orange-Cyberdefense/bof) - Testing framework for industrial protocols
- [ETS](https://www.knx.org/knx-en/for-professionals/software/ets-professional/) - Engineering Tool Software for KNXnet/IP (ETS Demo is free)
- [KNX Virtual](https://www.knx.org/knx-en/for-professionals/get-started/knx-virtual/index.php) - Windows-based application simulating a KNX installation
- [knxd](https://github.com/knxd/knxd) - KNXd service
- [KNXmap](https://github.com/takeshixx/knxmap) - KNXnet/IP scanning and auditing tool
- [XKNX](https://github.com/XKNX/xknx) - A KNX library written in Python

> All unreviewed AI-generated data is marked with `*`.
