import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium-Gallium alloy
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.037028],
	['Pu240',0.0019931],
	['Pu240',0.00013594],
	['Ga69',0.00077419104],
	['Ga71',0.00051380896]])
# Material Name: Nickel coating
m2 = mcdc.material(nuclides=[
	['Ni58',0.08824127778],
	['Ni60',0.033990382220000004],
	['Ni61',0.00147753838],
	['Ni62',0.004711038900000001],
	['Ni64',0.0011997627200000002]])
# Material Name: Air
m3 = mcdc.material(nuclides=[
	['N14',3.9786725421e-05],
	['N15',1.4627457899999999e-07],
	['O16',8.7365875779e-06],
	['O17',3.3124221000000003e-09]])
# Material Name: Tamper
m4 = mcdc.material(nuclides=[
	['Fe54',0.0050169973],
	['Fe56',0.07875612836],
	['Fe57',0.00181882246],
	['Fe58',0.00024205187999999997]])
# Material Name: Polyethylene
# S(a,b): c_H_in_CH2 (Not Implemented)
m5 = mcdc.material(nuclides=[
	['C0',0.041216],
	['H1',0.08241816219606],
	['H2',1.283780394e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.295, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.308, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.335, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.335, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.342, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.8412, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
c4 = mcdc.cell(+s3 & -s4, fill=m4)
c5 = mcdc.cell(+s4 & -s5, fill=m3)
c6 = mcdc.cell(+s5 & -s6, fill=m5)
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

