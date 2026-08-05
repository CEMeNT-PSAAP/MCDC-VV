import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041018],
	['U238',0.0040942],
	['C0',0.0004045000000000001],
	['Fe54',8.3413995e-06],
	['Fe56',0.0001309421334],
	['Fe57',3.0240248999999995e-06],
	['Fe58',4.024422e-07],
	['W180',1.4873999999999998e-08],
	['W182',3.2846750000000004e-06],
	['W183',1.7737245000000002e-06],
	['W184',3.7978280000000002e-06],
	['W186',3.5238985000000003e-06],
	['Cu63',0.000524786265],
	['Cu65',0.00023412373500000003],
	['Ni58',0.00023973961104],
	['Ni60',9.234726896e-05],
	['Ni61',4.01427184e-06],
	['Ni62',1.2799255200000001e-05],
	['Ni64',3.25959296e-06]])
# Material Name: Polyethylene
# S(a,b): c_H_in_CH2 (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.039047],
	['H1',0.078094]])
# Material Name: Fe
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=2.0, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 1.96], radius=7.55, bc='interface')
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=8.5, bc='interface')
s5 = mcdc.surface('plane-z', z=1.66, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=18.0, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 1.96], radius=18.0, bc='interface')
s8 = mcdc.surface('plane-z', z=0.0, bc='interface')
s9 = mcdc.surface('plane-z', z=1.96, bc='interface')
s10 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=21.5, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3 & +s9, fill=mvoid)
c4 = mcdc.cell(+s2 & -s4 & +s5 & -s9, fill=mvoid)
c5 = mcdc.cell(+s2 & -s5 & +s8 & -s10, fill=mvoid)
c6 = mcdc.cell(+s2 & -s6 & -s8, fill=m2)
c7 = mcdc.cell(+s3 & -s7 & +s9, fill=m2)
c8 = mcdc.cell(+s4 & +s5 & -s9 & -s10, fill=m3)
c9 = mcdc.cell(+s6 & -s8 & -s10, fill=mvoid)
c10 = mcdc.cell(+s7 & +s9 & -s10, fill=mvoid)
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

