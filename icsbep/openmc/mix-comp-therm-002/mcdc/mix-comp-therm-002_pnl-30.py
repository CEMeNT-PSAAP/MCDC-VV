import mcdc
import numpy as np


##############################
#__________Materials__________
##############################

# Material Name: UO2-PuO2 Mixture
# Depletable
m1 = mcdc.material(nuclides=[
	['Pu238',3.8836e-08],
	['Pu239',0.00039462],
	['Pu240',3.3206e-05],
	['Pu242',1.1882e-07],
	['Am241',1.4954e-06],
	['U235',0.00014886],
	['U238',0.020611],
	['O16',0.043779]])
# Material Name: Natural UO2 Layer
# Depletable
m2 = mcdc.material(nuclides=[
	['U235',0.00014824],
	['U238',0.020525],
	['O16',0.041943]])
# Material Name: Cladding
m3 = mcdc.material(nuclides=[
	['Sn112',4.687816e-06],
	['Sn114',3.189648e-06],
	['Sn115',1.643152e-06],
	['Sn116',7.0268912e-05],
	['Sn117',3.7115904e-05],
	['Sn118',0.00011705041599999999],
	['Sn119',4.1513752000000004e-05],
	['Sn120',0.00015745262399999998],
	['Sn122',2.2375864e-05],
	['Sn124',2.7981912e-05],
	['Fe54',5.5902749000000005e-06],
	['Fe56',8.775536068e-05],
	['Fe57',2.02665398e-06],
	['Fe58',2.6971044e-07],
	['Cr50',3.3062408500000004e-06],
	['Cr52',6.375756377000001e-05],
	['Cr53',7.2295959300000005e-06],
	['Cr54',1.7995994500000002e-06],
	['Ni58',2.0651808383999998e-05],
	['Ni60',7.955039615999999e-06],
	['Ni61',3.4580006399999995e-07],
	['Ni62',1.10256192e-06],
	['Ni64',2.80790016e-07],
	['Zr90',0.021928504499999998],
	['Zr91',0.0047820762],
	['Zr92',0.0073095015],
	['Zr94',0.007407529800000001],
	['Zr96',0.001193388]])
# Material Name: Moderator
# S(a,b): c_H_in_H2O (Not Implemented)
m4 = mcdc.material(nuclides=[
	['H1',0.066706],
	['O16',0.033340359213],
	['O17',1.2640787000000002e-05],
	['B10',1.8706e-08],
	['B11',7.577e-08]])
# Material Name: 6061 Aluminum
m5 = mcdc.material(nuclides=[
	['Si28',0.00031917925357600004],
	['Si29',1.6207011812000003e-05],
	['Si30',1.0683734612e-05],
	['Fe54',5.933844e-06],
	['Fe56',9.31486608e-05],
	['Fe57',2.1512088e-06],
	['Fe58',2.862864e-07],
	['Cu63',4.40699865e-05],
	['Cu65',1.96610135e-05],
	['Mn55',2.2115e-05],
	['Mg24',0.0005262163101000001],
	['Mg25',6.6784302e-05],
	['Mg26',7.350938790000001e-05],
	['Cr50',2.7073695000000004e-06],
	['Cr52',5.220892590000001e-05],
	['Cr53',5.9200731000000005e-06],
	['Cr54',1.4736315e-06],
	['Zn64',1.5226473899999998e-05],
	['Zn66',8.587149099999998e-06],
	['Zn67',1.2510667999999998e-06],
	['Zn68',5.713411499999999e-06],
	['Zn70',1.888987e-07],
	['Ti46',2.0934375000000002e-06],
	['Ti47',1.8879000000000002e-06],
	['Ti48',1.8706449999999998e-05],
	['Ti49',1.3727875e-06],
	['Ti50',1.314425e-06],
	['Al27',0.058433]])
# Material Name: Lead
m6 = mcdc.material(nuclides=[
	['Pb204',0.000450436],
	['Pb206',0.007753934],
	['Pb207',0.007110454],
	['Pb208',0.016859176]])
mvoid = mcdc.material(nuclides=[['N14',1e-10]])
##############################
#__________Geometry__________
##############################

# Surface(s)
s1 = mcdc.surface('plane-z', z=-30.0, bc='vacuum')
s2 = mcdc.surface('plane-z', z=0.0, bc='interface')
s4 = mcdc.surface('plane-z', z=2.8575, bc='interface')
s5 = mcdc.surface('plane-z', z=3.175, bc='interface')
s6 = mcdc.surface('plane-z', z=3.556, bc='interface')
s7 = mcdc.surface('plane-z', z=4.056, bc='interface')
s8 = mcdc.surface('plane-z', z=5.715, bc='interface')
s9 = mcdc.surface('plane-z', z=92.3925, bc='interface')
s10 = mcdc.surface('plane-z', z=94.9325, bc='interface')
s11 = mcdc.surface('plane-z', z=94.996, bc='interface')
s12 = mcdc.surface('plane-z', z=95.8215, bc='interface')
s14 = mcdc.surface('plane-z', z=96.774, bc='interface')
s15 = mcdc.surface('plane-z', z=110.236, bc='vacuum')
s21 = mcdc.surface('plane-x', x=0.0, bc='reflective')
s23 = mcdc.surface('plane-y', y=0.0, bc='reflective')
s25 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=50.0, bc='vacuum')
s35 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.64135, bc='interface')
s36 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.71755, bc='interface')
s37 = mcdc.surface('plane-x', x=-0.73025, bc='interface')
s38 = mcdc.surface('plane-x', x=0.73025, bc='interface')
s39 = mcdc.surface('plane-y', y=-0.73025, bc='interface')
s40 = mcdc.surface('plane-y', y=0.73025, bc='interface')

# Material Cell(s)
c1 = mcdc.cell(+s21 & +s23 & -s25 & +s1 & -s2, fill=m4)
c2 = mcdc.cell(+s21 & +s23 & -s25 & +s2 & -s4, fill=m5)
c4 = mcdc.cell(+s21 & +s23 & -s25 & +s12 & -s14, fill=m6)
c5 = mcdc.cell(+s21 & +s23 & -s25 & +s14 & -s15, fill=m4)
c21 = mcdc.cell(-s6 & -s36, fill=m3)
c22 = mcdc.cell(+s6 & -s7 & -s35, fill=m2)
c23 = mcdc.cell(+s7 & -s11 & -s35, fill=m1)
c24 = mcdc.cell(+s6 & -s11 & +s35 & -s36, fill=m3)
c25 = mcdc.cell(+s11 & -s36, fill=m3)
c26 = mcdc.cell(-s5 & +s36, fill=m4)
c27 = mcdc.cell(+s5 & -s8 & -s37, fill=m5)
c28 = mcdc.cell(+s5 & -s8 & +s38, fill=m5)
c29 = mcdc.cell(+s5 & -s8 & -s39 & +s37 & -s38, fill=m5)
c30 = mcdc.cell(+s5 & -s8 & +s40 & +s37 & -s38, fill=m5)
c31 = mcdc.cell(+s5 & -s8 & +s37 & -s38 & +s39 & -s40 & +s36, fill=m4)
c32 = mcdc.cell(+s8 & -s9 & +s36, fill=m4)
c33 = mcdc.cell(+s9 & -s10 & -s37, fill=m5)
c34 = mcdc.cell(+s9 & -s10 & +s38, fill=m5)
c35 = mcdc.cell(+s9 & -s10 & -s39 & +s37 & -s38, fill=m5)
c36 = mcdc.cell(+s9 & -s10 & +s40 & +s37 & -s38, fill=m5)
c37 = mcdc.cell(+s9 & -s10 & +s37 & -s38 & +s39 & -s40 & +s36, fill=m4)
c38 = mcdc.cell(+s10 & +s36, fill=m4)
c41 = mcdc.cell(-s5, fill=m4)
c42 = mcdc.cell(+s5 & -s8 & -s37, fill=m5)
c43 = mcdc.cell(+s5 & -s8 & +s38, fill=m5)
c44 = mcdc.cell(+s5 & -s8 & -s39 & +s37 & -s38, fill=m5)
c45 = mcdc.cell(+s5 & -s8 & +s40 & +s37 & -s38, fill=m5)
c46 = mcdc.cell(+s5 & -s8 & +s37 & -s38 & +s39 & -s40, fill=m4)
c47 = mcdc.cell(+s8 & -s9, fill=m4)
c48 = mcdc.cell(+s9 & -s10 & -s37, fill=m5)
c49 = mcdc.cell(+s9 & -s10 & +s38, fill=m5)
c50 = mcdc.cell(+s9 & -s10 & -s39 & +s37 & -s38, fill=m5)
c51 = mcdc.cell(+s9 & -s10 & +s40 & +s37 & -s38, fill=m5)
c52 = mcdc.cell(+s9 & -s10 & +s37 & -s38 & +s39 & -s40, fill=m4)
c53 = mcdc.cell(+s10, fill=m4)
# Root Universe Cells List:
u0_cells = []
# Material Universe(s)

# Rectangular Lattice 11
Lattice11 = mcdc.lattice(x=[-0.889, 1.778, 29], y=[-0.889, 1.778, 29], 