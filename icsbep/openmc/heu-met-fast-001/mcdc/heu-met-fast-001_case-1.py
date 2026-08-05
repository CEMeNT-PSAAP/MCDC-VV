import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

m1 = mcdc.material(nuclides=[
	['U235',0.044936],
	['U238',0.0027213]])
m2 = mcdc.material(nuclides=[
	['U235',0.045244],
	['U238',0.0024168]])
m3 = mcdc.material(nuclides=[
	['U235',0.045268],
	['U238',0.002393]])
m4 = mcdc.material(nuclides=[
	['U235',0.04509],
	['U238',0.002569]])
m5 = mcdc.material(nuclides=[
	['U235',0.045239],
	['U238',0.0024215]])
m6 = mcdc.material(nuclides=[
	['U235',0.044874],
	['U238',0.0024169]])
m7 = mcdc.material(nuclides=[
	['N14',3.5214e-05],
	['O16',1.5092e-05]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.0216, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=1.0541, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.2809, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=6.2937, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.7525, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.762, bc='interface')
s7 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.2527, bc='interface')
s8 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.261, bc='interface')
s9 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.7062, bc='interface')
s10 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=8.7499, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m7)
c3 = mcdc.cell(+s2 & -s3, fill=m2)
c4 = mcdc.cell(+s3 & -s4, fill=m7)
c5 = mcdc.cell(+s4 & -s5, fill=m3)
c6 = mcdc.cell(+s5 & -s6, fill=m7)
c7 = mcdc.cell(+s6 & -s7, fill=m4)
c8 = mcdc.cell(+s7 & -s8, fill=m7)
c9 = mcdc.cell(+s8 & -s9, fill=m5)
c10 = mcdc.cell(+s9 & -s10, fill=m6)
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

