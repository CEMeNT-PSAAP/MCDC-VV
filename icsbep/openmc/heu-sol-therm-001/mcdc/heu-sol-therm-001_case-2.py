import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Uranyl Nitrate Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.00082771],
	['U238',4.712e-05],
	['O16',0.037120925835],
	['O17',1.4074165e-05],
	['N14',0.002102],
	['H1',0.058433]])
# Material Name: SS-304 Tank
m2 = mcdc.material(nuclides=[
	['C0',0.00026231],
	['Si28',0.00126981823424],
	['Si29',6.447774688e-05],
	['Si30',4.250401888e-05],
	['P31',3.853e-05],
	['S32',2.6879422086800002e-05],
	['S33',2.1174450580000004e-07],
	['S34',1.1867098918000002e-06],
	['S36',4.1235156e-09],
	['Cr50',0.0007379982500000001],
	['Cr52',0.01423156165],
	['Cr53',0.00161374485],
	['Cr54',0.00040169525],
	['Mn55',0.0011209],
	['Fe54',0.0034983494],
	['Fe56',0.054916604079999994],
	['Fe57',0.0012682638800000001],
	['Fe58',0.00016878264000000002],
	['Ni58',0.0051329982599999996],
	['Ni60',0.00197722174],
	['Ni61',8.594846e-05],
	['Ni62',0.00027404130000000004],
	['Ni64',6.979024e-05],
	['Mo100',8.727018719999999e-07],
	['Mo92',1.312008387e-06],
	['Mo94',8.228152809999998e-07],
	['Mo95',1.4216334990000002e-06],
	['Mo96',1.4932838989999995e-06],
	['Mo97',8.58192666e-07],
	['Mo98',2.1756643959999998e-06]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=13.96, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.28, bc='vacuum')
s3 = mcdc.surface('plane-z', z=-0.64, bc='vacuum')
s4 = mcdc.surface('plane-z', z=0.0, bc='interface')
s5 = mcdc.surface('plane-z', z=28.93, bc='interface')
s6 = mcdc.surface('plane-z', z=41.6, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s2 & +s3 & -s4, fill=m2)
c2 = mcdc.cell(+s1 & -s2 & +s4 & -s6, fill=m2)
c3 = mcdc.cell(-s1 & +s4 & -s5, fill=m1)
c4 = mcdc.cell(-s1 & +s5 & -s6, fill=mvoid)
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

