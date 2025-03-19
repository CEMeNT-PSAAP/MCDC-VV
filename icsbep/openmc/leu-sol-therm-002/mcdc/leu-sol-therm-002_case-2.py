import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranium Oxyfluoride Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',6.1604e-05],
	['U238',0.0011828],
	['F19',0.0024893],
	['O16',0.033318367551],
	['O17',1.2632448999999999e-05],
	['H1',0.061683]])
# Material Name: Type 1100 Aluminum
m2 = mcdc.material(nuclides=[
	['Al27',0.059699],
	['Si28',0.000509126279536],
	['Si29',2.5851979831999998e-05],
	['Si30',1.7041740632e-05],
	['Cu63',3.5518206e-05],
	['Cu65',1.5845794e-05],
	['Zn64',1.2271848600000001e-05],
	['Zn66',6.9208534e-06],
	['Zn67',1.0083032e-06],
	['Zn68',4.604751e-06],
	['Zn70',1.522438e-07],
	['Mn55',1.4853e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=34.4995, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=34.6583, bc='vacuum')

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

