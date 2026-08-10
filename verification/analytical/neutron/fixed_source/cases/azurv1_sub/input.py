import numpy as np
import mcdc

simulation = mcdc.Simulation("AZURV1 subcritical")

# ======================================================================================
# Set model
# ======================================================================================
# Infinite medium with isotropic plane surface at the center
# Based on Ganapol LA-UR-01-1854 (AZURV1 benchmark)
# Effective scattering ratio c = 0.9

# Set materials
m = mcdc.Material.multigroup(
    capture=np.array([1.0 / 3.0]),
    scatter=np.array([[1.0 / 3.0]]),
    fission=np.array([1.0 / 3.0]),
    nu_p=np.array([1.7]),
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
# Set tallies, settings, and run MC/DC
# ======================================================================================

# Tallies
mesh = mcdc.MeshStructured(x=np.linspace(-20.5, 20.5, 202))
tally = mcdc.Tally(mesh=mesh, scores=["flux"], time=np.linspace(0.0, 20.0, 21))
simulation.set_tallies([tally])

# Settings
simulation.settings.N_particle = 100
simulation.settings.N_batch = 2

# Run
simulation.run()
