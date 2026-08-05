import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: IEU Flouride Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U232',4.5608e-08],
	['U233',0.0022379],
	['U235',8.959799999999998e-07],
	['U238',7.1284e-06],
	['H1',0.055183],
	['O16',0.032030855703],
	['O17',1.2144297e-05],
	['F19',0.0047182]])
# Material Name: 347 Stainless steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.0035799456],
	['Fe56',0.05619748991999999],
	['Fe57',0.00129784512],
	['Fe58',0.00017271936],
	['Cr50',0.0007246590999999999],
	['Cr52',0.013974329419999999],
	['Cr53',0.0015845767799999998],
	['Cr54',0.00039443469999999995],
	['Ni58',0.0061448933016],
	['Ni60',0.0023670018984],
	['Ni61',0.0001028919336],
	['Ni62',0.000328064508],
	['Ni64',8.35483584e-05]])
# Material Name: Beryllium reflector
# S(a,b): c_Be (Not Implemented)
m3 = mcdc.material(nuclides=[
	['Be9',0.12161]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.8726, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.9209, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=15.9209, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
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

