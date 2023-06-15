# Ethernet/IP

| Protocol | Ethernet/IP |
|---|---|
| Name | Ethernet/IP |
| Aliases | Enip |
| Description | Ethernet-based industrial communication protocol for industrial automation systems |
| Keywords | CIP |
| Port(s) | 44818/tcp, 2222/udp |
| Access to specs | Paid |
| Specifications | [Ethernet/IP Specifications](https://www.odva.org/subscriptions-services/specifications) |
| Security features |  |
| Nmap script(s) | [enip-info.nse](https://nmap.org/nsedoc/scripts/enip-info.html), [enip-enumerate.nse](https://github.com/digitalbond/Redpoint/blob/master/enip-enumerate.nse) |
| Wireshark dissector | [packet-enip.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-enip.c) |
| Scapy layer | [enipTCP.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/enipTCP.py) |
| Example Pcap(s) | [ICS-pcap Ethernet/IP](https://github.com/automayt/ICS-pcap/tree/master/ETHERNET_IP), [ICS-pcap EIP](https://github.com/automayt/ICS-pcap/tree/master/EIP) |
| Related CVE | [CVE-2012-6435](https://nvd.nist.gov/vuln/detail/CVE-2012-6435), [CVE-2012-6436](https://nvd.nist.gov/vuln/detail/CVE-2012-6436), [CVE-2012-6438](https://nvd.nist.gov/vuln/detail/CVE-2012-6438), [CVE-2012-6439](https://nvd.nist.gov/vuln/detail/CVE-2012-6439), [CVE-2012-6441](https://nvd.nist.gov/vuln/detail/CVE-2012-6441), [CVE-2012-6442](https://nvd.nist.gov/vuln/detail/CVE-2012-6442), [CVE-2018-14827](https://nvd.nist.gov/vuln/detail/CVE-2018-14827), [CVE-2019-6815](https://nvd.nist.gov/vuln/detail/CVE-2019-6815), [CVE-2020-13530](https://nvd.nist.gov/vuln/detail/CVE-2020-13530), [CVE-2020-13556](https://nvd.nist.gov/vuln/detail/CVE-2020-13556), [CVE-2020-13573](https://nvd.nist.gov/vuln/detail/CVE-2020-13573), [CVE-2020-25159](https://nvd.nist.gov/vuln/detail/CVE-2020-25159), [CVE-2020-6083](https://nvd.nist.gov/vuln/detail/CVE-2020-6083), [CVE-2020-6084](https://nvd.nist.gov/vuln/detail/CVE-2020-6084), [CVE-2020-6085](https://nvd.nist.gov/vuln/detail/CVE-2020-6085), [CVE-2020-6086](https://nvd.nist.gov/vuln/detail/CVE-2020-6086), [CVE-2020-6087](https://nvd.nist.gov/vuln/detail/CVE-2020-6087), [CVE-2020-6088](https://nvd.nist.gov/vuln/detail/CVE-2020-6088), [CVE-2021-20987](https://nvd.nist.gov/vuln/detail/CVE-2021-20987), [CVE-2021-21777](https://nvd.nist.gov/vuln/detail/CVE-2021-21777), [CVE-2021-27478](https://nvd.nist.gov/vuln/detail/CVE-2021-27478), [CVE-2021-27482](https://nvd.nist.gov/vuln/detail/CVE-2021-27482), [CVE-2021-27498](https://nvd.nist.gov/vuln/detail/CVE-2021-27498), [CVE-2021-27500](https://nvd.nist.gov/vuln/detail/CVE-2021-27500), [CVE-2021-34754](https://nvd.nist.gov/vuln/detail/CVE-2021-34754), [CVE-2021-36765](https://nvd.nist.gov/vuln/detail/CVE-2021-36765), [CVE-2022-1737](https://nvd.nist.gov/vuln/detail/CVE-2022-1737), [CVE-2022-3752](https://nvd.nist.gov/vuln/detail/CVE-2022-3752), [CVE-2022-43604](https://nvd.nist.gov/vuln/detail/CVE-2022-43604), [CVE-2022-43605](https://nvd.nist.gov/vuln/detail/CVE-2022-43605), [CVE-2022-43606](https://nvd.nist.gov/vuln/detail/CVE-2022-43606) |

## Articles
- [Fuzzing and PR’ing: How We Found Bugs in a Popular Third-Party EtherNet/IP Protocol Stack](https://claroty.com/team82/research/opener-enip-stack-vulnerabilities) - Sharon Brizinov, Tal Keren (Claroty, 2021)
## Conferences
- [Hunting EtherNet/IP Protocol Stacks](https://www.youtube.com/watch?v=0jftEYDo0ao) - Conference by Sharon Brizinov @ SANS ICS Security Summit 2022
## Tools
- [CIPster](https://github.com/liftoff-sr/CIPster) - Ethernet/IP (Common Industrial Protocol) stack in C++
- [enip-stack-detector](https://github.com/claroty/enip-stack-detector) - EtherNet/IP & CIP Stack Detector
- [OpENer](https://github.com/EIPStackGroup/OpENer) - EtherNet/IP stack for I/O adapter devices
- [Redpoint](https://github.com/digitalbond/Redpoint) - Digital Bond's ICS enumeration tools (nmap scripts)
- [scapy-cip-enip](https://github.com/scy-phy/scapy-cip-enip) - Ethernet/IP dissectors for Scapy

> All AI-generated data is marked with `*`.
