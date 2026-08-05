import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Depletable
m1 = mcdc.material(nuclides=[
	['U233',0.047253],
	['U238',0.00032975]])
# Material Name: Tungsten reflector
m2 = mcdc.material(nuclides=[
	['W180',6.17616e-05],
	['W182',0.01363902],
	['W183',0.0073650708],
	['W184',0.0157697952],
	['W186',0.0146323524],
	['Ni58',0.006611900835599999],
	['Ni60',0.0025468923643999996],
	['Ni61',0.00011071164759999998],
	['Ni62',0.000352997178],
	['Ni64',8.98979744e-05],
	['Cu63',0.0028195221],
	['Cu65',0.0012578779000000002],
	['Zr90',0.00040917155999999993],
	['Zr91',8.923041599999999e-05],
	['Zr92',0.00013639052],
	['Zr94',0.000138219664],
	['Zr96',2.226784e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=5.0444, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.4828, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
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

