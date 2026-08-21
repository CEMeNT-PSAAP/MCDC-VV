# MC/DC-VVP

![MC/DC logo](https://raw.githubusercontent.com/mcdc-project/mcdc/main/assets/mcdc-logo.svg)

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

A collection of verification, validation, and performance (VVP) test suites for [MC/DC](https://github.com/mcdc-project/mcdc).

The repository provides a unified framework for launching, processing, and organizing MC/DC-VVP campaigns on local workstations and HPC platforms.
Each suite is self-contained and can be executed independently, while the top-level workflow enables reproducible campaign-wide execution.
Workflow orchestration is performed using [Maestro](https://github.com/llnl/maestrowf).

## Directory layout

```text
configs/               Shared platform, user, and launch configurations
verification/          Verification suites and their cases
results/metadata.yaml  Append-only launch and processing history
results/<launch_id>/   Processed results for one recorded launch

launch.py              Launch all enabled suites
process.py             Process one recorded launch
```

MC/DC-VVP uses **suite** and **case** as standard terms for its two organizational levels:

- A **suite** is a self-contained collection of related VVP cases with a shared launch and processing workflow.
- A **case** is one individual problem definition and its inputs, reference solution or data, and processing logic.

The top-level workflow launches and processes enabled suites, while each suite workflow runs and processes its cases.
Every integrated suite provides a README that describes its layout, configuration, workflow, and cases.

## Configuration

Create the local launch configuration:

```bash
cp configs/launch_config.py.template configs/launch_config.py
```

Edit `configs/launch_config.py` to enable the desired suites and set their platform and launch options.
Use `platform=None` for local execution or a name from `configs/platform_config.py` for HPC execution.

For HPC execution, also create `configs/user_config.py` from its template and provide the account and optional queue, reservation, and Python paths for the target platform.

## Launching and processing

Launch locally enabled suites configured with `platform=None`:

```bash
python launch.py
```

Launch enabled suites configured for a specific HPC platform:

```bash
python launch.py --platform tuolumne
```

The `--platform` option selects suites with a matching configured platform.

After the latest launch has completed, process all suites submitted by that launch:

```bash
python process.py
```

Process a specific recorded launch by passing the launch ID printed by `launch.py` and stored in `results/metadata.yaml`:

```bash
python process.py 20260817T120000123456Z
```

Each launch is processed into its own `results/<launch_id>/` directory, which contains a metadata snapshot and the suite result hierarchy.
Reprocessing one launch replaces only that launch's subfolder and does not affect results from other launches.

## Suites

### Analytical verification

Analytical verification demonstrates the expected statistical convergence of MC/DC by comparing numerical solutions against analytical and semi-analytical reference solutions as the sampling effort is increased.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport | [Fixed-source](verification/analytical/neutron/fixed_source/README.md) | Multigroup steady-state and transient cases, including a two-group manufactured solution, Reed's problem, AZURV1 variants, and infinite SHEM-361 benchmarks. |
| Neutron transport | [k-eigenvalue](verification/analytical/neutron/k_eigenvalue/README.md) | Homogeneous and Kornreich-Parsons one-group slab benchmarks, plus infinite homogeneous SHEM-361 cases. |

### Benchmark verification

Benchmark verification compares MC/DC against established reference Monte Carlo codes for cases without analytical solutions.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport (multigroup) | Benchmark multigroup | Time-dependent benchmark cases, including the Kobayashi Dog-Leg and C5G7 transient benchmarks. |
| Neutron transport (continuous energy) | [Benchmark continuous energy](verification/benchmark/neutron/continuous_energy/README.md) | Continuous-energy benchmark cases for representative reactor systems. |

## Validation

Validation suites compare MC/DC predictions against experimental measurements.

*Coming soon.*

## Performance

Performance suites evaluate computational performance, scalability, and efficiency across supported execution platforms.

*Coming soon.*

## Documentation

The top-level and suite READMEs provide the repository-specific documentation for MC/DC-VVP.
