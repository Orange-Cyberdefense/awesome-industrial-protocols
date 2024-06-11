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
| Related CVE | [CVE-2013-2783](https://nvd.nist.gov/vuln/detail/CVE-2013-2783), [CVE-2013-2787](https://nvd.nist.gov/vuln/detail/CVE-2013-2787), [CVE-2013-2788](https://nvd.nist.gov/vuln/detail/CVE-2013-2788), [CVE-2013-2789](https://nvd.nist.gov/vuln/detail/CVE-2013-2789), [CVE-2013-2790](https://nvd.nist.gov/vuln/detail/CVE-2013-2790), [CVE-2013-2791](https://nvd.nist.gov/vuln/detail/CVE-2013-2791), [CVE-2013-2792](https://nvd.nist.gov/vuln/detail/CVE-2013-2792), [CVE-2013-2793](https://nvd.nist.gov/vuln/detail/CVE-2013-2793), [CVE-2013-2809](https://nvd.nist.gov/vuln/detail/CVE-2013-2809), [CVE-2013-2811](https://nvd.nist.gov/vuln/detail/CVE-2013-2811), [CVE-2013-2813](https://nvd.nist.gov/vuln/detail/CVE-2013-2813), [CVE-2013-2821](https://nvd.nist.gov/vuln/detail/CVE-2013-2821), [CVE-2013-2829](https://nvd.nist.gov/vuln/detail/CVE-2013-2829), [CVE-2013-6143](https://nvd.nist.gov/vuln/detail/CVE-2013-6143), [CVE-2014-0761](https://nvd.nist.gov/vuln/detail/CVE-2014-0761), [CVE-2014-2342](https://nvd.nist.gov/vuln/detail/CVE-2014-2342), [CVE-2014-2345](https://nvd.nist.gov/vuln/detail/CVE-2014-2345), [CVE-2014-5425](https://nvd.nist.gov/vuln/detail/CVE-2014-5425), [CVE-2014-5426](https://nvd.nist.gov/vuln/detail/CVE-2014-5426), [CVE-2015-1521](https://nvd.nist.gov/vuln/detail/CVE-2015-1521), [CVE-2015-1522](https://nvd.nist.gov/vuln/detail/CVE-2015-1522), [CVE-2020-6996](https://nvd.nist.gov/vuln/detail/CVE-2020-6996) |

## Conferences
- [Common Flaws in ICS Network Protocols](https://www.youtube.com/watch?v=Bhq4kC52Qg8) - Mars Cheng & Selmon Yang @ Hack In The Box (2020)
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
