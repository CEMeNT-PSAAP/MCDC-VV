import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: 98% Pu-239 in delta phase
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.03662],
	['Pu240',0.0006694399999999999],
	['Ga69',0.001320091896],
	['Ga71',0.0008761081040000001],
	['Fe54',8.256647000000002e-06],
	['Fe56',0.0001296117004],
	['Fe57',2.9932994e-06],
	['Fe58',3.9835320000000003e-07],
	['C0',0.00028972],
	['Ni58',0.0013443826212],
	['Ni60',0.0005178537788],
	['Ni61',2.25107452e-05],
	['Ni62',7.1774106e-05],
	['Ni64',1.8278748800000003e-05]])
# Material Name: Polyethylene
# S(a,b): c_H_in_CH2 (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.038814],
	['H1',0.077628]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.0, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
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

