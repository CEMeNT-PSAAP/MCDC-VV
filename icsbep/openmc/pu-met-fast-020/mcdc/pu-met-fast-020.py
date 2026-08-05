import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium alloy
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.03393],
	['Pu240',0.0035043],
	['Ga69',0.0013286873399999998],
	['Ga71',0.0008818126599999999],
	['C0',0.00030246],
	['Fe54',1.9010862500000002e-05],
	['Fe56',0.000298429885],
	['Fe57',6.8920475e-06],
	['Fe58',9.17205e-07],
	['W180',8.892e-08],
	['W182',1.96365e-05],
	['W183',1.060371e-05],
	['W184',2.270424e-05],
	['W186',2.1066629999999995e-05],
	['Ni58',0.0009658069802999997],
	['Ni60',0.00037202711970000006],
	['Ni61',1.6171761299999998e-05],
	['Ni62',5.1562651500000004e-05],
	['Ni64',1.3131487200000002e-05]])
# Material Name: Depleted Uranium
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.00023787],
	['U238',0.046738]])
# Material Name: Duralumin
m3 = mcdc.material(nuclides=[
	['Al27',0.058077],
	['Mg24',0.000815721732],
	['Mg25',0.00010352663999999999],
	['Mg26',0.00011395162799999999],
	['Mn55',0.00018284],
	['Cu63',0.0007834003500000001],
	['Cu65',0.00034949965000000003]])
# Material Name: Fe
m4 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.61], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.61], radius=5.35, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.61], radius=9.15, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.0, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.61], radius=13.0, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.2, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=0.41, bc='interface')
s12 = mcdc.surface('plane-z', z=0.61, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=11.0, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=15.0, bc='vacuum')
s16 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.5, bc='interface')
s17 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.75, bc='interface')
s18 = mcdc.surface('plane-z', z=-16.2, bc='vacuum')
s19 = mcdc.surface('plane-z', z=14.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s3 & -s10, fill=m1)
c2 = mcdc.cell(+s2 & -s4 & +s12, fill=m1)
c3 = mcdc.cell(+s3 & -s5 & -s10 & +s17, fill=m2)
c4 = mcdc.cell(+s4 & -s6 & +s12 & +s17, fill=m2)
c5 = mcdc.cell(+s5 & -s7 & -s10, fill=m2)
c6 = mcdc.cell(+s6 & -s8 & +s12 & +s16, fill=m2)
c7 = mcdc.cell(+s7 & -s9 & -s13 & -s10, fill=m3)
c8 = mcdc.cell(+s9 & +s18 & -s14 & -s10, fill=m3)
c9 = mcdc.cell(+s11 & -s12 & -s15, fill=m4)
c10 = mcdc.cell(-s1 & -s10, fill=mvoid)
c11 = mcdc.cell(-s2 & +s12, fill=mvoid)
c12 = mcdc.cell(+s10 & -s11 & -s15, fill=mvoid)
c13 = mcdc.cell(+s7 & -s15 & -s10 & +s13 & +s18, fill=mvoid)
c14 = mcdc.cell(+s8 & -s15 & +s12 & -s19, fill=mvoid)
c15 = mcdc.cell(+s9 & +s18 & +s14 & -s13 & -s10, fill=mvoid)
c16 = mcdc.cell(+s3 & -s5 & -s17 & -s10, fill=mvoid)
c17 = mcdc.cell(+s4 & -s6 & -s17 & +s12, fill=mvoid)
c18 = mcdc.cell(+s6 & -s8 & +s12 & -s16, fill=mvoid)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

##############################
#__________Settings__________
##############################

#	eigenvalue = 
   
# Simulation Parameters
