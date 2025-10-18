# Changelog

## [2025.10.1] - 2025-10-18

### Fixed
- Fix name for these wards: 6172, 6187, 16609, 23954, 29857.

## [2025.8.1] - 2025-08-09

### Changed
- Use new data after the rearrangement of July 2025, where district level is dropped.
- Switch to date-base version.
- No longer represent `Province`, `Ward` types as `enum`. We instead have `Province`, `Ward` as dataclasses,
and use `ProvinceCode`, `WardCode` as enum to define valid data.

## [0.6.0] - 2025-01-04

### Changed
- Update data with the form of new towns.


[2025.10.1]: https://github.com/sunshine-tech/VietnamProvinces/releases/tag/v2025.10.1
[2025.8.1]: https://github.com/sunshine-tech/VietnamProvinces/releases/tag/v2025.8.1
[0.6.0]: https://github.com/sunshine-tech/VietnamProvinces/releases/tag/v0.6.0
