# Ethernet/IP

| Protocol | Ethernet/IP |
|---|---|
| Name | Ethernet/IP |
| Aliases | Enip |
| Description | Ethernet-based industrial communication protocol for industrial automation systems. |
| Keywords | CIP |
| Port(s) | 44818/tcp, 2222/udp |
| Access to specs | 1000$ |
| Specifications | [Ethernet/IP Specifications](https://www.odva.org/subscriptions-services/specifications) |
| Security features |  |
| Nmap script(s) | [enip-info](https://nmap.org/nsedoc/scripts/enip-info.html) |
| Wireshark dissector | [packet-enip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-enip.c) |
| Scapy layer | [enipTCP.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/enipTCP.py) |
| Example Pcap(s) | [ICS-pcap Ethernet/IP](https://github.com/automayt/ICS-pcap/tree/master/ETHERNET_IP) |

## Articles
- [Fuzzing and PR’ing: How We Found Bugs in a Popular Third-Party EtherNet/IP Protocol Stack](https://claroty.com/team82/research/opener-enip-stack-vulnerabilities) - Sharon Brizinov, Tal Keren (Claroty, 2021)
## Conferences
- [Hunting EtherNet/IP Protocol Stacks](https://www.youtube.com/watch?v=0jftEYDo0ao) - Conference by Sharon Brizinov @ SANS ICS Security Summit 2022
## Tools
- [OpENer](https://github.com/EIPStackGroup/OpENer) - EtherNet/IP stack for I/O adapter devices
- [Redpoint](https://github.com/digitalbond/Redpoint) - Digital Bond's ICS enumeration tools (nmap scripts)
- [scapy-cip-enip](https://github.com/scy-phy/scapy-cip-enip) - Ethernet/IP dissectors for Scapy
- [enip-stack-detector](https://github.com/claroty/enip-stack-detector) - EtherNet/IP & CIP Stack Detector

> All AI-generated data is marked with `*`.
