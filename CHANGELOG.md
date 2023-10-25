Changelog
=========

## ????-??-??

### Added

- First version of the terminal user interface to view protocols
- New resources for: CAN, HICP, HL7, IEC-104, OPC-DA, OPC-UA, Powerlink
- New protocol: SOME/IP, LIS01/02-A2

### Changed

- Option `search` is now `fetch`
- Option `filter` is now `search`
- Feature (code) `find` is now `search`

## 2023-08-01

### Added

- PR #1: CAN / CAN-FD resources by @bogdzn
- New resources for: BACnet/IP, DNP3, Modbus, S7, UMAS, Zigbee by @biero-el-corridor
- New resources for: HICP, Ethernet/IP, OPC-UA
- Fix filter issues with unknown fields
- Fix filter issues when printing links and packets

## 2023-07-18

### Added

- New resources for: HICP, HL7, IEC-61850
- Note on AI-generated data
- "Packet" objects associated to protocols

### Changed

- Link identifiers and page names for some protocols
- Name and description of some link to conferences

### Removed

- AI requests about protocols' security model
