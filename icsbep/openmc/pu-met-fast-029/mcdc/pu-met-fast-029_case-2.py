import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.041923],
	['Pu240',0.0046622],
	['Fe54',1.8291343e-05],
	['Fe56',0.0002871349676],
	['Fe57',6.6311986e-06],
	['Fe58',8.824908e-07],
	['C0',0.0012949],
	['H1',0.00030207294783120005],
	['H2',4.7052168800000004e-08],
	['N14',3.2490549570000004e-05],
	['N15',1.1945043e-07],
	['O16',4.8324678003e-05],
	['O17',1.8321997e-08]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.8, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='vacuum')

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

