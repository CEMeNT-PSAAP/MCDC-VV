import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041011],
	['U238',0.0040989],
	['C0',0.00039946],
	['Fe54',7.911792e-06],
	['Fe56',0.0001241982144],
	['Fe57',2.8682784e-06],
	['Fe58',3.8171520000000006e-07],
	['W180',1.4939999999999997e-08],
	['W182',3.29925e-06],
	['W183',1.7815949999999997e-06],
	['W184',3.81468e-06],
	['W186',3.5395349999999996e-06],
	['Cu63',0.00050432478],
	['Cu65',0.00022499521999999998],
	['Ni58',0.00023039265267000002],
	['Ni60',8.874683733000001e-05],
	['Ni61',3.85776357e-06],
	['Ni62',1.230023835e-05],
	['Ni64',3.1325080799999997e-06]])
# Material Name: BeO Reflector
# S(a,b): c_Be_in_BeO (Not Implemented)
# S(a,b): c_O_in_BeO (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.067634],
	['O16',0.067608366714],
	['O17',2.5633286e-05]])
# Material Name: Fe
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
# Material Name: Copper
m4 = mcdc.material(nuclides=[
	['Cu63',0.0569553975],
	['Cu65',0.025409602499999996]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.75, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 2.74], radius=7.55, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 2.74], radius=8.35, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 2.74], radius=11.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.15, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=2.54, bc='interface')
s12 = mcdc.surface('plane-z', z=2.74, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.7, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s16 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s17 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s18 = mcdc.surface('cylinder-y', center=[0.0, 2.74], radius=0.6, bc='interface')
s19 = mcdc.surface('plane-z', z=-0.15, bc='interface')
s20 = mcdc.surface('plane-z', z=2.89, bc='interface')
s21 = mcdc.surface('plane-z', z=-14.15, bc='vacuum')
s22 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s3 & -s17, fill=mvoid)
c2 = mcdc.cell(-s16 & +s6 & -s8 & +s12, fill=mvoid)
c3 = mcdc.cell(+s1 & -s3 & +s17, fill=m1)
c4 = mcdc.cell(+s3 & -s4 & +s12, fill=mvoid)
c5 = mcdc.cell(+s3 & -s5 & -s10 & +s17, fill=m1)
c6 = mcdc.cell(+s4 & -s6 & +s12 & +s18, fill=m1)
c7 = mcdc.cell(+s5 & -s7 & -s19, fill=m2)
c8 = mcdc.cell(+s6 & -s8 & +s20 & +s16, fill=m2)
c9 = mcdc.cell(+s3 & +s10 & -s11 & -s15, fill=mvoid)
c10 = mcdc.cell(+s2 & +s11 & -s12 & -s15, fill=m3)
c11 = mcdc.cell(+s7 & -s15 & -s10 & +s13 & +s21, fill=mvoid)
c12 = mcdc.cell(+s8 & -s15 & +s12 & -s22, fill=mvoid)
c13 = mcdc.cell(+s7 & -s9 & -s13 & -s10, fill=m4)
c14 = mcdc.cell(+s9 & +s21 & -s14 & -s10, fill=m3)
c15 = mcdc.cell(+s9 & -s15 & +s14 & -s13 & -s10 & +s21, fill=mvoid)
c16 = mcdc.cell(+s3 & -s2 & +s11 & -s12, fill=mvoid)
c17 = mcdc.cell(+s5 & -s7 & +s19 & -s10, fill=mvoid)
c18 = mcdc.cell(+s6 & -s8 & +s12 & -s20, fill=mvoid)
c19 = mcdc.cell(-s10 & +s3 & -s5 & -s17, fill=mvoid)
c20 = mcdc.cell(+s4 & -s6 & +s12 & -s18, fill=mvoid)
c21 = mcdc.cell(-s1, fill=mvoid)
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

