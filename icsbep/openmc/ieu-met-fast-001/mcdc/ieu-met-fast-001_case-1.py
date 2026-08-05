import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Tuballoy
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.00034591],
	['U238',0.047694]])
# Material Name: Oralloy
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.044824],
	['U238',0.0026391]])
# Material Name: Mixed Uranium
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.023353],
	['U238',0.021939]])
# Material Name: 2024 Aluminum
m4 = mcdc.material(nuclides=[
	['Mg24',0.0008128005450000001],
	['Mg25',0.0001031559],
	['Mg26',0.000113543555],
	['Al27',0.057868],
	['Mn55',0.00015182],
	['Cu63',0.0007986825],
	['Cu65',0.0003563175]])
# Material Name: Stainless Steel
m5 = mcdc.material(nuclides=[
	['Cr50',0.0007183154000000001],
	['Cr52',0.01385199748],
	['Cr53',0.0015707053200000004],
	['Cr54',0.00039098180000000005],
	['Fe54',0.0036985991000000004],
	['Fe56',0.05806009612],
	['Fe57',0.0013408608200000001],
	['Fe58',0.00017844395999999998],
	['Ni58',0.0044314658055],
	['Ni60',0.0017069926944999999],
	['Ni61',7.420179049999999e-05],
	['Ni62',0.0002365877775],
	['Ni64',6.0251932e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.11125, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.74625, bc='interface')
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=4.60375, bc='interface')
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.065, bc='interface')
s10 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.66939, bc='interface')
s11 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=12.7, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=13.335, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=13.67711, bc='interface')
s17 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=15.29416, bc='interface')
s18 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=15.82055, bc='interface')
s19 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=17.1965, bc='interface')
s20 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=19.22627, bc='vacuum')
s21 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=21.0, bc='vacuum')
s101 = mcdc.surface('plane-z', z=0.0, bc='interface')
s105 = mcdc.surface('plane-z', z=0.804, bc='interface')
s106 = mcdc.surface('plane-z', z=1.408, bc='interface')
s109 = mcdc.surface('plane-z', z=2.212, bc='interface')
s110 = mcdc.surface('plane-z', z=2.816, bc='interface')
s113 = mcdc.surface('plane-z', z=3.62, bc='interface')
s114 = mcdc.surface('plane-z', z=4.224, bc='interface')
s117 = mcdc.surface('plane-z', z=5.028, bc='interface')
s118 = mcdc.surface('plane-z', z=5.632, bc='interface')
s121 = mcdc.surface('plane-z', z=6.436, bc='interface')
s122 = mcdc.surface('plane-z', z=7.04, bc='interface')
s125 = mcdc.surface('plane-z', z=7.844, bc='interface')
s126 = mcdc.surface('plane-z', z=8.448, bc='interface')
s129 = mcdc.surface('plane-z', z=9.252, bc='interface')
s131 = mcdc.surface('plane-z', z=9.856, bc='interface')
s134 = mcdc.surface('plane-z', z=10.66, bc='interface')
s136 = mcdc.surface('plane-z', z=11.264, bc='interface')
s138 = mcdc.surface('plane-z', z=12.068, bc='interface')
s140 = mcdc.surface('plane-z', z=12.672, bc='interface')
s142 = mcdc.surface('plane-z', z=13.476, bc='interface')
s144 = mcdc.surface('plane-z', z=14.08, bc='interface')
s146 = mcdc.surface('plane-z', z=14.884, bc='interface')
s161 = mcdc.surface('plane-z', z=14.9631, bc='vacuum')
s201 = mcdc.surface('plane-z', z=-0.3175, bc='interface')
s202 = mcdc.surface('plane-z', z=-0.9525, bc='interface')
s203 = mcdc.surface('plane-z', z=-3.175, bc='interface')
s204 = mcdc.surface('plane-z', z=-4.7625, bc='interface')
s205 = mcdc.surface('plane-z', z=-6.0325, bc='interface')
s206 = mcdc.surface('plane-z', z=-8.5725, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s101 & -s129 & -s2, fill=m3)
c51 = mcdc.cell(+s101 & -s105 & +s2 & -s12, fill=m2)
c52 = mcdc.cell(+s105 & -s106 & +s2 & -s12, fill=m1)
c53 = mcdc.cell(+s106 & -s109 & +s2 & -s12, fill=m2)
c54 = mcdc.cell(+s109 & -s110 & +s2 & -s12, fill=m1)
c55 = mcdc.cell(+s110 & -s113 & +s2 & -s12, fill=m2)
c56 = mcdc.cell(+s113 & -s114 & +s2 & -s12, fill=m1)
c57 = mcdc.cell(+s114 & -s117 & +s2 & -s12, fill=m2)
c58 = mcdc.cell(+s117 & -s118 & +s2 & -s12, fill=m1)
c59 = mcdc.cell(+s118 & -s121 & +s2 & -s12, fill=m2)
c60 = mcdc.cell(+s121 & -s122 & +s2 & -s12, fill=m1)
c61 = mcdc.cell(+s122 & -s125 & +s2 & -s12, fill=m2)
c62 = mcdc.cell(+s125 & -s126 & +s2 & -s12, fill=m1)
c63 = mcdc.cell(+s126 & -s129 & +s2 & -s12, fill=m2)
c64 = mcdc.cell(+s129 & -s131 & -s10, fill=m1)
c65 = mcdc.cell(+s131 & -s134 & -s12, fill=m2)
c66 = mcdc.cell(+s134 & -s136 & -s12, fill=m1)
c67 = mcdc.cell(+s136 & -s138 & -s12, fill=m2)
c68 = mcdc.cell(+s138 & -s140 & -s12, fill=m1)
c69 = mcdc.cell(+s140 & -s142 & -s12, fill=m2)
c70 = mcdc.cell(+s142 & -s144 & -s12, fill=m1)
c71 = mcdc.cell(+s144 & -s146 & -s12, fill=m2)
c72 = mcdc.cell(+s146 & -s161 & -s12, fill=m1)
c103 = mcdc.cell(+s129 & -s131 & +s10 & -s17, fill=m4)
c106 = mcdc.cell(+s201 & -s101 & -s8, fill=mvoid)
c107 = mcdc.cell(+s202 & -s201 & +s3 & -s8, fill=mvoid)
c108 = mcdc.cell(+s202 & -s101 & +s8 & -s18, fill=m4)
c110 = mcdc.cell(+s203 & -s201 & -s3, fill=m4)
c111 = mcdc.cell(+s205 & -s203 & -s7, fill=m4)
c112 = mcdc.cell(+s204 & -s202 & +s12 & -s14, fill=m4)
c114 = mcdc.cell(+s204 & -s202 & +s14 & -s21, fill=mvoid)
c118 = mcdc.cell(+s205 & -s204 & +s11 & -s19, fill=m4)
c119 = mcdc.cell(+s205 & -s204 & +s7 & -s11, fill=mvoid)
c120 = mcdc.cell(+s206 & -s205 & -s20, fill=m5)
c122 = mcdc.cell(+s205 & -s204 & +s19 & -s21, fill=mvoid)
c123 = mcdc.cell(+s206 & -s205 & +s20 & -s21, fill=mvoid)
c113 = mcdc.cell(+s3 & -s12 & -s202 & +s203, fill=mvoid)
c1132 = mcdc.cell(-s203 & -s12 & +s204 & +s7, fill=mvoid)
c121 = mcdc.cell(-s21 & +s17 & -s161 & +s202, fill=mvoid)
c124 = mcdc.cell(-s161 & +s131 & +s12 & -s17, fill=mvoid)
c125 = mcdc.cell(+s12 & -s129 & -s17 & +s101, fill=mvoid)
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

