import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Tuballoy
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.00034583],
	['U238',0.047684]])
# Material Name: Oralloy
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.044849],
	['U238',0.0026305]])
# Material Name: 2024 Aluminum
m3 = mcdc.material(nuclides=[
	['Mg24',0.0008128005450000001],
	['Mg25',0.0001031559],
	['Mg26',0.000113543555],
	['Al27',0.057868],
	['Mn55',0.00015182],
	['Cu63',0.0007986825],
	['Cu65',0.0003563175]])
# Material Name: Stainless Steel
m4 = mcdc.material(nuclides=[
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
s103 = mcdc.surface('plane-z', z=0.604, bc='interface')
s106 = mcdc.surface('plane-z', z=1.408, bc='interface')
s108 = mcdc.surface('plane-z', z=2.012, bc='interface')
s109 = mcdc.surface('plane-z', z=2.616, bc='interface')
s112 = mcdc.surface('plane-z', z=3.42, bc='interface')
s114 = mcdc.surface('plane-z', z=4.024, bc='interface')
s115 = mcdc.surface('plane-z', z=4.628, bc='interface')
s118 = mcdc.surface('plane-z', z=5.432, bc='interface')
s120 = mcdc.surface('plane-z', z=6.036, bc='interface')
s121 = mcdc.surface('plane-z', z=6.64, bc='interface')
s124 = mcdc.surface('plane-z', z=7.444, bc='interface')
s126 = mcdc.surface('plane-z', z=8.048, bc='interface')
s127 = mcdc.surface('plane-z', z=8.652, bc='interface')
s130 = mcdc.surface('plane-z', z=9.456, bc='interface')
s132 = mcdc.surface('plane-z', z=10.06, bc='interface')
s133 = mcdc.surface('plane-z', z=10.664, bc='interface')
s136 = mcdc.surface('plane-z', z=11.468, bc='interface')
s138 = mcdc.surface('plane-z', z=12.072, bc='interface')
s139 = mcdc.surface('plane-z', z=12.676, bc='interface')
s142 = mcdc.surface('plane-z', z=13.48, bc='interface')
s144 = mcdc.surface('plane-z', z=14.084, bc='interface')
s146 = mcdc.surface('plane-z', z=14.688, bc='interface')
s149 = mcdc.surface('plane-z', z=15.492, bc='interface')
s151 = mcdc.surface('plane-z', z=16.096, bc='interface')
s153 = mcdc.surface('plane-z', z=16.7, bc='interface')
s155 = mcdc.surface('plane-z', z=17.504, bc='interface')
s157 = mcdc.surface('plane-z', z=18.108, bc='interface')
s159 = mcdc.surface('plane-z', z=18.712, bc='interface')
s161 = mcdc.surface('plane-z', z=19.516, bc='interface')
s163 = mcdc.surface('plane-z', z=20.12, bc='interface')
s165 = mcdc.surface('plane-z', z=20.724, bc='interface')
s167 = mcdc.surface('plane-z', z=21.528, bc='interface')
s169 = mcdc.surface('plane-z', z=22.132, bc='interface')
s171 = mcdc.surface('plane-z', z=22.736, bc='interface')
s173 = mcdc.surface('plane-z', z=23.54, bc='interface')
s175 = mcdc.surface('plane-z', z=24.144, bc='interface')
s177 = mcdc.surface('plane-z', z=24.748, bc='interface')
s179 = mcdc.surface('plane-z', z=24.9729, bc='vacuum')
s201 = mcdc.surface('plane-z', z=-0.3175, bc='interface')
s202 = mcdc.surface('plane-z', z=-0.9525, bc='interface')
s203 = mcdc.surface('plane-z', z=-3.175, bc='interface')
s204 = mcdc.surface('plane-z', z=-4.7625, bc='interface')
s205 = mcdc.surface('plane-z', z=-6.0325, bc='interface')
s206 = mcdc.surface('plane-z', z=-8.5725, bc='vacuum')

# Material Cell(s)
c51 = mcdc.cell(+s101 & -s103 & -s12, fill=m1)
c52 = mcdc.cell(+s103 & -s106 & -s12, fill=m2)
c53 = mcdc.cell(+s106 & -s108 & -s12, fill=m1)
c54 = mcdc.cell(+s108 & -s109 & -s12, fill=m1)
c55 = mcdc.cell(+s109 & -s112 & -s12, fill=m2)
c56 = mcdc.cell(+s112 & -s114 & -s12, fill=m1)
c57 = mcdc.cell(+s114 & -s115 & -s12, fill=m1)
c58 = mcdc.cell(+s115 & -s118 & -s12, fill=m2)
c59 = mcdc.cell(+s118 & -s120 & -s12, fill=m1)
c60 = mcdc.cell(+s120 & -s121 & -s12, fill=m1)
c61 = mcdc.cell(+s121 & -s124 & -s12, fill=m2)
c62 = mcdc.cell(+s124 & -s126 & -s12, fill=m1)
c63 = mcdc.cell(+s126 & -s127 & -s12, fill=m1)
c64 = mcdc.cell(+s127 & -s130 & -s12, fill=m2)
c65 = mcdc.cell(+s130 & -s132 & -s12, fill=m1)
c66 = mcdc.cell(+s132 & -s133 & -s12, fill=m1)
c67 = mcdc.cell(+s133 & -s136 & -s12, fill=m2)
c68 = mcdc.cell(+s136 & -s138 & -s12, fill=m1)
c69 = mcdc.cell(+s138 & -s139 & -s12, fill=m1)
c70 = mcdc.cell(+s139 & -s142 & -s12, fill=m2)
c71 = mcdc.cell(+s142 & -s144 & -s12, fill=m1)
c72 = mcdc.cell(+s144 & -s146 & -s10, fill=m1)
c73 = mcdc.cell(+s146 & -s149 & -s12, fill=m2)
c74 = mcdc.cell(+s149 & -s151 & -s12, fill=m1)
c75 = mcdc.cell(+s151 & -s153 & -s12, fill=m1)
c76 = mcdc.cell(+s153 & -s155 & -s12, fill=m2)
c77 = mcdc.cell(+s155 & -s157 & -s12, fill=m1)
c78 = mcdc.cell(+s157 & -s159 & -s12, fill=m1)
c79 = mcdc.cell(+s159 & -s161 & -s12, fill=m2)
c80 = mcdc.cell(+s161 & -s163 & -s12, fill=m1)
c81 = mcdc.cell(+s163 & -s165 & -s12, fill=m1)
c82 = mcdc.cell(+s165 & -s167 & -s12, fill=m2)
c83 = mcdc.cell(+s167 & -s169 & -s12, fill=m1)
c84 = mcdc.cell(+s169 & -s171 & -s12, fill=m1)
c85 = mcdc.cell(+s171 & -s173 & -s12, fill=m2)
c86 = mcdc.cell(+s173 & -s175 & -s12, fill=m1)
c87 = mcdc.cell(+s175 & -s177 & -s12, fill=m1)
c88 = mcdc.cell(+s177 & -s179 & -s12, fill=m1)
c103 = mcdc.cell(+s144 & -s146 & +s10 & -s17, fill=m3)
c106 = mcdc.cell(+s201 & -s101 & -s8, fill=mvoid)
c107 = mcdc.cell(+s202 & -s201 & +s3 & -s8, fill=mvoid)
c108 = mcdc.cell(+s202 & -s101 & +s8 & -s18, fill=m3)
c110 = mcdc.cell(+s203 & -s201 & -s3, fill=m3)
c111 = mcdc.cell(+s205 & -s203 & -s7, fill=m3)
c112 = mcdc.cell(+s204 & -s202 & +s12 & -s14, fill=m3)
c114 = mcdc.cell(+s204 & -s202 & +s14 & -s21, fill=mvoid)
c118 = mcdc.cell(+s205 & -s204 & +s11 & -s19, fill=m3)
c119 = mcdc.cell(+s205 & -s204 & +s7 & -s11, fill=mvoid)
c120 = mcdc.cell(+s206 & -s205 & -s20, fill=m4)
c122 = mcdc.cell(+s205 & -s204 & +s19 & -s21, fill=mvoid)
c123 = mcdc.cell(+s206 & -s205 & +s20 & -s21, fill=mvoid)
c113 = mcdc.cell(+s3 & -s12 & -s202 & +s203, fill=mvoid)
c1132 = mcdc.cell(-s203 & -s12 & +s204 & +s7, fill=mvoid)
c121 = mcdc.cell(-s21 & +s12 & -s179 & +s146, fill=mvoid)
c1212 = mcdc.cell(-s21 & +s17 & -s146 & +s144, fill=mvoid)
c1213 = mcdc.cell(-s21 & +s12 & -s144 & +s101, fill=mvoid)
c1214 = mcdc.cell(-s21 & +s18 & -s101 & +s202, fill=mvoid)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

#	eigenvalue = 
   
# Simulation Parameters
