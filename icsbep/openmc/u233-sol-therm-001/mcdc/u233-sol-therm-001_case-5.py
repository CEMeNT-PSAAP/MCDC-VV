import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: UO2(NO3)2 Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U233',5.0042999999999995e-05],
	['U235',2.0314e-08],
	['U238',3.2091e-07],
	['N14',0.00013586],
	['H1',0.066329],
	['O16',0.033653240586],
	['O17',1.2759414e-05],
	['B10',1.0114e-06],
	['B11',4.0708e-06],
# Material Name: Type 1100 Aluminum
m2 = mcdc.material(nuclides=[
	['Al27',0.059881],
	['Si28',0.00020096847272000002],
	['Si29',1.0204605640000001e-05],
	['Si30',6.7269216400000005e-06],
	['Fe54',6.404951000000001e-06],
	['Fe56',0.0001005440332],
	['Fe57',2.3220002000000003e-06],
	['Fe58',3.090156e-07],
	['Cu63',3.5518206e-05],
	['Cu65',1.5845794e-05],
	['Mn55',1.4853e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=34.595, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=34.915, bc='vacuum')

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

