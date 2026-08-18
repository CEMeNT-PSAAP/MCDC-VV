from pathlib import Path

import numpy as np
import mcdc

REFERENCE_DATA = Path(__file__).resolve().parent / "reference.npz"
WINDOW_FLOOR = 1.0e-3
WINDOW_WIDTH = 2.5

simulation = mcdc.Simulation("AZURV1 weight windows")

# ======================================================================================
# Set model
# ======================================================================================
# Infinite medium with isotropic plane surface at the center
# Based on Ganapol LA-UR-01-1854 (AZURV1 benchmark)
# Effective scattering ratio c = 1.0

# Set materials
m = mcdc.Material.multigroup(
    capture=np.array([1.0 / 3.0]),
    scatter=np.array([[1.0 / 3.0]]),
    fission=np.array([1.0 / 3.0]),
    nu_p=np.array([2.0]),
)

# Set surfaces
s1 = mcdc.Surface.PlaneX(x=-1e10, boundary_condition="reflective")
s2 = mcdc.Surface.PlaneX(x=1e10, boundary_condition="reflective")

# Set cells
cell = mcdc.Cell(region=+s1 & -s2, fill=m)
simulation.set_model([cell])

# ======================================================================================
# Set source
# ======================================================================================
# Isotropic pulse at x=t=0

source = mcdc.Source(
    position=[0.0, 0.0, 0.0],
    isotropic=True,
    energy=0,
    time=0.0,
)
simulation.set_sources([source])

# ======================================================================================
# Set tallies, settings, techniques, and run MC/DC
# ======================================================================================

# Load the analytical grid and time-dependent cell-average flux.
with np.load(REFERENCE_DATA) as data:
    x = data["x"]
    time = data["t"]
    phi = data["phi"]

# Tallies
mesh = mcdc.MeshStructured(x=x)
tally = mcdc.Tally(mesh=mesh, scores=["flux"], time=time)
simulation.set_tallies([tally])

# Settings
simulation.settings.N_particle = 100
simulation.settings.N_batch = 2
simulation.settings.active_bank_buffer = 10_000

# Average the analytical flux over the complete simulation time.
phi_average = np.average(phi, axis=0, weights=np.diff(time))

# Convert the normalized analytical profile into lower, target, and upper weights.
target_weight = phi_average / np.max(phi_average)
target_weight = WINDOW_FLOOR + (1.0 - WINDOW_FLOOR) * target_weight
weight_windows = np.empty((1, len(x) - 1, 1, 1, 3))
weight_windows[0, :, 0, 0, 0] = target_weight / WINDOW_WIDTH
weight_windows[0, :, 0, 0, 1] = target_weight
weight_windows[0, :, 0, 0, 2] = target_weight * WINDOW_WIDTH

# Techniques
simulation.technique.weight_windows(weight_windows, mesh=mesh)

# Run
simulation.run()
