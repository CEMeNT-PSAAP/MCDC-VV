# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html) as a guide.
MC/DC-VVP release numbers align with the corresponding compatible MC/DC release.

## [Unreleased]

Target release: 0.16.0, the first versioned MC/DC-VVP release.

### Added

- Add the analytical neutron $k$-eigenvalue suite with a semi-analytical homogeneous one-group slab, the Kornreich-Parsons heterogeneous slab benchmark, subcritical and supercritical infinite-medium SHEM-361 cases, active-cycle convergence studies, and uncertainty plots, from [@ilhamv]
- Add the analytical neutron fixed-source manufactured two-group slab, from [@ilhamv]
- Add energy-dependent weight-window and time-census variants of the infinite homogeneous SHEM-361 problem, from [@ilhamv]
- Add AZURV1 variants for basic variance-reduction techniques, analytical spatial weight windows, time censuses, and census-based tallies, from [@ilhamv]
- Add a neutron code-to-code verification suite for the C5G7 four-phase and Kobayashi dog-leg transients, including archived participating-code data, fixed largest-sample references, convergence metrics, and animated reference, comparison, and difference results, from [@ilhamv]
- Add preliminary SINBAD model scaffolds for OKTAVIAN Si-60, FNG SiC, FNG/TUD SiC, and RFNC photon-compound experiments based on their public benchmark entries, from [@ilhamv]
- Add top-level and suite-level READMEs describing layouts, configuration, launching, processing, cases, and references, from [@ilhamv]
- Add shared platform, user, and launch configuration for local and HPC campaigns, from [@ilhamv]
- Add top-level cleanup, result collection, and flat GitHub release-asset preparation workflows, from [@ilhamv]
- Add Black formatting checks through pre-commit and GitHub Actions, from [@ilhamv]

### Changed

- Distribute the analytical fixed-source slab cases across the $x$, $y$, and $z$ axes to exercise every Cartesian slab orientation, from [@ilhamv]
- Migration to Maestro-based launch, from [@ilhamv]
- Update analytical fixed-source cases for the simulation-owned MC/DC interface and unified material model, from [@ilhamv]
- Standardize **suite**, **case**, and **task** as the VVP repository's organizational terminology, from [@ilhamv]
- Organize fixed-source cases around consistent input, reference, processing, and optional plotting scripts, from [@ilhamv]
- Reorganize legacy neutron benchmarks as code-to-code verification cases without separate continuous-energy and multigroup directory levels, from [@ilhamv]
- Use `N_node` for HPC resource selection, apply case-specific `walltime_factor` values to suite base walltimes, and skip completed tasks while retaining partial results, from [@ilhamv]
- Organize processed results into convergence, reference, and comparison outputs and collect them through the top-level processing workflow, from [@ilhamv]
- Consolidate the canonical SHEM-361 multigroup dataset under the analytical fixed-source suite for reuse by all SHEM-361 cases, from [@ilhamv]

### Deprecated

### Removed

- Remove the legacy continuous-energy pulsed pin-cell cases, from [@ilhamv]

### Fixed

### Security

[Unreleased]: https://github.com/mcdc-project/mcdc-vvp/tree/dev
[@ilhamv]: https://github.com/ilhamv
