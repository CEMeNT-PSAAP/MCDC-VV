import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.040999],
	['U238',0.0040989],
	['C0',0.00038652],
	['Fe54',7.916468e-06],
	['Fe56',0.0001242716176],
	['Fe57',2.8699736e-06],
	['Fe58',3.819408e-07],
	['W180',1.4896799999999998e-08],
	['W182',3.2897100000000003e-06],
	['W183',1.7764434000000001e-06],
	['W184',3.8036496e-06],
	['W186',3.5293002000000005e-06],
	['Cu63',0.000498218835],
	['Cu65',0.00022227116499999998],
	['Ni58',0.00022760149976999998],
	['Ni60',8.767169023e-05],
	['Ni61',3.8110276699999994e-06],
	['Ni62',1.215122385e-05],
	['Ni64',3.0945584799999997e-06]])
# Material Name: Aluminum reflector
m2 = mcdc.material(nuclides=[
	['Al27',0.058566]])
# Material Name: Steel
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
s1 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=7.75, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 1.17], radius=7.55, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 1.17], radius=9.15, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=10.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 1.17], radius=12.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=10.15, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=1.17, bc='interface')
s12 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=8.7, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s14 = mcdc.surface('plane-y', y=0.5, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s16 = mcdc.surface('plane-y', y=-0.5, bc='interface')
s17 = mcdc.surface('plane-z', z=0.97, bc='interface')
s18 = mcdc.surface('cylinder-y', center=[0.0, 1.17], radius=0.6, bc='interface')
s19 = mcdc.surface('plane-z', z=-14.15, bc='vacuum')
s20 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s3, fill=m1)
c2 = mcdc.cell(+s1 & +s3 & -s5 & -s10, fill=m1)
c3 = mcdc.cell(+s4 & -s6 & +s11 & +s18, fill=m1)
c4 = mcdc.cell(+s5 & -s7 & -s10, fill=m2)
c5 = mcdc.cell(+s6 & -s8 & +s11, fill=m2)
c6 = mcdc.cell(+s7 & -s9 & -s12 & -s10, fill=m4)
c7 = mcdc.cell(+s2 & -s11 & -s15 & +s17, fill=m3)
c8 = mcdc.cell(+s9 & +s19 & -s13 & -s10, fill=m3)
c9 = mcdc.cell(-s1 & -s14 & +s16, fill=mvoid)
c10 = mcdc.cell(-s1 & +s3 & -s5 & -s10, fill=mvoid)
c11 = mcdc.cell(+s3 & -s4 & +s11, fill=mvoid)
c12 = mcdc.cell(+s3 & -s11 & +s17 & -s2, fill=mvoid)
c13 = mcdc.cell(+s7 & -s10 & +s12 & -s15 & +s19, fill=mvoid)
c14 = mcdc.cell(+s8 & +s11 & -s15 & -s20, fill=mvoid)
c15 = mcdc.cell(+s9 & -s12 & +s13 & -s10 & -s15 & +s19, fill=mvoid)
c16 = mcdc.cell(+s4 & -s6 & +s11 & -s18, fill=mvoid)
c17 = mcdc.cell(+s3 & +s10 & -s15 & -s17, fill=mvoid)
c18 = mcdc.cell(-s3 & -s1 & +s14, fill=m1)
c19 = mcdc.cell(-s3 & -s1 & -s16, fill=m1)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

#	eigenvalue = 
   
# Simulation Parameters
