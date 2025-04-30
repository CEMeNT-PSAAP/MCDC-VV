import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.042023],
	['U238',0.0043613],
	['C0',0.0010919],
	['Fe54',1.1359757500000001e-05],
	['Fe56',0.00017832389900000002],
	['Fe57',4.1182765e-06],
	['Fe58',5.48067e-07],
	['W180',6.606e-08],
	['W182',1.4588250000000002e-05],
	['W183',7.877655000000001e-06],
	['W184',1.686732e-05],
	['W186',1.5650715e-05]])
# Material Name: Steel reflector 1
m2 = mcdc.material(nuclides=[
	['Fe54',0.00464192365],
	['Fe56',0.07286827418],
	['Fe57',0.0016828462300000002],
	['Fe58',0.00022395594],
	['C0',0.0011269],
	['Si28',0.00014816698092000002],
	['Si29',7.523496540000001e-06],
	['Si30',4.95952254e-06],
	['Cr50',1.1310904e-05],
	['Cr52',0.0002181195248],
	['Cr53',2.4733003199999997e-05],
	['Cr54',6.156567999999999e-06],
	['Mn55',0.00032851],
	['Ni58',0.00015700575447],
	['Ni60',6.047833552999999e-05],
	['Ni61',2.6289513699999997e-06],
	['Ni62',8.38224735e-06],
	['Ni64',2.1347112800000003e-06],
	['Cu63',0.000147296415],
	['Cu65',6.571358499999999e-05]])
# Material Name: Steel reflector 2
m3 = mcdc.material(nuclides=[
	['Fe54',0.0046201802500000005],
	['Fe56',0.0725269493],
	['Fe57',0.0016749635500000002],
	['Fe58',0.00022290690000000002],
	['C0',0.0011217],
	['Si28',0.00014747525832000001],
	['Si29',7.488372840000002e-06],
	['Si30',4.93636884e-06],
	['Cr50',1.1257895e-05],
	['Cr52',0.00021709729900000002],
	['Cr53',2.4617091e-05],
	['Cr54',6.127715e-06],
	['Mn55',0.00032697],
	['Ni58',0.00015627052395],
	['Ni60',6.0195126049999996e-05],
	['Ni61',2.6166404499999996e-06],
	['Ni62',8.34299475e-06],
	['Ni64',2.1247148e-06],
	['Cu63',0.000146604915],
	['Cu65',6.5405085e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.89, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.55, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=11.0, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=17.25, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
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

