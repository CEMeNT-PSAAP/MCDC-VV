# Analytical Neutron Fixed-Source Verification

This suite verifies MC/DC neutron transport using multigroup fixed-source problems with analytical reference solutions.
It exercises geometry tracking, surface crossings, material lookup, source sampling, particle transport, and tallying.
Verification checks for the expected $N^{-1/2}$ statistical convergence as the number of source particles increases.

The suite can be executed independently or as part of the top-level MC/DC-VVP workflow.

## Directory layout

```text
cases/              Verification problem definitions and processing scripts
maestro_run_*/      Generated Maestro workflow directories
results/            Generated figures from processed problems

task.yaml           Configure the particle-count study for each problem
study.yaml          Generated Maestro study definition

launch.py           Build and launch the Maestro study
run_case.py         Run one problem over its particle-count study
process.py          Process a completed Maestro study

cleanup.py          Remove generated outputs and figures
util.py             Provide shared processing and plotting utilities
```

## Configuration

The `task.yaml` file selects the problems and defines the particle-count range and number of tasks for each problem.
Edit this file to change the study without modifying the launch or processing scripts.

HPC runs use the shared platform settings in the repository's `configs/platform_config.py` and the user-specific settings in `configs/user_config.py`.

## Launching and processing

From this suite directory, launch the study locally:

```bash
python launch.py
```

Launch the study on a supported HPC platform:

```bash
python launch.py --platform tuolumne --mpi
```

Use `--walltime HOURS` to limit the requested walltime and `--rewrite` to replace existing problem output.

After all jobs have completed, process the latest Maestro run:

```bash
python process.py
```

Pass a Maestro run directory to process a specific run:

```bash
python process.py maestro_run_<timestamp>
```

Processed figures are written to this suite's `results/` directory.
The top-level `process.py` collects these figures under the repository's `results/` directory.

## Problems

| Problem | Description |
| :------ | :---------- |
| [`slab_absorbium`](cases/slab_absorbium/) | Steady-state flux distribution in a purely absorbing multilayer slab. |
| [`slab_isobeam_td`](cases/slab_isobeam_td/) | Time-dependent flux propagation from an isotropic planar source. |
| [`reed`](cases/reed/) | Reed's classic one-dimensional transport benchmark. |
| [`azurv1`](cases/azurv1/) | AZURV1 transient benchmark. |
| [`azurv1_sub`](cases/azurv1_sub/) | Subcritical variant of AZURV1. |
| [`azurv1_super`](cases/azurv1_super/) | Supercritical variant of AZURV1. |
| [`azurv1-census`](cases/azurv1-census/) | AZURV1 with time censuses. |
| [`azurv1-census-tally`](cases/azurv1-census-tally/) | AZURV1 using time-census-based tallying. |
| [`inf_shem361`](cases/inf_shem361/) | Infinite homogeneous SHEM-361 steady-state spectrum. |
| [`inf_shem361_td`](cases/inf_shem361_td/) | Time-dependent SHEM-361 spectrum evolution. |
| [`inf_shem361_td-census`](cases/inf_shem361_td-census/) | Time-dependent SHEM-361 spectrum evolution with time censuses. |

## References

- W. H. Reed, *New Difference Schemes for the Neutron Transport Equation*, Nuclear Science and Engineering, 1971.
- AZURV1 benchmark.
- SHEM-361 multigroup library.
