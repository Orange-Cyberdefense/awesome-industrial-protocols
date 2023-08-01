# HICP

| Protocol | HICP |
|---|---|
| Name | HICP |
| Aliases | SHICP |
| Description | Anybus' Host Interface Control Protocol |
| Keywords | Anybus |
| Port(s) | 3250/udp |
| Wireshark dissector | [packet-hicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hicp.c), [packet-shicp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-shicp.c) |
| Scapy layer | [hicp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/hicp.py) |
| Related CVE | [CVE-2009-4463](https://nvd.nist.gov/vuln/detail/CVE-2009-4463) |
| Multicast address | None |
| Discovery | **Module Scan**: Request to discover devices, usually sent via broadcast
| | Scapy: `HICPModuleScan()`
| | Raw: `MODULE SCAN\x00` |



> All unreviewed AI-generated data is marked with `*`. ([Why?](../srcs/README.md#note-on-ai-generated-content))
