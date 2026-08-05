import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['Np237',0.051876]])
m2 = mcdc.material(nuclides=[
	['Ni58',0.062169186618],
	['Ni60',0.023947459382000002],
	['Ni61',0.0010409794779999999],
	['Ni62',0.0033190980900000004],
	['Ni64',0.0008452764320000001]])
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.044482],
	['U238',0.0027038]])
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.0003505],
	['U238',0.047717]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.6921, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.7062, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.7266, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.1156, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=24.1242, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=mvoid)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
c5 = mcdc.cell(+s4 & -s5, fill=m4)
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
mcdc.source(x=[-25.0,25.0], y=[-25.0,25.0], z=[-25.0,25.0], prob=1.0)

mcdc.run()

