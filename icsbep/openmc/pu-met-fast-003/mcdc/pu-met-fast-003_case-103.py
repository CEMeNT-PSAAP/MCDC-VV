import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Pure Pu
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.04601],
	['Pu240',0.0029236],
	['Pu242',4.8566e-06]])
# Material Name: Aluminum
m2 = mcdc.material(nuclides=[
	['Al27',0.060263]])
# Material Name: Aluminum
m3 = mcdc.material(nuclides=[
	['Al27',0.053031]])
# Material Name: Al Heat Sink: Top
m4 = mcdc.material(nuclides=[
	['Al27',0.036742]])
# Material Name: Al Heat Sink: Bottom
m5 = mcdc.material(nuclides=[
	['Al27',0.030139]])
# Material Name: Steel
m6 = mcdc.material(nuclides=[
	['Fe54',0.004916930900000001],
	['Fe56',0.07718529988],
	['Fe57',0.0017825451800000001],
	['Fe58',0.00023722404000000002]])
# Material Name: Steel (Table Support at 7% density)
m7 = mcdc.material(nuclides=[
	['Fe54',0.000344182825],
	['Fe56',0.00540293429],
	['Fe57',0.000124777315],
	['Fe58',1.660557e-05]])
# Material Name: Stainless Steel: Shoe
m8 = mcdc.material(nuclides=[
	['Al27',0.02926],
	['Fe54',0.00045538979499999997],
	['Fe56',0.007148645893999999],
	['Fe57',0.000165093409],
	['Fe58',2.1970902e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-x', x=-66.0, bc='vacuum')
s2 = mcdc.surface('plane-x', x=66.0, bc='vacuum')
s3 = mcdc.surface('plane-y', y=-23.0, bc='vacuum')
s4 = mcdc.surface('plane-y', y=23.0, bc='vacuum')
s5 = mcdc.surface('plane-z', z=-32.54, bc='vacuum')
s6 = mcdc.surface('plane-z', z=-2.54, bc='interface')
s7 = mcdc.surface('plane-z', z=0.0, bc='interface')
s8 = mcdc.surface('plane-z', z=8.3, bc='interface')
s9 = mcdc.surface('plane-z', z=14.529, bc='interface')
s10 = mcdc.surface('plane-z', z=15.164, bc='interface')
s11 = mcdc.surface('plane-z', z=15.185, bc='interface')
s12 = mcdc.surface('plane-z', z=19.818, bc='interface')
s13 = mcdc.surface('plane-z', z=19.905, bc='interface')
s14 = mcdc.surface('plane-z', z=20.384, bc='interface')
s15 = mcdc.surface('plane-z', z=22.239, bc='interface')
s16 = mcdc.surface('plane-z', z=22.874, bc='interface')
s17 = mcdc.surface('plane-z', z=22.895, bc='interface')
s18 = mcdc.surface('plane-z', z=27.528, bc='interface')
s19 = mcdc.surface('plane-z', z=27.615, bc='interface')
s20 = mcdc.surface('plane-z', z=28.094, bc='interface')
s21 = mcdc.surface('plane-z', z=29.949, bc='interface')
s22 = mcdc.surface('plane-z', z=30.584, bc='interface')
s23 = mcdc.surface('plane-z', z=30.605, bc='interface')
s24 = mcdc.surface('plane-z', z=35.238, bc='interface')
s25 = mcdc.surface('plane-z', z=35.325, bc='interface')
s26 = mcdc.surface('plane-z', z=35.804, bc='interface')
s27 = mcdc.surface('plane-z', z=45.733, bc='vacuum')
s28 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.104, bc='interface')
s29 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.326, bc='interface')
s30 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.2625, bc='interface')
s31 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.2995, bc='interface')
s32 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.425, bc='interface')
s33 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.609, bc='interface')
s40 = mcdc.surface('plane-x', x=-14.4, bc='interface')
s41 = mcdc.surface('plane-x', x=14.4, bc='interface')
s42 = mcdc.surface('plane-y', y=-14.4, bc='interface')
s43 = mcdc.surface('plane-y', y=14.4, bc='interface')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & +s3 & -s4 & +s5 & -s6, fill=m7)
c2 = mcdc.cell(+s1 & -s2 & +s3 & -s4 & +s6 & -s7, fill=m3)
c3 = mcdc.cell(-s8 & -s32, fill=m8)
c4 = mcdc.cell(+s8 & -s9 & -s28, fill=mvoid)
c5 = mcdc.cell(+s8 & -s9 & +s28 & -s29, fill=m2)
c6 = mcdc.cell(+s8 & -s9 & +s29 & -s32, fill=mvoid)
c7 = mcdc.cell(+s26 & -s32, fill=mvoid)
c8 = mcdc.cell(+s32 & -s33, fill=m2)
c80 = mcdc.cell(+s33, fill=mvoid)
c9 = mcdc.cell(+s9 & -s10 & -s31, fill=m5)
c10 = mcdc.cell(+s10 & -s11 & -s31, fill=m6)
c11 = mcdc.cell(+s11 & -s12 & -s30, fill=m1)
c12 = mcdc.cell(+s11 & -s12 & +s30 & -s31, fill=m2)
c13 = mcdc.cell(+s12 & -s13 & -s31, fill=m2)
c14 = mcdc.cell(+s13 & -s14 & -s31, fill=m4)
c15 = mcdc.cell(+s9 & -s14 & +s31 & -s32, fill=mvoid)
c16 = mcdc.cell(+s14 & -s15 & -s28, fill=mvoid)
c17 = mcdc.cell(+s14 & -s15 & +s28 & -s29, fill=m2)
c18 = mcdc.cell(+s14 & -s15 & +s29 & -s32, fill=mvoid)
c19 = mcdc.cell(+s15 & -s16 & -s31, fill=m5)
c20 = mcdc.cell(+s16 & -s17 & -s31, fill=m6)
c21 = mcdc.cell(+s17 & -s18 & -s30, fill=m1)
c22 = mcdc.cell(+s17 & -s18 & +s30 & -s31, fill=m2)
c23 = mcdc.cell(+s18 & -s19 & -s31, fill=m2)
c24 = mcdc.cell(+s19 & -s20 & -s31, fill=m4)
c25 = mcdc.cell(+s15 & -s20 & +s31 & -s32, fill=mvoid)
c26 = mcdc.cell(+s20 & -s21 & -s28, fill=mvoid)
c27 = mcdc.cell(+s20 & -s21 & +s28 & -s29, fill=m2)
c28 = mcdc.cell(+s20 & -s21 & +s29 & -s32, fill=mvoid)
c29 = mcdc.cell(+s21 & -s22 & -s31, fill=m5)
c30 = mcdc.cell(+s22 & -s23 & -s31, fill=m6)
c31 = mcdc.cell(+s23 & -s24 & -s30, fill=m1)
c32 = mcdc.cell(+s23 & -s24 & +s30 & -s31, fill=m2)
c33 = mcdc.cell(+s24 & -s25 & -s31, fill=m2)
c34 = mcdc.cell(+s25 & -s26 & -s31, fill=m4)
c35 = mcdc.cell(+s21 & -s26 & +s31 & -s32, fill=mvoid)
c37 = mcdc.cell(+s1 & -s2 & +s3 & -s42 & +s7 & -s27, fill=mvoid)
c38 = mcdc.cell(+s1 & -s40 & +s42 & -s43 & +s7 & -s27, fill=mvoid)
c39 = mcdc.cell(+s41 & -s2 & +s42 & -s43 & +s7 & -s27, fill=mvoid)
c40 = mcdc.cell(+s1 & -s2 & +s43 & -s4 & +s7 & -s27, fill=mvoid)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

# Rectangular Lattice 100
Lattice100 = mcdc.lattice(x=[-14.4, 9.6, 3], y=[-14.4, 9.6, 3], 