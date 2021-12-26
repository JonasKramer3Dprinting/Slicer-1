import math
pi = 3.141592653590
x = 0
y = 0
z = 0
i = 0
j = 0
r = 0
e = 0
ft = 0
fe = 0
te = 0
tb = 0
def g0(x,y,z,ft):
    s = "G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " F" + str(ft) + "\n"
    return s
def g1(x,y,z,e,fe):
    s = "G1 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " E" + str(e) + " F" + str(fe) + "\n"
    return s
def g2p(x,y,z,i,j,e,fe):
    s = "G2 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " I" + str(i) + " J" + str(j) + " E" + str(e) + " F" + str(fe) + "\n"
    return s
def g2r(x,y,z,r,e,fe):
    s = "G2 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " R" + str(r) + " E" + str(e) + " F" + str(fe) + "\n"
    return s
def g3p(x,y,z,i,j,e,fe):
    s = "G3 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " I" + str(i) + " J" + str(j) + " E" + str(e) + " F" + str(fe) + "\n"
    return s
def g3r(x,y,z,r,e,fe):
    s = "G3 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " R" + str(r) + " E" + str(e) + " F" + str(fe) + "\n"
    return s
def g17():
    s = "G17; change to xy \n"
    return s
def g18():
    s = "G18; change to xz \n"
    return s
def g19():
    s = "G19; change to yz \n"
    return s
def g20():
    s = "G20; change to imperial system \n"
    return s
def g21():
    s = "G21; change to metric system \n"
    return s
def g28():
    s = "G28; homing \n"
    return s
def g90():
    s = "G90; change to absolutive positioning \n"
    return s
def g91():
    s = "G91; change to relative positioning \n"
    return s
def g92(x,y,z):
    s = "G92 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n"
    return s
def m82():
    s = "M82; extruder changes to absolutive positioning \n"
    return s
def m83():
    s = "M83; extruder changes to relative positioning \n"
    return s
def m104(te):
    s = "M104 S" + str(te) + "\n"
    return s
def m109(te):
    s = "M109 S" + str(te) + "\n"
    return s
def m140(tb):
    s = "M104 S" + str(tb) + "\n"
    return s
def m190(tb):
    s = "M109 S" + str(tb) + "\n"
    return s
gCode = ""
e = (200 * 0.2 * 0.8 * 4)/(1.75**2*pi)
ft = 1200
fe = 1200
te = 210
tb = 70
gCode = gCode + m104(te) + m140(tb) + g17() + g21() + g28() + g90() + g92(0,0,0) + m83() + g0(0,0,10,ft) + m109(te) + m190(tb) + g0(10,10,10,ft) + g0(10,10,0.2,ft) + g1(10,210,0.2,fe,e) + g0(10.8,210,0.2,ft) + g1(10.8,10,0.2,fe,e) + g0(10,10,10,ft) + m82()
print(gCode)