import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 98% Pu-239 in delta phase
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.036623],
	['Pu240',0.0006695099999999999],
	['Ga69',0.0013211137319999997],
	['Ga71',0.000876786268],
	['Fe54',8.327371500000001e-06],
	['Fe56',0.00013072192380000002],
	['Fe57',3.0189393000000003e-06],
	['Fe58',4.0176539999999997e-07],
	['C0',0.00029311],
	['Ni58',0.0012678641855999998],
	['Ni60',0.0004883790144],
	['Ni61',2.1229497600000002e-05],
	['Ni62',6.7688928e-05],
	['Ni64',1.72383744e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.67, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
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

