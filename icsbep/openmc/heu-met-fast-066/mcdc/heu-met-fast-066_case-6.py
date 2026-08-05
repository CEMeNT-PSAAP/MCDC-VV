import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: Beryllium (source)
# S(a,b): c_Be (Not Implemented)
m1 = mcdc.material(nuclides=[
	['Be9',0.11862]])
# Material Name: Nickel
m2 = mcdc.material(nuclides=[
	['Ni58',0.06214740200999999],
	['Ni60',0.023939067989999993],
	['Ni61',0.0010406147099999998],
	['Ni62',0.0033179350500000004],
	['Ni64',0.0008449802400000001]])
# Material Name: Air
m3 = mcdc.material(nuclides=[
	['N14',3.8453626515e-05],
	['N15',1.41373485e-07],
	['O16',1.0382063706e-05],
	['O17',3.936294e-09],
	['Ar36',1.5398976e-09],
	['Ar38',2.9034640000000003e-10],
	['Ar40',4.59769756e-07],
	['C0',1.6307e-08]])
# Material Name: Beryllium (moderator/reflector)
# S(a,b): c_Be (Not Implemented)
m4 = mcdc.material(nuclides=[
	['Be9',0.12295]])
# Material Name: HEU
# Depletable
m5 = mcdc.material(nuclides=[
	['U235',0.044575],
	['U238',0.002754]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.4983, bc='interface')
s2 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.5207, bc='interface')
s3 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=0.5555, bc='interface')
s4 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=4.0895, bc='interface')
s5 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=7.479, bc='interface')
s6 = mcdc.surface('sphere', center=[0.0, 0.0, 0.0], radius=13.119, bc='vacuum')

# Material Cell(s)
c1 = mcdc.cell(-s1, fill=m1)
c2 = mcdc.cell(+s1 & -s2, fill=m2)
c3 = mcdc.cell(+s2 & -s3, fill=m3)
c4 = mcdc.cell(+s3 & -s4, fill=m4)
c5 = mcdc.cell(+s4 & -s5, fill=m5)
c6 = mcdc.cell(+s5 & -s6, fill=m4)
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

