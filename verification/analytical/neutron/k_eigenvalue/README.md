# Analytical Neutron $k$-Eigenvalue Verification

This suite verifies MC/DC neutron $k$-eigenvalue calculations using one-group and multigroup problems with analytical and semi-analytical reference solutions.
It compares estimated multiplication factors and fundamental-mode flux shapes against dominant solutions of the corresponding transport eigenvalue problems.
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

Each case contains a common set of files:

```text
input.py            Define and run the MC/DC model
reference.py        Generate the analytical reference solution
process.py          Evaluate convergence across the study
plot.py             Inspect one MC/DC result against the reference
```

The multigroup cases use the SHEM-361 dataset in the neighboring fixed-source suite at `../fixed_source/data/SHEM-361.npz`.

## Configuration

The `task.yaml` file selects the cases and defines the minimum and maximum active-cycle counts and the number of tasks for each case.
The active-cycle counts are geometrically spaced so that convergence can be assessed efficiently over a range of tens to thousands of cycles.
An optional `walltime_factor` scales the launch-level walltime for an individual HPC case and defaults to `1.0`.
The base walltime is specified in hours, and the scaled value is rounded up to the scheduler resolution and limited by the platform maximum.
Local execution ignores walltime.

The fixed particle and inactive-cycle counts are defined in each case's `input.py` and should be tuned with a preliminary source-convergence and variance study before running the active-cycle campaign.
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

Use `--walltime HOURS` to set the base walltime and `--rewrite` to replace existing case output.

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

Each case's `plot.py` can inspect one result interactively, showing its flux shape and the cycle-by-cycle multiplication factor:

```bash
python cases/inf_shem361_subcritical/plot.py cases/inf_shem361_subcritical/output_320.h5
```

## Cases

| Case | Description |
| :--- | :---------- |
| [`one_group_slab`](cases/one_group_slab/) | Homogeneous finite one-group slab with vacuum boundaries and a semi-analytical, leakage-dependent fundamental eigenpair. |
| [`kornreich`](cases/kornreich/) | Kornreich-Parsons seven-region, one-group slab with a published Green's-function eigenvalue. |
| [`inf_shem361_subcritical`](cases/inf_shem361_subcritical/) | Infinite homogeneous SHEM-361 with the capture cross section increased by 50%. |
| [`inf_shem361_supercritical`](cases/inf_shem361_supercritical/) | Infinite homogeneous SHEM-361 with the original capture cross section. |

### One-group finite slab

This case uses a homogeneous 10 cm slab with vacuum boundaries, $(\Sigma_c,\Sigma_s,\Sigma_f)=(0.25,0.50,0.25)$ cm$^{-1}$, and $\nu_p=2.519421$.
A refined $E_1$ collision-integral eigenproblem supplies the cell-averaged fundamental flux and $k=1.2$.

### Kornreich-Parsons slab

This case alternates four beryllium-reflector regions with three uranium-fuel regions, each one mean free path thick, with vacuum boundaries.
The reflector has $(\Sigma_t,\Sigma_s,\nu\Sigma_f)=(0.371,0.334,0)$ cm$^{-1}$, while the fuel has $(0.415,0.334,0.178)$ cm$^{-1}$.
The published Green's-function reference is $k_\mathrm{eff}=1.17361$.
MC/DC assigns all non-scattering fuel removal to fission to preserve the published $\nu\Sigma_f$, and a refined collision-integral solution supplies the reference flux shape.

### SHEM-361 cases

For each multigroup case, the analytical multiplication factor and spectrum are obtained from

$$
\left[\mathrm{diag}(\Sigma_t)-\Sigma_s\right]\phi
= \frac{1}{k}\nu\Sigma_f\phi.
$$

SciPy solves the generalized eigenvalue problem, and the dominant real eigenpair supplies $k$ and the normalized fundamental-mode spectrum.

## References

- D. E. Kornreich and D. K. Parsons, [*The Green's Function Method for Effective Multiplication Benchmark Calculations in Multi-Region Slab Geometry*](https://doi.org/10.1016/j.anucene.2004.03.012), Annals of Nuclear Energy, vol. 31, no. 13, pp. 1477–1494, 2004.
- A. Hébert and A. Santamarina, *Refinement of the Santamarina-Hfaiedh Energy Mesh Between 22.5 eV and 11.4 keV*, PHYSOR 2008, vol. 2, pp. 929–938, 2008.
