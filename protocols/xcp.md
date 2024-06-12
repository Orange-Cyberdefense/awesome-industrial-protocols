# XCP

| Protocol | XCP |
|---|---|
| Name | XCP |
| Aliases | Universal Measurement and Calibration Protocol, ASAM MCD-1 XCP |
| Description | Interface usually working on top of other protocols (such as USB, CAN/CAN-FD, FlexRay, Ethernet, SXL) to read and write the memory of an ECU |
| Keywords | CANbus, Automotive, XCP, ASAM MCD-1 XCP |
| Access to specs | Paid |
| Specifications | [XCP Book v1.5](https://cdn.vector.com/cms/content/application-areas/ecu-calibration/xcp/XCP_Book_V1.5_EN.pdf), [ASAM MCD-1 XCP specifications](https://www.asam.net/standards/detail/mcd-1-xcp/) |
| Scapy layer | [automotive/xcp](https://github.com/secdev/scapy/tree/master/scapy/contrib/automotive/xcp) |

## Documentations
- [ASAM wiki on XCP standard](https://www.asam.net/standards/detail/mcd-1-xcp/wiki) - Wiki describing protocol history, frame layout, etc.
- [AutoSAR requirements on XCP](https://www.autosar.org/fileadmin/standards/R21-11/CP/AUTOSAR_SRS_XCP.pdf) - AutoSAR requirements to implement XCP stack in an ECU
- [The XCP Reference Book](https://www.vector.com/int/en/know-how/protocols/xcp-measurement-and-calibration-protocol/xcp-book/) - Free technical book on XCP protocol and how to use it (Vector)
## Tools
- [a2lparser](https://github.com/mrom1/a2lparser) - Python A2L parser and XML exporter
- [AutoFuze](https://github.com/DanAurea/AutoFuze/tree/master/protocols/xcp) - Automotive Fuzzing tool providing XCP implementation over USB and CAN
- [xcpdump](https://github.com/christoph2/xcpdump) - ASAM XCP sniffer for SocketCAN
