import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.040892],
	['Pu240',0.0047716],
	['Fe54',1.7526817e-05],
	['Fe56',0.0002751335444],
	['Fe57',6.3540334000000005e-06],
	['Fe58',8.456052000000001e-07],
	['C0',0.0019577],
	['H1',0.0008189624349234001],
	['H2',1.275650766e-07],
	['N14',8.808715050700001e-05],
	['N15',3.23849493e-07],
	['O16',0.00013101032826],
	['O17',4.9671740000000006e-08]])
# Material Name: Layer 2
# Depletable
m2 = mcdc.material(nuclides=[
	['Pu239',0.042276],
	['Pu240',0.004606],
	['Fe54',1.5509123e-05],
	['Fe56',0.00024346006359999994],
	['Fe57',5.6225546e-06],
	['Fe58',7.482587999999999e-07],
	['C0',0.0011053],
	['H1',0.00020007883486860005],
	['H2',3.11651314e-08],
	['N14',2.1520879200000002e-05],
	['N15',7.91208e-08],
	['O16',3.200786442e-05],
	['O17',1.213558e-08]])
# Material Name: Layer 3
# Depletable
m3 = mcdc.material(nuclides=[
	['Pu239',0.041681],
	['Pu240',0.0047176],
	['Fe54',1.7743082e-05],
	['Fe56',0.0002785284424],
	['Fe57',6.4324363999999995e-06],
	['Fe58',8.560391999999999e-07],
	['C0',0.0011922],
	['H1',0.000275007163713],
	['H2',4.2836286999999996e-08],
	['N14',2.9579252856e-05],
	['N15',1.0874714400000001e-07],
	['O16',4.3994319831e-05],
	['O17',1.6680169000000002e-08]])
# Material Name: Layer 4
# Depletable
m4 = mcdc.material(nuclides=[
	['Pu239',0.042431],
	['Pu240',0.0043997],
	['Fe54',1.665825e-05],
	['Fe56',0.0002614989],
	['Fe57',6.03915e-06],
	['Fe58',8.036999999999999e-07],
	['C0',0.0013956],
	['H1',0.0004330125521208],
	['H2',6.74478792e-08],
	['N14',4.6574769402e-05],
	['N15',1.71230598e-07],
	['O16',6.9270736437e-05],
	['O17',2.6263563000000002e-08]])
# Material Name: Layer 5
# Depletable
m5 = mcdc.material(nuclides=[
	['Pu239',0.041407],
	['Pu240',0.0048168],
	['Fe54',2.12728775e-05],
	['Fe56',0.00033393868299999997],
	['Fe57',7.7121005e-06],
	['Fe58',1.026339e-06],
	['C0',0.0013617],
	['H1',0.0002608793643192],
	['H2',4.06356808e-08],
	['N14',2.8059838931000004e-05],
	['N15',1.03161069e-07],
	['O16',4.1733177129e-05],
	['O17',1.5822871e-08]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.8, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.35, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m3)
c5 = mcdc.cell(+s4 & -s5, fill=m4)
c6 = mcdc.cell(+s5 & -s6, fill=m5)
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

