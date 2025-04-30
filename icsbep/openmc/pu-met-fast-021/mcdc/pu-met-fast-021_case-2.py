import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.044422],
	['Pu240',0.0021326],
	['C0',0.00019515],
	['Fe54',4.7895683500000004e-06],
	['Fe56',7.518598022e-05],
	['Fe57',1.7363721699999999e-06],
	['Fe58',2.3107926000000002e-07]])
# Material Name: Berylium-oxide Reflector
# S(a,b): c_Be_in_BeO (Not Implemented)
# S(a,b): c_O_in_BeO (Not Implemented)
m2 = mcdc.material(nuclides=[
	['Be9',0.069041],
	['O16',0.069014833461],
	['O17',2.6166539e-05]])
# Material Name: Steel Cover
m3 = mcdc.material(nuclides=[
	['Fe54',0.002997316],
	['Fe56',0.047051451200000004],
	['Fe57',0.0010866232],
	['Fe58',0.0001446096],
	['C0',0.00034757000000000006],
	['Si28',0.0008225504010800002],
	['Si29',4.1766762459999996e-05],
	['Si30',2.7532836460000002e-05],
	['Ti46',5.0353049999999994e-05],
	['Ti47',4.5409295999999995e-05],
	['Ti48',0.00044994264799999995],
	['Ti49',3.3019394e-05],
	['Ti50',3.1615612e-05],
	['Cr50',0.0006279394],
	['Cr52',0.01210918628],
	['Cr53',0.00137308452],
	['Cr54',0.0003417898],
	['Mn55',0.0015198000000000002],
	['Ni58',0.0048423779739],
	['Ni60',0.0018652753260999999],
	['Ni61',8.108222689999999e-05],
	['Ni62',0.00025852561950000003],
	['Ni64',6.58388536e-05]])
# Material Name: Duralumin base and top (2.78 g/cm3)
m4 = mcdc.material(nuclides=[
	['Al27',0.058077],
	['Mg24',0.000815721732],
	['Mg25',0.00010352663999999999],
	['Mg26',0.00011395162799999999],
	['Mn55',0.00018284],
	['Cu63',0.0007834003500000001],
	['Cu65',0.00034949965000000003]])
# Material Name: Duralumin top cylindrical shell (0.417 g/cm3)
m5 = mcdc.material(nuclides=[
	['Al27',0.0087115],
	['Mg24',0.00012235825980000002],
	['Mg25',1.5528996000000002e-05],
	['Mg26',1.70927442e-05],
	['Mn55',2.7426e-05],
	['Cu63',0.00011750659499999998],
	['Cu65',5.2423405e-05]])
# Material Name: Duralumin bottom cylindrical shell (1.8155 g/cm3)
m6 = mcdc.material(nuclides=[
	['Al27',0.037928],
	['Mg24',0.0005327218725],
	['Mg25',6.760995e-05],
	['Mg26',7.44181775e-05],
	['Mn55',0.00011941],
	['Cu63',0.00051158553],
	['Cu65',0.00022823446999999998]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-17.51, bc='vacuum')
s2 = mcdc.surface('plane-z', z=-2.57, bc='interface')
s3 = mcdc.surface('plane-z', z=-2.55, bc='interface')
s4 = mcdc.surface('plane-z', z=-2.37, bc='interface')
s5 = mcdc.surface('plane-z', z=-2.1, bc='interface')
s6 = mcdc.surface('plane-z', z=-2.06, bc='interface')
s7 = mcdc.surface('plane-z', z=-1.61, bc='interface')
s8 = mcdc.surface('plane-z', z=-1.57, bc='interface')
s9 = mcdc.surface('plane-z', z=-1.12, bc='interface')
s10 = mcdc.surface('plane-z', z=-1.08, bc='interface')
s11 = mcdc.surface('plane-z', z=-0.63, bc='interface')
s12 = mcdc.surface('plane-z', z=-0.59, bc='interface')
s13 = mcdc.surface('plane-z', z=-0.14, bc='interface')
s14 = mcdc.surface('plane-z', z=-0.12, bc='interface')
s15 = mcdc.surface('plane-z', z=0.12, bc='interface')
s16 = mcdc.surface('plane-z', z=0.14, bc='interface')
s17 = mcdc.surface('plane-z', z=0.59, bc='interface')
s18 = mcdc.surface('plane-z', z=0.63, bc='interface')
s19 = mcdc.surface('plane-z', z=1.08, bc='interface')
s20 = mcdc.surface('plane-z', z=1.12, bc='interface')
s21 = mcdc.surface('plane-z', z=1.57, bc='interface')
s22 = mcdc.surface('plane-z', z=1.61, bc='interface')
s23 = mcdc.surface('plane-z', z=2.06, bc='interface')
s24 = mcdc.surface('plane-z', z=2.1, bc='interface')
s25 = mcdc.surface('plane-z', z=2.37, bc='interface')
s26 = mcdc.surface('plane-z', z=2.55, bc='interface')
s27 = mcdc.surface('plane-z', z=2.57, bc='interface')
s28 = mcdc.surface('plane-z', z=2.59, bc='interface')
s29 = mcdc.surface('plane-z', z=17.51, bc='vacuum')
s30 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=9.995, bc='vacuum')
s31 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=6.263, bc='interface')
s32 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=6.063, bc='interface')
s33 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=5.995, bc='interface')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s30, fill=m2)
c2 = mcdc.cell(+s28 & -s29 & -s30, fill=m2)
c3 = mcdc.cell(+s2 & -s4 & -s30 & +s31, fill=m4)
c4 = mcdc.cell(+s25 & -s28 & -s30 & +s31, fill=m4)
c6 = mcdc.cell(+s15 & -s28 & -s31 & +s32, fill=m5)
c7 = mcdc.cell(+s2 & -s14 & -s31 & +s32, fill=m6)
c8 = mcdc.cell(+s2 & -s3 & -s33, fill=m3)
c9 = mcdc.cell(+s5 & -s6 & -s33, fill=m3)
c10 = mcdc.cell(+s7 & -s8 & -s33, fill=m3)
c11 = mcdc.cell(+s9 & -s10 & -s33, fill=m3)
c12 = mcdc.cell(+s11 & -s12 & -s33, fill=m3)
c13 = mcdc.cell(+s13 & -s14 & -s33, fill=m3)
c14 = mcdc.cell(+s15 & -s16 & -s33, fill=m3)
c15 = mcdc.cell(+s17 & -s18 & -s33, fill=m3)
c16 = mcdc.cell(+s19 & -s20 & -s33, fill=m3)
c17 = mcdc.cell(+s21 & -s22 & -s33, fill=m3)
c18 = mcdc.cell(+s23 & -s24 & -s33, fill=m3)
c19 = mcdc.cell(+s26 & -s27 & -s33, fill=m3)
c20 = mcdc.cell(+s2 & -s14 & +s33 & -s32, fill=m3)
c21 = mcdc.cell(+s15 & -s27 & +s33 & -s32, fill=m3)
c22 = mcdc.cell(+s3 & -s5 & -s33, fill=m1)
c23 = mcdc.cell(+s6 & -s7 & -s33, fill=m1)
c24 = mcdc.cell(+s8 & -s9 & -s33, fill=m1)
c25 = mcdc.cell(+s10 & -s11 & -s33, fill=m1)
c26 = mcdc.cell(+s12 & -s13 & -s33, fill=m1)
c27 = mcdc.cell(+s16 & -s17 & -s33, fill=m1)
c28 = mcdc.cell(+s18 & -s19 & -s33, fill=m1)
c29 = mcdc.cell(+s20 & -s21 & -s33, fill=m1)
c30 = mcdc.cell(+s22 & -s23 & -s33, fill=m1)
c31 = mcdc.cell(+s24 & -s26 & -s33, fill=m1)
c32 = mcdc.cell(+s14 & -s15 & -s31, fill=mvoid)
c33 = mcdc.cell(+s4 & -s25 & +s31 & -s30, fill=mvoid)
c34 = mcdc.cell(+s27 & -s28 & -s30, fill=mvoid)
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
mcdc.source(x=[0.0,1.0], y=[0.0,1.0], z=[0.0,1.0], prob=1.0)

mcdc.run()

