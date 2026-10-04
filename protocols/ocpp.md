# OCPP

| Protocol | OCPP |
|---|---|
| Name | OCPP |
| Aliases | Open Charge Point Protocol, OCPP-J |
| Description | Protocol between charge points and a central system for EV charging infrastructure |
| Keywords | EV, Charging |
| Port(s) | 9000/tcp (WebSocket), 443/tcp (wss) |
| Access to specs | Free |
| Specifications | [OCPP 2.0.1 specification](https://www.openchargealliance.org/protocols/) |

## Tools
- [OIDA](https://github.com/f0rw4rd/oida) - NetExec-like CLI for OT/ICS assessments, `oida` uses uniform syntax across protocols; `oida ocpp <url>` tests anonymous access and enumerates charge point configuration over WebSocket ([docs](https://getoida.dev/protocols/ocpp/))
