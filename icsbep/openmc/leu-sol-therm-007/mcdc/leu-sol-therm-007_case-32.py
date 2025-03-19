import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',6.897e-05],
	['U238',0.00061432],
	['H1',0.058085],
	['N14',0.0026828366399000003],
	['N15',9.8633601e-06],
	['O16',0.037811663945999996],
	['O17',1.4336053999999999e-05]])
# Material Name: Stainless Steel
m2 = mcdc.material(nuclides=[
	['C0',4.373600000000001e-05],
	['Si28',0.00098012480936],
	['Si29',4.976794132e-05],
	['Si30',3.2807249319999995e-05],
	['Mn55',0.0011561],
	['P31',4.3169999999999995e-05],
	['S32',2.83050331868e-06],
	['S33',2.2297485580000004e-08],
	['S34',1.2496497418e-07],
	['S36',4.3422156e-10],
	['Ni58',0.0056778176907],
	['Ni60',0.0021870852093],
	['Ni61',9.50710797e-05],
	['Ni62',0.0003031282035],
	['Ni64',7.71978168e-05],
	['Cr50',0.0007288737500000001],
	['Cr52',0.014055604750000002],
	['Cr53',0.0015937927500000002],
	['Cr54',0.00039672875000000004],
	['Fe54',0.00347315745],
	['Fe56',0.05452114434],
	['Fe57',0.00125913099],
	['Fe58',0.00016756722000000002]])
# Material Name: Air
m3 = mcdc.material(nuclides=[
	['N14',3.8873084392e-05],
	['N15',1.4291560800000001e-07],
	['O16',1.0405054989e-05],
	['O17',3.945011e-09]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=29.5, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=29.8, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-2.0, bc='vacuum')
s4 = mcdc.surface('plane-z', z=0.0, bc='interface')
s5 = mcdc.surface('plane-z', z=63.55, bc='interface')
s6 = mcdc.surface('plane-z', z=150.0, bc='interface')
s7 = mcdc.surface('plane-z', z=152.5, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s2 & +s3 & -s4, fill=m2)
c2 = mcdc.cell(+s1 & -s2 & +s4 & -s6, fill=m2)
c3 = mcdc.cell(-s2 & +s6 & -s7, fill=m2)
c4 = mcdc.cell(-s1 & +s4 & -s5, fill=m1)
c5 = mcdc.cell(-s1 & +s5 & -s6, fill=m3)
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

