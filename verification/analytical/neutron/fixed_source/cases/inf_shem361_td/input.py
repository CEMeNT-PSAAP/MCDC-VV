from pathlib import Path

import numpy as np
import mcdc

SHEM361_DATA = Path(__file__).resolve().parents[2] / "data" / "SHEM-361.npz"

simulation = mcdc.Simulation("Infinite SHEM-361 time-dependent")

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
    speed = data["v"]
    lamd = data["lamd"]

# Set material
m = mcdc.Material.multigroup(
    capture=SigmaC,
    scatter=SigmaS,
    fission=SigmaF,
    nu_p=nu_p,
    chi_p=chi_p,
    nu_d=nu_d,
    chi_d=chi_d,
    decay_rate=lamd,
    speed=speed,
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
    discrete_energy=np.array([[360], [1.0]]),
)
simulation.set_sources([source])

# ======================================================================================
# Set tallies, settings, and run MC/DC
# ======================================================================================

# Tallies
tally = mcdc.Tally(
    scores=["flux"],
    time=np.insert(np.logspace(-8, 1, 100), 0, 0.0),
    energy="all",
)
simulation.set_tallies([tally])

# Settings
simulation.settings.N_particle = 50
simulation.settings.N_batch = 2
simulation.settings.active_bank_buffer = 1000

# Run
simulation.run()
