# RTSP

| Protocol | RTSP |
|---|---|
| Name | RTSP |
| Aliases | RTP, RTCP |
| Description | Real-Time Streaming Protocol to send video streams |
| Keywords | Camera, Video, Stream |
| Port(s) | 554/tcp |
| Access to specs | Free |
| Specifications | [RFC 2326](https://www.rfc-editor.org/rfc/rfc2326.html), [RFC 3550](https://www.rfc-editor.org/info/rfc3550/) |
| Nmap script(s) | [rtsp-url-brute](https://nmap.org/nsedoc/scripts/rtsp-url-brute.html) |
| Wireshark dissector | [packet-rtsp.c](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-rtsp.c) |
| Scapy layer | [rtsp.py](https://github.com/secdev/scapy/blob/master/scapy/contrib/rtsp.py) |

## Conferences
- [Looping Surveillance Cameras through Live Editing](https://www.youtube.com/watch?v=RoOqznZUClI) - Van Albert and Banks @ DEFCON 23 (2016)
- [Penetration Tests on Video Surveillance Networks](https://www.youtube.com/watch?v=i_qzFF4LeQ4) - Claire Vacherot @ Security Fest (2026)
## Tools
- [cam-amber](https://github.com/Orange-Cyberdefense/cam-amber) - Toolkit for camera discovery and assessment
- [cameradar](https://github.com/Ullaakut/cameradar) - Detect and bruteforce RTSP endpoints
