# DNP3

| Protocol | DNP3 |
|---|---|
| Name | DNP3 |
| Aliases | Distributed Network Protocol |
| Description | Industrial communication protocol for remote monitoring and control of automation systems |
| Keywords | Power grid, Water |
| Port(s) | 20000/tcp, 20000/udp |
| Access to specs | Paid |
| Specifications | [IEEE 1815-2012](https://standards.ieee.org/ieee/1815/5414/) |
| Security features | Optional authentication, optional encryption with TLS |
| Nmap script(s) | [dnp3-info.nse](https://github.com/digitalbond/Redpoint/blob/master/dnp3-info.nse) |
| Wireshark dissector | [packet-dnp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-dnp.c) |
| Example Pcap(s) | [ICS-pcap DNP3](https://github.com/automayt/ICS-pcap/tree/master/DNP3) |

## Conferences
- [Common Flaws in ICS Network Protocols](https://www.youtube.com/watch?v=Bhq4kC52Qg8) - Mars Cheng & Selmon Yang @ Hack In The Box (2020)
- [DEF CON 33 - There and Back Again: Detecting OT Devices Across Protocol Gateways - Rob King](https://www.youtube.com/watch?v=YBPYYk8FIkc) - @ DEF CON (2025)
- [NSM 101 for ICS](https://www.youtube.com/watch?v=H6AWRziR028) - Chris Sistrunk @ DEF CON 23 101 Track (2015)
- [SCADA Protocol Implementation Considerations | SANS ICS Concepts](https://www.youtube.com/watch?v=Fi7JhLm4vjY) - @ SANS ICS Security (2022)
- [Sniffing SCADA](https://www.youtube.com/watch?v=4vPptUmyv4U) - Karl Koscher @ DEF CON 23 Packet Capture Village (2015)
- [Unraveling SCADA Protocols Using Sulley Fuzzer](https://www.youtube.com/watch?v=UUta_Ord8GI) - Ganesh Devarajan @ DEF CON 15 (2014)
## Tools
- [dnp3-simulator](https://github.com/dnp3/dnp3-simulator) - .NET DNP3 simulator with GUI 
- [FreyrSCADA DNP3](https://github.com/FreyrSCADA/DNP3) - DNP3 Protocol - Outstation Server and Client Master Simulator
- [gec/dnp3](https://github.com/gec/dnp3) - Open source Distributed Network Protocol
- [gec/dnp3slavesim](https://github.com/gec/dnp3slavesim) - Parallel dnp3 slave simulator
- [opendnp3](https://github.com/dnp3/opendnp3) - DNP3 (IEEE-1815) protocol stack. Modern C++ with bindings for .NET and Java
- [Step Function I/O DNP3](https://github.com/stepfunc/dnp3) - Rust implementation of DNP3 (IEEE 1815) with idiomatic bindings for C, .NET, C++, and Java
