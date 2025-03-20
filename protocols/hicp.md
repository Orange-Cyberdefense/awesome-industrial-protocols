# HICP

| Protocol | HICP |
|---|---|
| Name | HICP |
| Aliases | SHICP |
| Description | HMS IP Configuration Protocol |
| Keywords | Anybus |
| Port(s) | 3250/udp |
| Wireshark dissector | [packet-hicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hicp.c), [packet-shicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-shicp.c) |
| Scapy layer | [hicp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/hicp.py) |
| Related CVE | [CVE-2009-4463](https://nvd.nist.gov/vuln/detail/CVE-2009-4463), [CVE-2024-23767](https://nvd.nist.gov/vuln/detail/CVE-2024-23767) |
| Multicast address | None |
| Discovery | **Module Scan**: Request to discover devices, usually sent via broadcast
| | Scapy: `HICPModuleScan()`
| | Raw: `MODULE SCAN\x00` |

## Conferences
- [Trying Gateway Bugs: Breaking Industrial Protocol Translation Devices Before The Research Begins](https://www.youtube.com/watch?v=OGdfAlzvuvg) - Claire Vacherot @ Hack.lu (2024)
