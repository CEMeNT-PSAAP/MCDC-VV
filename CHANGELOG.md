# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html) as a guide.
MC/DC-VVP release numbers align with the corresponding compatible MC/DC release.

## [Unreleased]

Target release: 0.16.0, the first versioned MC/DC-VVP release.

### Added

- Add the analytical neutron $k$-eigenvalue MMS one-group slab, from [@ilhamv]
- Add the analytical neutron fixed-source MMS two-group slab, from [@ilhamv]
- Add the analytical neutron $k$-eigenvalue suite with subcritical and supercritical SHEM-361 cases, analytical matrix-eigenvalue references, active-cycle convergence studies, and uncertainty plots, from [@ilhamv]
- Add energy-dependent weight-window and time-census variants of the infinite homogeneous SHEM-361 problem, from [@ilhamv]
- Add AZURV1 variants for basic variance-reduction techniques, analytical spatial weight windows, time censuses, and census-based tallies, from [@ilhamv]
- Add top-level and suite-level READMEs describing layouts, configuration, launching, processing, cases, and references, from [@ilhamv]
- Add shared platform, user, and launch configuration for local and HPC campaigns, from [@ilhamv]

### Changed

- Distribute the analytical fixed-source slab cases across the $x$, $y$, and $z$ axes to exercise every Cartesian slab orientation, from [@ilhamv]
- Migration to Maestro-based launch, from [@ilhamv]
- Update analytical fixed-source cases for the simulation-owned MC/DC interface and unified material model, from [@ilhamv]
- Standardize **suite** and **case** as the VVP repository's organizational terminology, from [@ilhamv]
- Organize fixed-source cases around consistent input, reference, processing, and optional plotting scripts, from [@ilhamv]

### Deprecated

### Removed

### Fixed

### Security

[Unreleased]: https://github.com/ilhamv/mcdc-vvp/tree/master
[@ilhamv]: https://github.com/ilhamv
