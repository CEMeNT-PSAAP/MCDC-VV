import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: HEU
# Depletable
m1 = mcdc.material(nuclides=[
	['U235',0.042055],
	['U238',0.0043629],
	['C0',0.0010482],
	['Fe54',1.0821433000000001e-05],
	['Fe56',0.0001698733556],
	['Fe57',3.9231166e-06],
	['Fe58',5.220948e-07],
	['W180',6.205559999999999e-08],
	['W182',1.3703944999999999e-05],
	['W183',7.4001303e-06],
	['W184',1.58448632e-05],
	['W186',1.4702005899999999e-05]])
# Material Name: Duralumin reflector
m2 = mcdc.material(nuclides=[
	['Al27',0.053934],
	['Fe54',5.769131899999999e-05],
	['Fe56',0.0009056303308],
	['Fe57',2.09149538e-05],
	['Fe58',2.7833964e-06],
	['Cu63',0.00070263315],
	['Cu65',0.00031346685]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.018, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.35, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=12.25, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=mvoid)
c2 = mcdc.cell(+s1 & -s2, fill=m1)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
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

