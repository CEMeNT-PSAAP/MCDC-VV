import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 36 wt% U-235
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.017118],
	['U238',0.029211],
	['C0',0.0007738900000000001],
	['Fe54',7.047901000000001e-06],
	['Fe56',0.00011063697320000001],
	['Fe57',2.5550902e-06],
	['Fe58',3.400356e-07],
	['W180',1.2104399999999999e-08],
	['W182',2.673055e-06],
	['W183',1.4434497e-06],
	['W184',3.0906568000000003e-06],
	['W186',2.8677341e-06],
	['Cu63',0.000263689695],
	['Cu65',0.00011764030499999999],
	['Ni58',0.00028107590471999997],
	['Ni60',0.00010826993527999999],
	['Ni61',4.70641912e-06],
	['Ni62',1.5006123600000001e-05],
	['Ni64',3.82161728e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=15.324, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

# Simulation Parameters
mcdc.eigenmode(N_inactive=20, N_active=180)
mcdc.setting(N_particle=10000)

# Source Parameters
# Particle: neutron
# Space Type: box
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[-1.0,1.0], prob=1.0)

mcdc.run()

