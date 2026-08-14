from pathlib import Path

import numpy as np
import mcdc

SHEM361_DATA = (
    Path(__file__).resolve().parents[3] / "fixed_source" / "data" / "SHEM-361.npz"
)

CAPTURE_FACTOR = 1.0
N_PARTICLE = 10000
N_INACTIVE = 20
N_ACTIVE = 20

simulation = mcdc.Simulation("Infinite SHEM-361 supercritical k-eigenvalue")

# ======================================================================================
# Set model
# ======================================================================================
# The infinite homogeneous medium is modeled with a reflecting slab.

with np.load(SHEM361_DATA) as data:
    SigmaC = data["SigmaC"] * CAPTURE_FACTOR
    SigmaS = data["SigmaS"]
    SigmaF = data["SigmaF"]
    nu_p = data["nu_p"]
    nu_d = data["nu_d"]
    chi_p = data["chi_p"]
    chi_d = data["chi_d"]
    G = int(data["G"])

material = mcdc.Material.multigroup(
    capture=SigmaC,
    scatter=SigmaS,
    fission=SigmaF,
    nu_p=nu_p,
    chi_p=chi_p,
    nu_d=nu_d,
    chi_d=chi_d,
)

left = mcdc.Surface.PlaneX(x=-1.0e10, boundary_condition="reflective")
right = mcdc.Surface.PlaneX(x=1.0e10, boundary_condition="reflective")
cell = mcdc.Cell(region=+left & -right, fill=material)
simulation.set_model([cell])

# ======================================================================================
# Set initial source
# ======================================================================================

source = mcdc.Source(
    position=(0.0, 0.0, 0.0),
    isotropic=True,
    discrete_energy=np.array([[G - 1], [1.0]]),
)
simulation.set_sources([source])

# ======================================================================================
# Set tallies, settings, techniques, and run MC/DC
# ======================================================================================

tally = mcdc.Tally(scores=["flux"], energy="all")
simulation.set_tallies([tally])

# Particle and inactive-cycle counts stay fixed while the study overrides N_active.
simulation.settings.N_particle = N_PARTICLE
simulation.settings.set_eigenmode(N_inactive=N_INACTIVE, N_active=N_ACTIVE)
simulation.settings.census_bank_buffer_ratio = 4.0
simulation.settings.source_bank_buffer_ratio = 4.0

# Keep exactly N_particle source histories after each eigenvalue cycle.
simulation.technique.population_control()

simulation.run()
