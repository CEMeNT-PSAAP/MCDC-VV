import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Core, R < 9.15
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041031],
	['U238',0.0041021],
	['C0',0.00038642],
	['Fe54',7.926989e-06],
	['Fe56',0.0001244367748],
	['Fe57',2.8737878e-06],
	['Fe58',3.824484e-07],
	['W180',1.4897999999999999e-08],
	['W182',3.289975e-06],
	['W183',1.7765865000000004e-06],
	['W184',3.8039560000000004e-06],
	['W186',3.5295845000000006e-06],
	['Cu63',0.0004911793650000001],
	['Cu65',0.000219130635],
	['Ni58',0.00022438827009],
	['Ni60',8.643395990999999e-05],
	['Ni61',3.75722439e-06],
	['Ni62',1.1979675450000002e-05],
	['Ni64',3.0508701600000005e-06]])
# Material Name: Core, outer shell
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.042698],
	['U238',0.0040143],
	['C0',0.00014403],
	['Fe54',2.2194634000000003e-06],
	['Fe56',3.484082888e-05],
	['Fe57',8.046266800000001e-07],
	['Fe58',1.0708103999999999e-07],
	['W180',7.28496e-10],
	['W182',1.608762e-07],
	['W183',8.6873148e-08],
	['W184',1.8600931200000003e-07],
	['W186',1.7259284399999998e-07],
	['Al27',0.00054473]])
# Material Name: Steel (pure Fe)
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
# Material Name: M1 copper (pure Cu)
m4 = mcdc.material(nuclides=[
	['Cu63',0.0569553975],
	['Cu65',0.025409602499999996]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=2.0, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 1.207], radius=2.0, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 1.207], radius=9.15, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=10.15, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 1.207], radius=10.15, bc='interface')
s7 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s8 = mcdc.surface('cylinder-y', center=[0.0, 1.207], radius=0.6, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=10.44, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=1.007, bc='interface')
s12 = mcdc.surface('plane-z', z=1.207, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=8.7, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=16.0, bc='vacuum')
s16 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s17 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.8, bc='interface')
s18 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=10.29, bc='interface')
s19 = mcdc.surface('plane-z', z=-14.74, bc='interface')
s20 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=15.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1 & -s10, fill=mvoid)
c2 = mcdc.cell(+s12 & -s2, fill=mvoid)
c3 = mcdc.cell(+s1 & -s3 & +s7 & -s10, fill=m1)
c4 = mcdc.cell(+s2 & -s4 & +s8 & +s12 & +s16, fill=m1)
c5 = mcdc.cell(+s3 & -s5 & -s10 & +s16, fill=m2)
c6 = mcdc.cell(+s4 & -s6 & +s12 & +s16, fill=m2)
c7 = mcdc.cell(+s1 & -s3 & -s7 & -s10, fill=mvoid)
c8 = mcdc.cell(+s2 & -s4 & -s8 & +s12, fill=mvoid)
c9 = mcdc.cell(+s10 & -s11 & -s15, fill=mvoid)
c10 = mcdc.cell(+s11 & -s12 & -s20 & +s17, fill=m3)
c11 = mcdc.cell(+s5 & -s15 & -s10 & +s13, fill=mvoid)
c12 = mcdc.cell(+s6 & -s15 & +s12, fill=mvoid)
c13 = mcdc.cell(+s18 & -s9 & -s13 & -s10, fill=m4)
c14 = mcdc.cell(+s9 & +s19 & -s14 & -s10, fill=m3)
c15 = mcdc.cell(+s9 & -s15 & +s14 & -s13 & -s10, fill=mvoid)
c16 = mcdc.cell(+s3 & -s5 & -s16 & -s10, fill=mvoid)
c17 = mcdc.cell(+s2 & -s6 & -s16 & +s12, fill=mvoid)
c18 = mcdc.cell(+s11 & -s12 & -s17, fill=mvoid)
c19 = mcdc.cell(+s5 & -s13 & -s18 & -s10, fill=mvoid)
c20 = mcdc.cell(-s14 & -s15 & -s19, fill=mvoid)
c21 = mcdc.cell(+s11 & -s12 & -s15 & +s20, fill=mvoid)
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

