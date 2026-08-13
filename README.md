# MC/DC-VVP

![MC/DC logo](https://raw.githubusercontent.com/mcdc-project/mcdc/main/assets/mcdc-logo.svg)

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

A collection of verification, validation, and performance (VVP) test suites for [MC/DC](https://github.com/mcdc-project/mcdc).

The repository provides a unified framework for launching, processing, and organizing MC/DC-VVP campaigns on local workstations and HPC platforms. Each verification, validation, and performance suite is self-contained and can be executed independently, while the top-level workflow enables reproducible campaign-wide execution. On supported HPC systems, campaign orchestration is performed using [Maestro](https://github.com/llnl/maestrowf).

## Repository organization

```text
configs/        Shared platform, user, and launch configurations
verification/   Verification test suites
validation/     Validation test suites
performance/    Performance test suites
results/        Processed results from completed campaigns

launch.py       Launch all enabled suites
process.py      Process all enabled suites
```

Each suite contains its own launch and processing workflow and may also be executed manually without the top-level scripts.

## Quick start

1. Create a user launch configuration:

```bash
cp configs/launch_config.py.template configs/launch_config.py
```

2. Edit `configs/launch_config.py` to enable the desired suites and select the target platform.

3. Launch the enabled suites:

```bash
# Local execution
python launch.py

# HPC execution
python launch.py --platform tuolumne
```

4. After all jobs have completed, process the results:

```bash
python process.py
```

Processed figures, metadata, and summary results are written to the `results/` directory.

## Verification suites

### Analytical verification

Analytical verification demonstrates the expected statistical convergence of MC/DC by comparing numerical solutions against analytical reference solutions as the number of source particles is increased.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport | Fixed-source | Multigroup steady-state and transient fixed-source problems, including Reed's problem, AZURV1 variants, and infinite SHEM-361 benchmarks. |

### Benchmark verification

Benchmark verification compares MC/DC against established reference Monte Carlo codes on problems without analytical solutions.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport (multigroup) | Benchmark multigroup | Time-dependent benchmark problems, including the Kobayashi Dog-Leg and C5G7 transient benchmarks. |
| Neutron transport (continuous energy) | Benchmark continuous energy | Continuous-energy benchmark problems for representative reactor systems. |

## Validation

Validation suites compare MC/DC predictions against experimental measurements.

*Coming soon.*

## Performance

Performance suites evaluate computational performance, scalability, and efficiency across supported execution platforms.

*Coming soon.*

## Documentation

Comprehensive user and developer documentation will be available on Read the Docs. It will include:

- Framework architecture
- Launch and processing workflow
- Platform and user configuration
- Adding new suites and cases
- Developer guidelines
