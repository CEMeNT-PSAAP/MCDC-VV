import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.041032],
	['U238',0.004101],
	['C0',0.00039536000000000004],
	['Fe54',7.897764e-06],
	['Fe56',0.0001239780048],
	['Fe57',2.8631928e-06],
	['Fe58',3.810384e-07],
	['W180',1.4911199999999998e-08],
	['W182',3.29289e-06],
	['W183',1.7781606e-06],
	['W184',3.8073264e-06],
	['W186',3.5327117999999993e-06],
	['Cu63',0.0004927006649999999],
	['Cu65',0.000219809335],
	['Ni58',0.00022507584678000002],
	['Ni60',8.669881322e-05],
	['Ni61',3.7687373799999992e-06],
	['Ni62',1.20163839e-05],
	['Ni64',3.06021872e-06]])
# Material Name: Duralumin
m2 = mcdc.material(nuclides=[
	['Al27',0.058077],
	['Mg24',0.000815721732],
	['Mg25',0.00010352663999999999],
	['Mg26',0.00011395162799999999],
	['Mn55',0.00018284],
	['Cu63',0.0007834003500000001],
	['Cu65',0.00034949965000000003]])
# Material Name: Pure Fe
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
# Material Name: Depleted Uranium
# Depletable
m4 = mcdc.material(nuclides=[
	['U235',0.00023832],
	['U238',0.046826]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.64], radius=3.15, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.64], radius=8.35, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.64], radius=9.15, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.64], radius=13.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.2, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=0.44, bc='interface')
s12 = mcdc.surface('plane-z', z=0.64, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=11.0, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=15.0, bc='vacuum')
s16 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s17 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.75, bc='interface')
s18 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s19 = mcdc.surface('cylinder-y', center=[0.0, 0.64], radius=0.6, bc='interface')
s20 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.5, bc='interface')
s21 = mcdc.surface('plane-z', z=-16.0, bc='vacuum')
s22 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1 & -s10, fill=mvoid)
c2 = mcdc.cell(+s12 & -s2, fill=mvoid)
c3 = mcdc.cell(+s1 & -s3 & -s10 & +s16 & +s18, fill=m1)
c4 = mcdc.cell(+s2 & -s4 & +s12 & +s16 & +s19, fill=m1)
c5 = mcdc.cell(+s3 & -s5 & -s10 & +s17, fill=m4)
c6 = mcdc.cell(+s4 & -s6 & +s12 & +s17, fill=m4)
c7 = mcdc.cell(+s5 & -s7 & -s10, fill=m4)
c8 = mcdc.cell(+s6 & -s8 & +s12 & +s20, fill=m4)
c9 = mcdc.cell(+s10 & -s11 & -s15, fill=mvoid)
c10 = mcdc.cell(+s11 & -s12 & -s15, fill=m3)
c11 = mcdc.cell(+s7 & -s15 & -s10 & +s13 & +s21, fill=mvoid)
c12 = mcdc.cell(+s8 & -s15 & +s12 & -s22, fill=mvoid)
c13 = mcdc.cell(+s7 & -s9 & -s13 & -s10, fill=m2)
c14 = mcdc.cell(+s9 & -s14 & -s10 & +s21, fill=m2)
c15 = mcdc.cell(+s9 & +s14 & -s13 & -s10 & +s21, fill=mvoid)
c16 = mcdc.cell(+s1 & -s3 & -s10 & -s16, fill=mvoid)
c17 = mcdc.cell(+s2 & -s4 & +s12 & -s16, fill=mvoid)
c18 = mcdc.cell(+s3 & -s5 & -s17 & -s10, fill=mvoid)
c19 = mcdc.cell(+s4 & -s6 & +s12 & -s17, fill=mvoid)
c20 = mcdc.cell(+s1 & -s3 & -s10 & +s16 & -s18, fill=mvoid)
c21 = mcdc.cell(+s2 & -s4 & +s12 & +s16 & -s19, fill=mvoid)
c22 = mcdc.cell(+s6 & -s8 & +s12 & -s20, fill=mvoid)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

#	eigenvalue = 
   
# Simulation Parameters
