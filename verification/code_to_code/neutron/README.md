# Neutron Code-to-Code Verification

This suite compares neutron transport results from multiple independently implemented codes.
The current participating codes are MC/DC and OpenMC, and the workflow is intended to accommodate additional codes.
It exercises time-dependent multigroup transport, moving geometry, delayed neutrons, void streaming, and multidimensional space-time tallies.
The arithmetic mean of the participating code estimates at the largest sampling level defines the fixed comparison reference for every level.
The reported metrics are the pair-averaged L2 norm and maximum absolute pairwise relative difference normalized by that fixed reference.
Verification checks for $N^{-1/2}$ decay in both metrics as the participating calculations scale their sampling efforts together.
Observing that rate supports that the codes are converging statistically toward the same solution, while a plateau can indicate bias or a modeling discrepancy.
Agreement does not by itself establish correctness because independently implemented codes can still share a common bias.

The suite can be executed independently or as part of the top-level MC/DC-VVP workflow.

## Directory layout

```text
cases/              Verification case definitions and processing scripts
data/               Shared multigroup cross-section data
maestro_run_*/      Generated Maestro workflow directories
results/
  launch_config.yaml Effective suite launch configuration
  task.yaml          Task-generation configuration used by the launch
  convergence/      Statistical-convergence figures
  reference/        Largest-sample fixed-reference figures and animations
  comparison/       Largest-sample comparison and difference animations

task.yaml           Configure task generation for each case
study.yaml          Generated Maestro study definition

launch.py           Build and launch the Maestro study
run_case.py         Run the tasks for one case
process.py          Process a completed Maestro study

cleanup.py          Remove generated outputs and figures
util.py             Provide shared processing and plotting utilities
```

Each case contains a common set of files:

```text
input.py            Define and run the MC/DC model
reference.py        Download and verify the participating OpenMC outputs
process.py          Evaluate code-to-code convergence
plot.py             Animate one MC/DC and OpenMC result pair
```

## Configuration

The `task.yaml` file selects the cases and defines the particle-count range and number of tasks for each case.
One task is one MC/DC execution at one generated `N_particle` value, paired during processing with the corresponding result from every participating code.
Each case defines a `walltime_factor` that scales the launch-level walltime for HPC execution.
The base walltime is specified in hours, and the scaled value is rounded up to the scheduler resolution and limited by the platform maximum.
For example, a base of `1.5` hours gives C5G7 1 hour 30 minutes and Kobayashi 45 minutes.
Local execution ignores walltime.
Each case uses 30 batches, matching the corresponding OpenMC campaign.
The total number of particle histories shown during processing is therefore the particle count per batch multiplied by 30.
The largest particle-count task supplies the participating results used to construct the fixed comparison reference.

The OpenMC statepoints are canonical external comparison data because they are too large to track in this repository.
Download and checksum them from their Zenodo records before processing:

```bash
python cases/c5g7-4phase/reference.py
python cases/kobayashi/reference.py
```

HPC runs use the shared platform settings in the repository's `configs/platform_config.py` and the user-specific settings in `configs/user_config.py`.
The `N_node` option sets the number of nodes, with all available CPU cores used on each node.

## Launching and processing

From this suite directory, launch the study locally:

```bash
python launch.py
```

Launch the study on a supported HPC platform:

```bash
python launch.py --platform tuolumne --N_node 1
```

Use `--walltime HOURS` to set the base walltime.
Cases with all five MC/DC outputs are omitted from the Maestro study, while partially complete cases run only their missing particle levels.
Run `python cleanup.py` before launching to remove existing case outputs and start the suite fresh.

After all jobs have completed and the OpenMC comparison data have been downloaded, process the latest Maestro run:

```bash
python process.py
```

Pass a Maestro run directory to process a specific run:

```bash
python process.py maestro_run_<timestamp>
```

Convergence figures are written to `results/convergence/`.
Fixed-reference figures and animations are written to `results/reference/`.
Animated spatial comparisons and relative-difference evolution at the largest shared sample size are written to `results/comparison/`.
Each case may produce `reference_*.png` figures or `reference_*.gif` animations from the arithmetic mean of the largest-sample participating-code estimates.
Each case produces `comparison.gif` for the participating-code solutions and `difference.gif` for their relative differences.
The top-level `process.py` collects these figures under the repository's `results/` directory.

Each case's `plot.py` can inspect one MC/DC and OpenMC result pair using the largest-sample pair as the fixed comparison reference:

```bash
python cases/kobayashi/plot.py \
    cases/kobayashi/output_100000000.h5 \
    cases/kobayashi/reference/output_0.h5 \
    cases/kobayashi/output_10000000000.h5 \
    cases/kobayashi/reference/output_4.h5
```

## Cases

| Case | Description |
| :--- | :---------- |
| [`c5g7-4phase`](cases/c5g7-4phase/) | Four-phase C5G7 transient with a pulsed source and continuously moving control rods. |
| [`kobayashi`](cases/kobayashi/) | Pulsed three-dimensional Kobayashi dog-leg shielding problem with a void channel. |

### Four-phase C5G7 transient

This seven-group problem adapts the heterogeneous C5G7-TD core into four source- and control-rod-driven phases over 20 seconds.
The quantity of interest is the pin-pitch-resolved space-time fission-rate distribution.
The MC/DC model uses the canonical cross sections in `data/MGXS-C5G7.h5`, while the OpenMC statepoints are provided by the associated Zenodo record.

### Time-dependent Kobayashi dog-leg

This one-group problem adapts the steady-state Kobayashi shielding benchmark by pulsing the source through a three-dimensional dog-leg void channel.
The quantities of interest are the space-time flux distribution and total neutron density in time.
The OpenMC statepoints are provided by the associated Zenodo record.

## References

- I. Variansyah, [*Four-Phase C5G7 Transient Benchmark for Neutron Transport*](https://doi.org/10.5281/zenodo.15719118), Zenodo, 2025.
- I. Variansyah, [*Time-Dependent Kobayashi Dog-Leg Benchmark for Neutron Transport*](https://doi.org/10.5281/zenodo.15069882), Zenodo, 2025.
- J. Hou, K. N. Ivanov, V. F. Boyarinov, and P. A. Fomichenko, [*OECD/NEA Benchmark for Time-Dependent Neutron Transport Calculations Without Spatial Homogenization*](https://doi.org/10.1016/j.nucengdes.2017.02.008), Nuclear Engineering and Design, vol. 317, pp. 177–189, 2017.
- K. Kobayashi, N. Sugimura, and Y. Nagaya, [*3D Radiation Transport Benchmark Problems and Results for Simple Geometries with Void Region*](https://doi.org/10.1016/S0149-1970(01)00007-5), Progress in Nuclear Energy, vol. 39, no. 2, pp. 119–144, 2001.
