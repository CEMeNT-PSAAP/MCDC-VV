import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.033928],
	['Pu240',0.0035031999999999997],
	['Ga69',0.001328627232],
	['Ga71',0.0008817727679999999],
	['C0',0.00030244],
	['Fe54',1.9009693499999997e-05],
	['Fe56',0.0002984115342],
	['Fe57',6.8916237e-06],
	['Fe58',9.171486000000001e-07],
	['W180',8.891279999999999e-08],
	['W182',1.963491e-05],
	['W183',1.06028514e-05],
	['W184',2.27024016e-05],
	['W186',2.10649242e-05],
	['Ni58',0.0009711850554000001],
	['Ni60',0.0003740987446],
	['Ni61',1.62618134e-05],
	['Ni62',5.1849777e-05],
	['Ni64',1.3204609600000002e-05]])
# Material Name: HEU
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.041081],
	['U238',0.0041002],
	['C0',0.0003865],
	['Fe54',8.7832815e-06],
	['Fe56',0.0001378787358],
	['Fe57',3.1842213000000005e-06],
	['Fe58',4.2376140000000003e-07],
	['W180',1.4794799999999999e-08],
	['W182',3.267185e-06],
	['W183',1.7642799000000003e-06],
	['W184',3.7776056000000005e-06],
	['W186',3.5051346999999994e-06],
	['Cu63',0.00050912379],
	['Cu65',0.00022713621000000002],
	['Ni58',0.00023258472884999997],
	['Ni60',8.959122115e-05],
	['Ni61',3.8944683499999995e-06],
	['Ni62',1.2417269250000001e-05],
	['Ni64',3.1623124e-06]])
# Material Name: Iron
m3 = mcdc.material(nuclides=[
	['Fe54',0.0047446203],
	['Fe56',0.07448039196],
	['Fe57',0.00172007706],
	['Fe58',0.00022891068]])
# Material Name: Copper
m4 = mcdc.material(nuclides=[
	['Cu63',0.0569553975],
	['Cu65',0.025409602499999996]])
# Material Name: Duralumin
m5 = mcdc.material(nuclides=[
	['Al27',0.058077],
	['Mg24',0.000815721732],
	['Mg25',0.00010352663999999999],
	['Mg26',0.00011395162799999999],
	['Mn55',0.00018284],
	['Cu63',0.0007834003500000001],
	['Cu65',0.00034949965000000003]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.0, bc='interface')
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=5.5, bc='interface')
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=1.1, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 1.225], radius=5.35, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 1.225], radius=7.55, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.7, bc='interface')
s10 = mcdc.surface('plane-z', z=0.0, bc='interface')
s11 = mcdc.surface('plane-z', z=1.025, bc='interface')
s12 = mcdc.surface('plane-z', z=1.225, bc='interface')
s13 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=6.5, bc='interface')
s14 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.5, bc='interface')
s15 = mcdc.surface('cylinder-y', center=[0.0, 0.0], radius=0.6, bc='interface')
s16 = mcdc.surface('cylinder-y', center=[0.0, 1.225], radius=0.6, bc='interface')
s17 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=14.0, bc='vacuum')
s18 = mcdc.surface('plane-z', z=-14.7, bc='vacuum')
s19 = mcdc.surface('plane-z', z=9.0, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s5, fill=m1)
c3 = mcdc.cell(+s5 & -s6 & +s12, fill=mvoid)
c4 = mcdc.cell(+s5 & -s2 & +s11 & -s12, fill=mvoid)
c5 = mcdc.cell(+s5 & -s7 & -s10 & +s15, fill=m2)
c6 = mcdc.cell(+s3 & +s6 & -s8 & +s12 & +s16, fill=m2)
c7 = mcdc.cell(+s5 & -s7 & -s10 & -s15, fill=mvoid)
c8 = mcdc.cell(+s6 & -s8 & +s12 & -s16, fill=mvoid)
c9 = mcdc.cell(+s5 & +s10 & -s11 & -s17, fill=mvoid)
c10 = mcdc.cell(+s2 & +s11 & -s12 & -s17, fill=m5)
c11 = mcdc.cell(+s7 & -s10 & +s13 & -s17 & +s18, fill=mvoid)
c12 = mcdc.cell(+s8 & +s12 & -s17 & -s19, fill=mvoid)
c13 = mcdc.cell(+s7 & -s9 & -s13 & -s10, fill=m4)
c14 = mcdc.cell(+s9 & -s10 & -s14 & +s18, fill=m3)
c15 = mcdc.cell(+s9 & -s10 & -s13 & +s14 & +s18, fill=mvoid)
c16 = mcdc.cell(-s3 & +s6 & -s8 & +s12, fill=mvoid)
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
# Space Type: point
mcdc.source(point=[0.0,0.0,0.0], prob=1.0)

mcdc.run()

