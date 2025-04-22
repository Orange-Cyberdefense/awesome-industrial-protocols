# S7comm

| Protocol | S7comm |
|---|---|
| Name | S7comm |
| Aliases | S7, S7commPlus |
| Description | Communication protocol for Siemens S7 PLCs |
| Port(s) | 102/tcp |
| Nmap script(s) | [s7-info.nse](https://nmap.org/nsedoc/scripts/s7-info.html), [s7-enumerate.nse](https://github.com/digitalbond/Redpoint/blob/master/s7-enumerate.nse) |
| Wireshark dissector | [packet-s7comm.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-s7comm.c) |
| Example Pcap(s) | [ICS-pcap S7](https://github.com/automayt/ICS-pcap/tree/master/S7) |
| Related CVE | [CVE-2018-4850](https://nvd.nist.gov/vuln/detail/CVE-2018-4850), [CVE-2019-10929](https://nvd.nist.gov/vuln/detail/CVE-2019-10929), [CVE-2021-40368](https://nvd.nist.gov/vuln/detail/CVE-2021-40368) |

## Articles
- [The Siemens S7 Communication - Part 1 General Structure](http://gmiru.com/article/s7comm/) - On GyM's Personal Blog (2016)
- [The Siemens S7 Communication - Part 2 Job Requests and Ack Data](http://gmiru.com/article/s7comm-part2/) - On GyM's Personal Blog (2017)
## Conferences
- [#HITB2021AMS COMMSEC D2 - Breaking Siemens SIMATIC S7 PLC Protection Mechanism - Gao Jian](https://www.youtube.com/watch?v=ocOEiNp-8K0) - @  Hack In The Box (2021)
- [A Decade After Stuxnet: How Siemens S7 is Still an Attacker&#39;s Heaven](https://www.youtube.com/watch?v=4-VoLm2SXao) - @ Black Hat (2024)
- [Fuzzing and Breaking Security Functions of SIMATIC PLCs](https://www.youtube.com/watch?v=XeSSuWR5PaU) - Gao Jian @ Black Hat Europe (2022)
- [Nope, S7ill Not Secure: Stealing Private Keys From S7 PLCs](https://www.youtube.com/watch?v=9AO24tqksRw) - Nadav Adir and Alon Dankner @ Black Hat USA (2024)
- [PLC-Blaster: A worm Living Solely In The PLC](https://www.youtube.com/watch?v=NNAKaAKRUow) - Ralf Spenneberg, Maik Brueggemann & Hendrik Schwartke @ Black Hat Asia (2016)
- [Rogue7: Rogue Engineering-Station Attacks on S7 Simatic PLCs](https://www.youtube.com/watch?v=dHxsctLBUEI) - Uriel Malin, Sara Bitan, Avishai Wool and Eli Biham @ Black Hat USA (2019)
- [The spear to break the security wall of S7CommPlus](https://www.youtube.com/watch?v=93lyRgZYxKw) - Cheng Lei @ DEF CON 25 (2017)
## Tools
- [python-snap7](https://github.com/gijzelaerr/python-snap7) - A Python wrapper for the snap7 PLC communication library
- [s7-pcaps](https://github.com/gymgit/s7-pcaps) - Traffic captures between STEP7/WinCC and S7-300/S7-400 PLCs
- [s7scan](https://github.com/klsecservices/s7scan) - Scan networks to gather basic information about Siemens PLCs
- [Snap7](https://snap7.sourceforge.net/) - Step7 Open Source Ethernet Communication Suite
