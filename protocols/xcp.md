# CAN

| Protocol            | XCP                                                                                                                                                        |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                | XCP                                                                                                                                                        |
| Aliases             | Universal Measurement and Calibration Protocol, ASAM MCD-1 XCP                                                                                             |
| Description         | an interface, usually working on top of other protocols (such as USB, CAN/CAN-FD, FlexRay, Ethernet, SXL) to read and write access to the memory of an ECU |
| Keywords            | CANbus, automotive, XCP, ASAM MCD-1 XCP                                                                                                                    |
| Specifications      | [XCP Book v1.5](https://cdn.vector.com/cms/content/application-areas/ecu-calibration/xcp/XCP_Book_V1.5_EN.pdf)                                             |
| Wireshark dissector |                                                                                                                                                            |
| Scapy layer         | [contrib/automotive/xcp](https://github.com/secdev/scapy/tree/master/scapy/contrib/automotive/xcp)                                                         |
| Related CVE         |                                                                                                                                                            |

## Documentations

- [ASAM wiki on XCP standard](https://www.asam.net/standards/detail/mcd-1-xcp/wiki/) - Wiki describing Protocol history, Frame Layout, etc.
- [Official specifications link (not free)](https://www.asam.net/standards/detail/mcd-1-xcp/) - Official specifications (not free).
- [AutoSAR requirements on XCP](https://www.autosar.org/fileadmin/standards/R21-11/CP/AUTOSAR_SRS_XCP.pdf) - AutoSAR requirements to implement XCP stack in an ECU.

## Articles

- [Free technical book on XCP from Vektor](https://www.vector.com/int/en/know-how/protocols/xcp-measurement-and-calibration-protocol/xcp-book/#) - Free book on XCP protocol and how to use it.

## Tools

- [autofuze](https://github.com/DanAurea/AutoFuze/tree/master/protocols/xcp) - Automotive Fuzzing tool providing XCP implementation over USB and CAN 
- [xcpdump](https://github.com/christoph2/xcpdump) - XCP sniffer over SocketCAN.
- [a2lparser](https://github.com/mrom1/a2lparser) - library able to parse `.a2l` files