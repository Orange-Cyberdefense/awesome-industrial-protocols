Changelog
=========

## 2024-02-02

### Added

- New resources for: CAN, Modbus, UMAS, CIP, CODESYS, DICOM, DNP3,
	Ethernet/IP, FINS, GE-SRTP, OPC-DA, OPC-UA, S-Bus
- New protocol : RTPS, BSAP, FOCAS, MTConnect, MDLC
- 2 new YouTube channel to fetch content from

### Changed

- Fetch now omits results already existing in a protocol.

## 2023-10-27

### Added

- First version of the terminal user interface to view and search protocols
- New resources for: CAN, HICP, HL7, IEC-104, OPC-DA, OPC-UA, Powerlink, KNX
- New protocol: SOME/IP, LIS01/02-A2
- PR #2 by @ValtteriL ; PR #3 by @f0rw4rd

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
