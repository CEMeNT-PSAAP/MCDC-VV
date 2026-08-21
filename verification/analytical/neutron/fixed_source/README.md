# Analytical Neutron Fixed-Source Verification

This suite verifies MC/DC neutron transport using multigroup fixed-source cases with analytical reference solutions.
It exercises geometry tracking, surface crossings, material lookup, source sampling, particle transport, and tallying.
Verification checks for the expected $N^{-1/2}$ statistical convergence as the number of source particles increases.

The suite can be executed independently or as part of the top-level MC/DC-VVP workflow.

## Directory layout

```text
cases/              Verification case definitions and processing scripts
data/               Shared multigroup cross-section data
maestro_run_*/      Generated Maestro workflow directories
results/            Generated figures from processed cases

task.yaml           Configure the particle-count study for each case
study.yaml          Generated Maestro study definition

launch.py           Build and launch the Maestro study
run_case.py         Run one case over its particle-count study
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

## Configuration

The `task.yaml` file selects the cases and defines the particle-count range and number of tasks for each case.
An optional `walltime_factor` scales the launch-level walltime for an individual HPC case and defaults to `1.0`.
The base walltime is specified in hours, and the scaled value is rounded up to the scheduler resolution and limited by the platform maximum.
Local execution ignores walltime.
Edit this file to change the study without modifying the launch or processing scripts.

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

## Cases

| Case | Description |
| :--- | :---------- |
| [`slab_absorbium`](cases/slab_absorbium/) | Steady-state flux distribution in a purely absorbing multilayer slab. |
| [`mms_two_group_slab`](cases/mms_two_group_slab/) | Manufactured steady-state two-group slab with positive linear volume sources and isotropic incoming boundary fluxes. |
| [`slab_isobeam_td`](cases/slab_isobeam_td/) | Time-dependent flux propagation from an isotropic planar source. |
| [`reed`](cases/reed/) | Reed's classic one-dimensional transport benchmark. |
| [`azurv1`](cases/azurv1/) | AZURV1 transient benchmark. |
| [`azurv1_sub`](cases/azurv1_sub/) | Subcritical variant of AZURV1. |
| [`azurv1_super`](cases/azurv1_super/) | Supercritical variant of AZURV1. |
| [`azurv1-census`](cases/azurv1-census/) | AZURV1 with time censuses. |
| [`azurv1-census-tally`](cases/azurv1-census-tally/) | AZURV1 using time-census-based tallying. |
| [`azurv1-basic_techniques`](cases/azurv1-basic_techniques/) | AZURV1 with implicit capture, weighted emission, and global weight roulette. |
| [`azurv1-weight_windows`](cases/azurv1-weight_windows/) | AZURV1 with spatial weight windows derived from the time-averaged analytical solution. |
| [`inf_shem361`](cases/inf_shem361/) | Infinite homogeneous SHEM-361 steady-state spectrum. |
| [`inf_shem361_td`](cases/inf_shem361_td/) | Time-dependent SHEM-361 spectrum evolution. |
| [`inf_shem361_td-census`](cases/inf_shem361_td-census/) | Time-dependent SHEM-361 spectrum evolution with time censuses. |
| [`inf_shem361-weight_windows`](cases/inf_shem361-weight_windows/) | Infinite homogeneous SHEM-361 with energy-dependent weight windows derived from the analytical spectrum. |

### MMS two-group slab

This steady-state, one-dimensional problem uses a 10 cm slab with vacuum boundaries, two energy groups, and isotropic scattering.
Both groups have $\Sigma_t=1$ cm$^{-1}$ and $\Sigma_c=0.6$ cm$^{-1}$, and every entry of the outgoing-by-incoming scattering matrix is $0.2$ cm$^{-1}$.
We manufacture the right-hand sides (sum of in-scattering and non-homogeneous source) of the group-wise transport equation:

$$
R_1(x)=0.5+0.01x,
\qquad
R_2(x)=0.6-0.01x.
$$

The equal-and-opposite slopes yield isotropic incoming boundary fluxes and the positive, angle-integrated volume sources

$$
q_1(x)=0.56+0.02x,
\qquad
q_2(x)=0.76-0.02x.
$$

MC/DC samples these sources with piecewise-linear spatial distributions and the incoming fluxes with white half-space boundary sources.
The analytical scalar flux is $\phi_g(x)=2R_g(x)+R'_g(x)[E_3(x)-E_3(10-x)]$.

### SHEM-361 multigroup data

The SHEM-361 cases use `data/SHEM-361.npz` as their multigroup cross-section dataset.
The dataset was generated by homogenizing a continuous-energy calculation of an infinite lattice of borated PWR fuel pin cells onto the SHEM-361 energy-group structure.

## References

- W. H. Reed, *New Difference Schemes for the Neutron Transport Equation*, Nuclear Science and Engineering, 1971.
- B. D. Ganapol, R. S. Baker, J. A. Dahl, and R. E. Alcouffe, [*Homogeneous Infinite Media Time-Dependent Analytical Benchmarks*](https://www.osti.gov/biblio/975281), Los Alamos National Laboratory, LA-UR-01-1854, 2001.
- A. Hébert and A. Santamarina, *Refinement of the Santamarina-Hfaiedh Energy Mesh Between 22.5 eV and 11.4 keV*, PHYSOR 2008, vol. 2, pp. 929–938, 2008.
