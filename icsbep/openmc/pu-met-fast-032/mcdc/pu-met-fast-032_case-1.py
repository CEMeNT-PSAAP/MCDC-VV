import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Layer 1
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu239',0.041607],
	['Pu240',0.0048551],
	['Fe54',1.7833095e-05],
	['Fe56',0.000279941454],
	['Fe57',6.4650689999999995e-06],
	['Fe58',8.603819999999999e-07],
	['C0',0.001992],
	['H1',0.0008332902031692],
	['H2',1.2979683079999999e-07],
	['N14',8.9628483846e-05],
	['N15',3.29516154e-07],
	['O16',0.00013330945656],
	['O17',5.0543440000000006e-08]])
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
# Material Name: Steel reflector
m5 = mcdc.material(nuclides=[
	['Fe54',0.0046715578],
	['Fe56',0.07333346696],
	['Fe57',0.0016935895599999998],
	['Fe58',0.00022538567999999998],
	['C0',0.0011341],
	['Si28',0.000149107723656],
	['Si29',7.5712647719999995e-06],
	['Si30',4.991011571999999e-06],
	['Cr50',1.1383031e-05],
	['Cr52',0.0002195104222],
	['Cr53',2.48907198e-05],
	['Cr54',6.195827e-06],
	['Mn55',0.00033061],
	['Ni58',0.00015800648489999999],
	['Ni60',6.086381509999999e-05],
	['Ni61',2.6457078999999998e-06],
	['Ni62',8.435674500000001e-06],
	['Ni64',2.1483176e-06],
	['Cu63',0.000148236855],
	['Cu65',6.6133145e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.7, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.4, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=3.15, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.02, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.66, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=9.15, bc='vacuum')

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

