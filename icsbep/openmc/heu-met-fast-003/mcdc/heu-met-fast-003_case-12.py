import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Oralloy
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044917],
	['U238',0.0025993]])
# Material Name: Nickel
m2 = mcdc.material(nuclides=[
	['Ni58',0.062169186618],
	['Ni60',0.023947459382000002],
	['Ni61',0.0010409794779999999],
	['Ni62',0.0033190980900000004],
	['Ni64',0.0008452764320000001]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.4627, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=26.7827, bc='vacuum')

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

