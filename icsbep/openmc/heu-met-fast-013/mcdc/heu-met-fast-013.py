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
	['Fe58',3.8171519999999996e-07],
	['W180',1.4808e-08],
	['W182',3.2701e-06],
	['W183',1.7658540000000001e-06],
	['W184',3.780976e-06],
	['W186',3.508262e-06],
	['Cu63',0.00050432478],
	['Cu65',0.00022499521999999998],
	['Ni58',0.00023039265267],
	['Ni60',8.874683733000001e-05],
	['Ni61',3.85776357e-06],
	['Ni62',1.230023835e-05],
	['Ni64',3.13250808e-06]])
# Material Name: Steel
m2 = mcdc.material(nuclides=[
	['Fe54',0.00482533975],
	['Fe56',0.0757475147],
	['Fe57',0.0017493404500000002],
	['Fe58',0.0002328051],
	['C0',0.00077554],
	['Si28',0.0003211898606],
	['Si29',1.6309104699999998e-05],
	['Si30',1.0751034699999998e-05],
	['Cr50',2.9190144500000005e-06],
	['Cr52',5.629028809000001e-05],
	['Cr53',6.38286681e-06],
	['Cr54',1.5888306500000002e-06],
	['Mn55',0.00044508]])
# Material Name: Pure Fe
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
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.2], radius=7.55, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.2], radius=8.35, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.2], radius=12.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.15, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=0.2, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.7, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s14 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s16 = mcdc.surface('cylinder-y', center=[0.0, 0.2], radius=0.6, bc='interface')
s17 = mcdc.surface('plane-z', z=-15.15, bc='vacuum')
s18 = mcdc.surface('plane-z', z=13.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s3 & -s14, fill=mvoid)
c3 = mcdc.cell(+s1 & -s3 & +s14, fill=m1)
c4 = mcdc.cell(+s3 & -s4 & +s11, fill=mvoid)
c5 = mcdc.cell(+s3 & -s5 & -s10 & +s14, fill=m1)
c6 = mcdc.cell(+s4 & -s6 & +s11 & +s16, fill=m1)
c7 = mcdc.cell(+s5 & -s7 & -s10, fill=m2)
c8 = mcdc.cell(+s6 & -s8 & +s11, fill=m2)
c9 = mcdc.cell(-s2 & +s3 & +s10 & -s11, fill=mvoid)
c10 = mcdc.cell(+s2 & +s10 & -s11 & -s15, fill=m3)
c11 = mcdc.cell(+s7 & -s15 & -s10 & +s12 & +s17, fill=mvoid)
c12 = mcdc.cell(+s8 & +s11 & -s15 & -s18, fill=mvoid)
c13 = mcdc.cell(+s7 & -s9 & -s12 & -s10, fill=m4)
c14 = mcdc.cell(+s9 & -s13 & -s10 & +s17, fill=m3)
c15 = mcdc.cell(+s9 & -s12 & +s13 & -s10 & +s17, fill=mvoid)
c16 = mcdc.cell(+s3 & -s5 & -s10 & -s14, fill=mvoid)
c17 = mcdc.cell(+s4 & -s6 & +s11 & -s16, fill=mvoid)
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

