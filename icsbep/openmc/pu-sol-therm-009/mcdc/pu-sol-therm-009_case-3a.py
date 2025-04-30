import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu238',9.7592e-10],
	['Pu239',2.3201e-05],
	['Pu240',5.9809e-07],
	['Pu242',3.2939e-09],
	['N14',0.00076076],
	['H1',0.065121],
	['O16',0.03451]])
# Material Name: 1100 Aluminum
m2 = mcdc.material(nuclides=[
	['Al27',0.059881],
	['Si28',0.00034835150136],
	['Si29',1.7688295320000002e-05],
	['Si30',1.166020332e-05],
	['Cu63',3.5518206e-05],
	['Cu65',1.5845794e-05],
	['Zn64',1.2271848600000001e-05],
	['Zn66',6.9208534e-06],
	['Zn67',1.0083032e-06],
	['Zn68',4.604751e-06],
	['Zn70',1.522438e-07],
	['Mn55',1.4853000000000002e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=60.964, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=61.734, bc='vacuum')

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

