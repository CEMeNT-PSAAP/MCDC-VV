from pathlib import Path

import numpy as np
import mcdc

from reference import reference

SHEM361_DATA = Path(__file__).resolve().parents[2] / "data" / "SHEM-361.npz"
WINDOW_FLOOR = 1.0e-3
WINDOW_WIDTH = 2.5

simulation = mcdc.Simulation("Infinite SHEM-361 weight windows")

# ======================================================================================
# Set model
# ======================================================================================
# The infinite homogeneous medium is modeled with a reflecting slab

# Load material data
with np.load(SHEM361_DATA) as data:
    SigmaC = data["SigmaC"] * 1.5  # /cm
    SigmaS = data["SigmaS"]
    SigmaF = data["SigmaF"]
    nu_p = data["nu_p"]
    nu_d = data["nu_d"]
    chi_p = data["chi_p"]
    chi_d = data["chi_d"]
    G = int(data["G"])

# Set material
m = mcdc.Material.multigroup(
    capture=SigmaC,
    scatter=SigmaS,
    fission=SigmaF,
    nu_p=nu_p,
    chi_p=chi_p,
    nu_d=nu_d,
    chi_d=chi_d,
)

# Set surfaces
s1 = mcdc.Surface.PlaneX(x=-1e10, boundary_condition="reflective")
s2 = mcdc.Surface.PlaneX(x=1e10, boundary_condition="reflective")

# Set cells
c = mcdc.Cell(region=+s1 & -s2, fill=m)
simulation.set_model([c])

# ======================================================================================
# Set source
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

# Tallies
tally = mcdc.Tally(scores=["flux"], energy="all")
simulation.set_tallies([tally])

# Settings
simulation.settings.N_particle = 40
simulation.settings.N_batch = 2
simulation.settings.active_bank_buffer = 10_000

# Normalize the analytical group spectrum into target weights.
phi = reference()
target_weight = phi / np.max(phi)
target_weight = WINDOW_FLOOR + (1.0 - WINDOW_FLOOR) * target_weight

# Center each standard multigroup coordinate in its corresponding window bin.
group_bounds = np.arange(G + 1, dtype=float) - 0.5
weight_windows = np.empty((G, 1, 1, 1, 3))
weight_windows[:, 0, 0, 0, 0] = target_weight / WINDOW_WIDTH
weight_windows[:, 0, 0, 0, 1] = target_weight
weight_windows[:, 0, 0, 0, 2] = target_weight * WINDOW_WIDTH

# Techniques
simulation.technique.weight_windows(weight_windows, energy=group_bounds)

# Run
simulation.run()
