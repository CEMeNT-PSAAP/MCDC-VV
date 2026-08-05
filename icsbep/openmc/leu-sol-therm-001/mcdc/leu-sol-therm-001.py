import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: SS304L
m1 = mcdc.material(nuclides=[
	['Cr50',0.0007103206000000001],
	['Cr52',0.013697825720000001],
	['Cr53',0.00155322348],
	['Cr54',0.00038663020000000007],
	['Mn55',0.0017192],
	['Fe54',0.0035092211000000003],
	['Fe56',0.055087266520000004],
	['Fe57',0.00127220522],
	['Fe58',0.00016930716],
	['Ni58',0.0049299929442],
	['Ni60',0.0018990244557999995],
	['Ni61',8.25492782e-05],
	['Ni62',0.000263203221],
	['Ni64',6.70301008e-05]])
# Material Name: Air
m2 = mcdc.material(nuclides=[
	['N14',3.5085011118e-05],
	['N15',1.2898888199999999e-07],
	['O16',1.5086280132e-05],
	['O17',5.719868e-09]])
# Material Name: Fuel Solution
# S(a,b): c_H_in_H2O (Not Implemented)
# Depletable
m3 = mcdc.material(nuclides=[
	['U235',0.00012377],
	['U238',0.0023508],
	['H1',0.056179],
	['O16',0.032954505507],
	['O17',1.2494493000000001e-05],
	['F19',0.0051035]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-40.0, bc='vacuum')
s2 = mcdc.surface('plane-z', z=-37.1425, bc='interface')
s3 = mcdc.surface('plane-z', z=7.6575, bc='interface')
s4 = mcdc.surface('plane-z', z=39.375, bc='interface')
s5 = mcdc.surface('plane-z', z=41.28, bc='vacuum')
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=2.54, bc='interface')
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=3.175, bc='interface')
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=24.4475, bc='interface')
s9 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=25.4, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(+s1 & -s2 & -s6, fill=m2)
c2 = mcdc.cell(+s1 & -s2 & +s6 & -s9, fill=m1)
c3 = mcdc.cell(+s2 & -s4 & -s6, fill=m2)
c4 = mcdc.cell(+s2 & -s4 & +s6 & -s7, fill=m1)
c5 = mcdc.cell(+s2 & -s3 & +s7 & -s8, fill=m3)
c6 = mcdc.cell(+s3 & -s4 & +s7 & -s8, fill=m2)
c7 = mcdc.cell(+s2 & -s4 & +s8 & -s9, fill=m1)
c8 = mcdc.cell(+s4 & -s5 & -s6, fill=m2)
c9 = mcdc.cell(+s4 & -s5 & +s6 & -s9, fill=m1)
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
mcdc.source(x=[-10.0,10.0], y=[-10.0,10.0], z=[-40.0,40.0], prob=1.0)

mcdc.run()

