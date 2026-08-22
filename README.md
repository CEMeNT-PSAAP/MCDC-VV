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
results/               Processed results organized by suite

launch.py              Launch all enabled suites
process.py             Collect available suite results
```

MC/DC-VVP uses **suite** and **case** as standard terms for its two organizational levels:

- A **suite** is a self-contained collection of related VVP cases with a shared launch and processing workflow.
- A **case** is one individual problem definition and its inputs, reference solution or data, and processing logic.

The top-level workflow launches enabled suites and collects available suite results, while each suite workflow runs and processes its cases.
Every integrated suite provides a README that describes its layout, configuration, workflow, and cases.

## Configuration

Create the local launch configuration:

```bash
cp configs/launch_config.py.template configs/launch_config.py
```

Edit `configs/launch_config.py` to enable the desired suites and set their platform and launch options.
Use `platform=None` for local execution or a name from `configs/platform_config.py` for HPC execution.
For HPC execution, `N_node` sets the number of nodes and each node uses all available CPU cores.
For HPC execution, a suite's base `walltime` in hours is scaled by each case's `walltime_factor` in that suite's `task.yaml`.
The scaled value is rounded up to the scheduler's supported resolution, the platform maximum remains the final limit, and local execution ignores walltime settings.

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

After processing the desired suites, collect their available `results/` directories:

```bash
python process.py
```

The top-level processor checks every suite registered in `configs/launch_config.py` and moves each available suite `results/` directory under the same suite path in the top-level `results/` directory.
Within each suite, `convergence/` contains study-wide convergence figures and `comparison/` contains plots or animations from the largest-statistics result.
Collecting a suite replaces that suite's existing top-level results.

## Suites

### Analytical verification

Analytical verification demonstrates the expected statistical convergence of MC/DC by comparing numerical solutions against analytical and semi-analytical reference solutions as the sampling effort is increased.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport | [Fixed-source](verification/analytical/neutron/fixed_source/README.md) | Multigroup steady-state and transient cases, including a two-group manufactured solution, Reed's problem, AZURV1 variants, and infinite SHEM-361 benchmarks. |
| Neutron transport | [k-eigenvalue](verification/analytical/neutron/k_eigenvalue/README.md) | Homogeneous and Kornreich-Parsons one-group slab benchmarks, plus infinite homogeneous SHEM-361 cases. |

### Code-to-code verification

Code-to-code verification assesses whether relative differences among independently implemented transport codes decrease at the expected statistical rate as their sampling effort increases.
Convergence proportional to $N^{-1/2}$ supports that the participating codes are approaching the same solution at the expected Monte Carlo rate, although agreement alone cannot exclude shared bias.
The arithmetic mean of all participating code estimates at the largest sampling level defines a fixed comparison reference for every level, allowing a case to include two or more codes without designating one as exact.

| Physics | Suite | Description |
| :------ | :---- | :---------- |
| Neutron transport | [Code-to-code](verification/code_to_code/neutron/README.md) | Time-dependent C5G7 and Kobayashi comparisons against OpenMC. |

## Validation

Validation suites compare MC/DC predictions against experimental measurements.

*Coming soon.*

## Performance

Performance suites evaluate computational performance, scalability, and efficiency across supported execution platforms.

*Coming soon.*

## Documentation

The top-level and suite READMEs provide the repository-specific documentation for MC/DC-VVP.
