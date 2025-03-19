import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.044918],
	['U238',0.002574]])
# Material Name: c_Graphite
# S(a,b): c_Graphite (Not Implemented)
m2 = mcdc.material(nuclides=[
	['C0',0.08538]])
# Material Name: Cu
m3 = mcdc.material(nuclides=[
	['Cu63',0.05724237000000001],
	['Cu65',0.025537630000000002]])
# Material Name: Al 6061-T6
m4 = mcdc.material(nuclides=[
	['Si28',0.00031630168756000004],
	['Si29',1.6060897220000002e-05],
	['Si30',1.058741522e-05],
	['Fe54',5.8806545e-06],
	['Fe56',9.23136994e-05],
	['Fe57',2.1319259000000002e-06],
	['Fe58',2.837202e-07],
	['Cu63',4.80391965e-05],
	['Cu65',2.14318035e-05],
	['Mn55',2.1915e-05],
	['Mg24',0.0005214634599],
	['Mg25',6.6181098e-05],
	['Mg26',7.28454421e-05],
	['Cr50',3.35368825e-06],
	['Cr52',6.467253965e-05],
	['Cr53',7.33334685e-06],
	['Cr54',1.82542525e-06],
	['Zn64',1.5088797899999998e-05],
	['Zn66',8.509505099999999e-06],
	['Zn67',1.2397548e-06],
	['Zn68',5.6617514999999996e-06],
	['Zn70',1.871907e-07],
	['Ti46',2.074545e-06],
	['Ti47',1.8708623999999995e-06],
	['Ti48',1.8537631199999998e-05],
	['Ti49',1.3603986e-06],
	['Ti50',1.3025628e-06],
	['Al27',0.057816]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-5.7912, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s3 = mcdc.surface('plane-z', z=3.4972, bc='interface')
s4 = mcdc.surface('plane-z', z=9.8472, bc='interface')
s5 = mcdc.surface('plane-z', z=24.2744, bc='interface')
s6 = mcdc.surface('plane-z', z=28.30384, bc='interface')
s7 = mcdc.surface('plane-z', z=28.60356, bc='interface')
s8 = mcdc.surface('plane-z', z=32.633, bc='interface')
s9 = mcdc.surface('plane-z', z=36.66244, bc='interface')
s10 = mcdc.surface('plane-z', z=36.96216, bc='interface')
s11 = mcdc.surface('plane-z', z=40.9916, bc='interface')
s12 = mcdc.surface('plane-z', z=45.02104, bc='interface')
s13 = mcdc.surface('plane-z', z=45.32076, bc='interface')
s14 = mcdc.surface('plane-z', z=49.3502, bc='interface')
s15 = mcdc.surface('plane-z', z=53.37964, bc='interface')
s16 = mcdc.surface('plane-z', z=53.67936, bc='interface')
s17 = mcdc.surface('plane-z', z=57.7088, bc='interface')
s18 = mcdc.surface('plane-z', z=61.73824, bc='interface')
s19 = mcdc.surface('plane-z', z=62.03796, bc='interface')
s20 = mcdc.surface('plane-z', z=66.0674, bc='interface')
s21 = mcdc.surface('plane-z', z=70.09684, bc='interface')
s22 = mcdc.surface('plane-z', z=70.39656, bc='interface')
s23 = mcdc.surface('plane-z', z=74.426, bc='interface')
s24 = mcdc.surface('plane-z', z=78.45544, bc='interface')
s25 = mcdc.surface('plane-z', z=78.75516, bc='interface')
s26 = mcdc.surface('plane-z', z=82.7846, bc='interface')
s27 = mcdc.surface('plane-z', z=86.81404, bc='interface')
s28 = mcdc.surface('plane-z', z=87.11376, bc='interface')
s29 = mcdc.surface('plane-z', z=91.1432, bc='interface')
s30 = mcdc.surface('plane-z', z=95.17264, bc='interface')
s31 = mcdc.surface('plane-z', z=95.47236, bc='interface')
s32 = mcdc.surface('plane-z', z=99.5018, bc='interface')
s33 = mcdc.surface('plane-z', z=103.53124, bc='interface')
s34 = mcdc.surface('plane-z', z=103.83096, bc='interface')
s35 = mcdc.surface('plane-z', z=107.8604, bc='interface')
s36 = mcdc.surface('plane-z', z=108.6104, bc='interface')
s37 = mcdc.surface('plane-z', z=123.0376, bc='interface')
s38 = mcdc.surface('plane-z', z=123.9012, bc='vacuum')
s39 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.54, bc='interface')
s40 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.1496, bc='interface')
s41 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.175, bc='interface')
s42 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=4.7625, bc='interface')
s43 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.67, bc='interface')
s44 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=26.797, bc='interface')
s45 = mcdc.surface('plane-x', x=-27.94, bc='interface')
s46 = mcdc.surface('plane-x', x=27.94, bc='interface')
s47 = mcdc.surface('plane-y', y=-27.94, bc='interface')
s48 = mcdc.surface('plane-y', y=27.94, bc='interface')
s49 = mcdc.surface('plane-x', x=-44.1452, bc='vacuum')
s50 = mcdc.surface('plane-x', x=44.1452, bc='vacuum')
s51 = mcdc.surface('plane-y', y=-44.1452, bc='vacuum')
s52 = mcdc.surface('plane-y', y=44.1452, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s17 & -s39, fill=mvoid)
c2 = mcdc.cell(+s1 & -s17 & +s39 & -s40, fill=m4)
c3 = mcdc.cell(+s1 & -s17 & +s40 & -s41, fill=mvoid)
c4 = mcdc.cell(+s1 & -s2 & +s41 & +s49 & -s50 & +s51 & -s52, fill=mvoid)
c5 = mcdc.cell(+s2 & -s3 & +s41 & -s44, fill=mvoid)
c6 = mcdc.cell(+s2 & -s3 & +s44 & +s49 & -s50 & +s51 & -s52, fill=m3)
c7 = mcdc.cell(+s3 & -s4 & +s41 & -s42, fill=mvoid)
c8 = mcdc.cell(+s3 & -s4 & +s42 & -s43, fill=m4)
c9 = mcdc.cell(+s3 & -s4 & +s43 & -s44, fill=mvoid)
c10 = mcdc.cell(+s3 & -s4 & +s44 & +s49 & -s50 & +s51 & -s52, fill=m3)
c11 = mcdc.cell(+s4 & -s5 & +s41 & -s43, fill=m3)
c12 = mcdc.cell(+s4 & -s5 & +s43 & -s44, fill=mvoid)
c13 = mcdc.cell(+s4 & -s5 & +s44 & +s49 & -s50 & +s51 & -s52, fill=m3)
c14 = mcdc.cell(+s5 & -s6 & +s41 & -s43, fill=m2)
c15 = mcdc.cell(+s6 & -s7 & +s41 & -s43, fill=m1)
c16 = mcdc.cell(+s7 & -s8 & +s41 & -s43, fill=m2)
c17 = mcdc.cell(+s8 & -s9 & +s41 & -s43, fill=m2)
c18 = mcdc.cell(+s9 & -s10 & +s41 & -s43, fill=m1)
c19 = mcdc.cell(+s10 & -s11 & +s41 & -s43, fill=m2)
c20 = mcdc.cell(+s11 & -s12 & +s41 & -s43, fill=m2)
c21 = mcdc.cell(+s12 & -s13 & +s41 & -s43, fill=m1)
c22 = mcdc.cell(+s13 & -s14 & +s41 & -s43, fill=m2)
c23 = mcdc.cell(+s14 & -s15 & +s41 & -s43, fill=m2)
c24 = mcdc.cell(+s15 & -s16 & +s41 & -s43, fill=m1)
c25 = mcdc.cell(+s16 & -s17 & +s41 & -s43, fill=m2)
c26 = mcdc.cell(+s17 & -s18 & -s43, fill=m2)
c27 = mcdc.cell(+s18 & -s19 & -s43, fill=m1)
c28 = mcdc.cell(+s19 & -s20 & -s43, fill=m2)
c29 = mcdc.cell(+s20 & -s21 & -s43, fill=m2)
c30 = mcdc.cell(+s21 & -s22 & -s43, fill=m1)
c31 = mcdc.cell(+s22 & -s23 & -s43, fill=m2)
c32 = mcdc.cell(+s23 & -s24 & -s43, fill=m2)
c33 = mcdc.cell(+s24 & -s25 & -s43, fill=m1)
c34 = mcdc.cell(+s25 & -s26 & -s43, fill=m2)
c35 = mcdc.cell(+s26 & -s27 & -s43, fill=m2)
c36 = mcdc.cell(+s27 & -s28 & -s43, fill=m1)
c37 = mcdc.cell(+s28 & -s29 & -s43, fill=m2)
c38 = mcdc.cell(+s29 & -s30 & -s43, fill=m2)
c39 = mcdc.cell(+s30 & -s31 & -s43, fill=m1)
c40 = mcdc.cell(+s31 & -s32 & -s43, fill=m2)
c41 = mcdc.cell(+s32 & -s33 & -s43, fill=m2)
c42 = mcdc.cell(+s33 & -s34 & -s43, fill=m1)
c43 = mcdc.cell(+s34 & -s35 & -s43, fill=m2)
c44 = mcdc.cell(+s35 & -s36 & -s43, fill=mvoid)
c45 = mcdc.cell(+s36 & -s37 & -s44, fill=m3)
c46 = mcdc.cell(+s5 & -s36 & +s43 & -s44, fill=mvoid)
c47 = mcdc.cell(+s5 & -s37 & +s44 & +s49 & -s50 & +s51 & -s52, fill=m3)
c48 = mcdc.cell(+s37 & -s38 & +s45 & -s46 & +s47 & -s48, fill=mvoid)
c49 = mcdc.cell(+s37 & -s38 & +s49 & -s45 & +s51 & -s52, fill=m3)
c50 = mcdc.cell(+s37 & -s38 & +s46 & -s50 & +s51 & -s52, fill=m3)
c51 = mcdc.cell(+s37 & -s38 & +s45 & -s46 & +s51 & -s47, fill=m3)
c52 = mcdc.cell(+s37 & -s38 & +s45 & -s46 & +s48 & -s52, fill=m3)
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
mcdc.source(x=[-1.0,1.0], y=[-1.0,1.0], z=[70.0,72.0], prob=1.0)

mcdc.run()

