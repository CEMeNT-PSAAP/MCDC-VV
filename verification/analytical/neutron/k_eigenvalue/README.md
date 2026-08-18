# Analytical Neutron $k$-Eigenvalue Verification

This suite verifies MC/DC neutron $k$-eigenvalue calculations using infinite homogeneous multigroup problems with analytical reference solutions.
It compares the estimated multiplication factor and fundamental-mode energy spectrum against the dominant solution of the corresponding generalized matrix eigenvalue problem.
Verification checks for the expected $N_\mathrm{active}^{-1/2}$ statistical convergence as the number of active cycles increases.

The number of particles per cycle and the number of inactive cycles are fixed in each case input so that the study isolates convergence with active cycles.
The suite can be executed independently or as part of the top-level MC/DC-VVP workflow.

## Directory layout

```text
cases/              Verification case definitions and processing scripts
maestro_run_*/      Generated Maestro workflow directories
results/            Generated figures from processed cases

task.yaml           Configure the active-cycle study for each case
study.yaml          Generated Maestro study definition

launch.py           Build and launch the Maestro study
run_case.py         Run one case over its active-cycle study
process.py          Process a completed Maestro study

cleanup.py          Remove generated outputs and figures
util.py             Provide shared processing and plotting utilities
```

The cases use the SHEM-361 dataset in the neighboring fixed-source suite at `../fixed_source/data/SHEM-361.npz`.

## Configuration

The `task.yaml` file selects the cases and defines the minimum and maximum active-cycle counts and the number of tasks for each case.
The active-cycle counts are geometrically spaced so that convergence can be assessed efficiently over a range of tens to hundreds of cycles.

The fixed particle and inactive-cycle counts are defined in each case's `input.py` and should be tuned with a preliminary source-convergence and variance study before running the active-cycle campaign.
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

Use `--walltime HOURS` to limit the requested walltime and `--rewrite` to replace existing case output.

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

Each case's `plot.py` can inspect one result interactively, showing both the energy spectrum and the cycle-by-cycle multiplication factor:

```bash
python cases/inf_shem361_subcritical/plot.py cases/inf_shem361_subcritical/output_320.h5
```

## Cases

| Case | Description |
| :--- | :---------- |
| [`inf_shem361_subcritical`](cases/inf_shem361_subcritical/) | Infinite homogeneous SHEM-361 with the capture cross section increased by 50%. |
| [`inf_shem361_supercritical`](cases/inf_shem361_supercritical/) | Infinite homogeneous SHEM-361 with the original capture cross section. |

For each case, the analytical multiplication factor and spectrum are obtained from

$$
\left[\operatorname{diag}(\Sigma_t)-\Sigma_s\right]\phi
= \frac{1}{k}\nu\Sigma_f\phi.
$$

SciPy solves the generalized eigenvalue problem, and the dominant real eigenpair supplies $k$ and the normalized fundamental-mode spectrum.

## References

- A. Hébert and A. Santamarina, *Refinement of the Santamarina-Hfaiedh Energy Mesh Between 22.5 eV and 11.4 keV*, PHYSOR 2008, vol. 2, pp. 929–938, 2008.
