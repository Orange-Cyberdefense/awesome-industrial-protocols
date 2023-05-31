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

- [Ethernet/IP](#ethernetip)
- [KNXnet/IP](#knxnetip)



## Ethernet/IP
| Protocol | Ethernet/IP |
|---|---|
| Name | Ethernet/IP |
| Alias | Enip |
| Description | Ethernet-based industrial communication protocol for industrial automation systems. |
| Keywords | CIP |
| Port | 44818/tcp, 2222/udp |
| Access | 1000$ |
| Specifications | [Ethernet/IP Specifications](https://www.odva.org/subscriptions-services/specifications) |
| Security |  |
| Nmap script(s) | [enip-info](https://nmap.org/nsedoc/scripts/enip-info.html) |
| Wireshark dissector | [Ethernet/IP Wireshark dissector](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-enip.c) |
| Scapy layer | [Ethernet/IP Scapy layer](https://github.com/secdev/scapy/blob/master/scapy/contrib/enipTCP.py) |
### Tools
- [OpENer: Ethernet/IP stack](https://github.com/EIPStackGroup/OpENer)
- [Digital Bond's ICS enumeration tools (nmap scripts)](https://github.com/digitalbond/Redpoint)
- [Ethernet/IP dissectors for Scapy](https://github.com/scy-phy/scapy-cip-enip)
- [ICS PCAPs Collection](https://github.com/automayt/ICS-pcap)
- [EtherNet/IP & CIP Stack Detector](https://github.com/claroty/enip-stack-detector)
### Articles
- [Fuzzing and PR’ing: How We Found Bugs in a Popular Third-Party EtherNet/IP Protocol Stack](https://claroty.com/team82/research/opener-enip-stack-vulnerabilities)


## KNXnet/IP
| Protocol | KNXnet/IP |
|---|---|
| Name | KNXnet/IP |
| Alias | KNX, KNX/IP, Konnex |
| Description | Protocol for home and building automation systems. |
| Keywords | BMS, BAS, Building |
| Port | 3671/udp |
| Access | Free |
| Specifications | [KNX Standard](https://my.knx.org/fr/shop/knx-specifications) |
| Security | Optional, Security extensions available |
| Nmap script(s) | [knx-gateway-discover](https://nmap.org/nsedoc/scripts/knx-gateway-discover.html) |
| Wireshark dissector | [KNXnet/IP Wireshark dissector](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-knxip.c) |
| Scapy layer | [KNXnet/IP Scapy layer](https://github.com/secdev/scapy/blob/master/scapy/contrib/knx.py) |
### Conferences
- [Learn how to control every room at a luxury hotel remotely (Jesus Molina, DEFCON 22, 2014)](https://www.youtube.com/watch?v=RX-O4XuCW1Y)
- [Sneak into buildings with KNXnet/IP (Claire Vacherot, DEFCON 29, 2020)](https://www.youtube.com/watch?v=QofeTV39kQE)
### Tools
- [BOF: Testing framework for industrial protocols](https://github.com/Orange-Cyberdefense/bof)
- [KNXmap](https://github.com/takeshixx/knxmap)
- [KNXd service](https://github.com/knxd/knxd)

**awesome-industrial-protocols** is licensed under
[CC0](https://creativecommons.org/publicdomain/zero/1.0/). **Turn/IP** is
licensed under [GPL-v3](https://www.gnu.org/licenses/gpl-3.0.en.html).
