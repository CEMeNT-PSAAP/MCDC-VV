import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',5.7551e-05],
	['U238',0.00051262],
	['H1',0.058561],
	['N14',0.0025144],
	['O16',0.037263871638],
	['O17',1.4128362000000001e-05]])
# Material Name: Stainless steel
m2 = mcdc.material(nuclides=[
	['C0',4.3736e-05],
	['Si28',0.00098012480936],
	['Si29',4.976794132e-05],
	['Si30',3.2807249319999995e-05],
	['Mn55',0.0011561],
	['P31',1.3170000000000001e-05],
	['S32',1.88009591868e-06],
	['S33',1.4810585579999998e-08],
	['S34',8.300507418e-08],
	['S36',2.8842156e-10],
	['Ni58',0.0056778176907],
	['Ni60',0.0021870852093],
	['Ni61',9.507107969999999e-05],
	['Ni62',0.0003031282035],
	['Ni64',7.71978168e-05],
	['Cr50',0.0007288737500000001],
	['Cr52',0.014055604750000002],
	['Cr53',0.0015937927500000002],
	['Cr54',0.00039672875000000004],
	['Fe54',0.00347315745],
	['Fe56',0.054521144339999994],
	['Fe57',0.00125913099],
	['Fe58',0.00016756722000000002]])
# Material Name: Water at 25 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066658],
	['O16',0.033316368309],
	['O17',1.2631690999999998e-05]])
# Material Name: Air
m4 = mcdc.material(nuclides=[
	['N14',3.9016e-05],
	['O16',1.0405054989e-05],
	['O17',3.945011e-09]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=29.5, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=29.8, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=59.8, bc='vacuum')
s4 = mcdc.surface('plane-z', z=-32.0, bc='vacuum')
s5 = mcdc.surface('plane-z', z=-2.0, bc='interface')
s6 = mcdc.surface('plane-z', z=0.0, bc='interface')
s7 = mcdc.surface('plane-z', z=130.33, bc='interface')
s8 = mcdc.surface('plane-z', z=150.0, bc='interface')
s9 = mcdc.surface('plane-z', z=152.5, bc='interface')
s10 = mcdc.surface('plane-z', z=172.5, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s4 & -s5 & -s3, fill=m3)
c2 = mcdc.cell(+s5 & -s6 & -s1, fill=m2)
c3 = mcdc.cell(+s6 & -s7 & -s1, fill=m1)
c4 = mcdc.cell(+s7 & -s8 & -s1, fill=m4)
c5 = mcdc.cell(+s8 & -s9 & -s1, fill=m2)
c6 = mcdc.cell(+s5 & -s9 & +s1 & -s2, fill=m2)
c7 = mcdc.cell(+s5 & -s9 & +s2 & -s3, fill=m3)
c8 = mcdc.cell(+s9 & -s10 & -s3, fill=m3)
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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

