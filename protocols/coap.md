# CoAP

| Protocol | CoAP |
|---|---|
| Name | CoAP |
| Aliases | Constrained Application Protocol |
| Description | Constrained REST protocol for IoT and LwM2M field devices |
| Keywords | IoT, LwM2M |
| Port(s) | 5683/udp, 5684/udp (DTLS) |
| Access to specs | Free |
| Specifications | [RFC 7252](https://www.rfc-editor.org/rfc/rfc7252.html) |
| Wireshark dissector | [packet-coap.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-coap.c) |
| Scapy layer | [coap.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/coap.py) |

## Tools
- [OIDA](https://github.com/f0rw4rd/oida) - NetExec-like CLI for OT/ICS assessments, `oida` uses uniform syntax across protocols; `oida coap <target>` enumerates resources via `/.well-known/core` and fingerprints LwM2M devices ([docs](https://getoida.dev/protocols/coap/))
