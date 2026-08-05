import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Plutonium nitrate solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',8.7811e-05],
	['Pu240',2.8161e-06],
	['N14',0.00090422],
	['H1',0.064783],
	['O16',0.034833],
	['Fe54',7.1852585e-08],
	['Fe56',1.127931922e-06],
	['Fe57',2.6048866999999998e-08],
	['Fe58',3.4666260000000004e-09]])
# Material Name: 2S (1100) aluminum
m2 = mcdc.material(nuclides=[
	['Al27',0.059881],
	['Si28',0.00034835150136],
	['Si29',1.7688295320000002e-05],
	['Si30',1.166020332e-05],
	['Cu63',3.5518206e-05],
	['Cu65',1.5845794e-05],
	['Zn64',1.2271848600000001e-05],
	['Zn66',6.9208534e-06],
	['Zn67',1.0083032e-06],
	['Zn68',4.604751e-06],
	['Zn70',1.522438e-07],
	['Mn55',1.4853000000000002e-05]])
# Material Name: Water at 27 C
# S(a,b): c_H_in_H2O (Not Implemented)
m3 = mcdc.material(nuclides=[
	['H1',0.066622],
	['O16',0.033311]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=16.2487, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=16.3777, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=46.3777, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
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

