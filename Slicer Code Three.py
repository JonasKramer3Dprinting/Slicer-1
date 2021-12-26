import math

pi = 3.141592653590

tei = 0
te = 0
tbi = 0
tb = 0
lhi = 0
lh = 0
lwi = 0
lw = 0
fti = 0
ft = 0
fei = 0
fe = 0
rd = 0

lineDistance = 0
lineWidth = 0
lineHeigth = 0
travelSpeed = 0
extrusionSpeed = 0
extruderTemperature = 0
bedTemperature = 0
retractionDistance = 0

X = 0
Y = 0
Z = 0
x = 0
y = 0
z = 0
i = 0
j = 0
r = 0
e = 0

gCodeStart = ""
gCodeFirstLayer = ""
gCodeMiddle = ""
gCodeEnd = ""


def find_factor(x, y, X, Y, lineWidth, lineHeigth, pi):
    lineDistance = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
    e = (lineDistance * lineWidth * lineHeigth * 4) / (1.75 ** 2 * pi)
    return e


def g0(x, y, z, travelSpeed):
    s = "G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " F" + str(travelSpeed) + "\n"
    return s


def g1(x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeigth, pi):
    s = (
        "G1 X"
        + str(x)
        + " Y"
        + str(y)
        + " Z"
        + str(z)
        + " E"
        + str(find_factor(x, y, X, Y, lineWidth, lineHeigth, pi))
        + " F"
        + str(extrusionSpeed)
        + "\n"
    )
    return s


def g1retract(retractionDistance):
    s = "G1 E-" + str(retractionDistance) + "\n"
    return s


def g1retractreversed(retractionDistance):
    s = "G1 E" + str(retractionDistance) + "\n"
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


def g92(x, y, z):
    x = 0
    y = 0
    z = 0
    s = "G92 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n"
    return s


def m82():
    s = "M82; extruder changes to absolutive positioning \n"
    return s


def m83():
    s = "M83; extruder changes to relative positioning \n"
    return s


def m104(extruderTemperature):
    s = "M104 S" + str(extruderTemperature) + "\n"
    return s


def m109(extruderTemperature):
    s = "M109 S" + str(extruderTemperature) + "\n"
    return s


def m140(bedTemperature):
    s = "M140 S" + str(bedTemperature) + "\n"
    return s


def m190(bedTemperature):
    s = "M190 S" + str(bedTemperature) + "\n"
    return s


def printSettings():
    global tei
    global te
    global tbi
    global tb
    global lhi
    global lh
    global lwi
    global lw
    global fti
    global ft
    global fei
    global fe
    global rd
    tei = float(input("Initial Layer Extruder Temperature: "))
    te = float(input("Extruder Temperature: "))
    tbi = float(input("Initial Layer Bed Temperature: "))
    tb = float(input("Bed Temperature: "))
    lhi = float(input("Initial Layer Heigth: "))
    lh = float(input("Layer Heigth: "))
    lwi = float(input("Initial Layer Line Width: "))
    lw = float(input("Line Width: "))
    fti = float(input("Initial Layer Travel Speed: "))
    ft = float(input("Travel Speed: "))
    fei = float(input("Initial Layer Extrusion Speed: "))
    fe = float(input("Extrusion Speed: "))
    rd = float(input("Retract Distance: "))


def changeOne():
    global extruderTemperature
    global bedTemperature
    global lineHeigth
    global lineWidth
    global travelSpeed
    global extrusionSpeed
    global retractionDistance
    extruderTemperature = tei
    bedTemperature = tbi
    lineHeigth = 0.2
    lineWidth = 0.8
    travelSpeed = 1200
    extrusionSpeed = 1200
    retractionDistance = 10


def changeTwo():
    global extruderTemperature
    global bedTemperature
    global lineHeigth
    global lineWidth
    global travelSpeed
    global extrusionSpeed
    global retractionDistance
    extruderTemperature = tei
    bedTemperature = tbi
    lineHeigth = lhi
    lineWidth = lwi
    travelSpeed = fti
    extrusionSpeed = fei
    retractionDistance = rd


def changeThree():
    global extruderTemperature
    global bedTemperature
    global lineHeigth
    global lineWidth
    global travelSpeed
    global extrusionSpeed
    global retractionDistance
    extruderTemperature = te
    bedTemperature = tb
    lineHeigth = lh
    lineWidth = lw
    travelSpeed = ft
    extrusionSpeed = fe
    retractionDistance = rd


printSettings()

changeOne()
z = lineHeigth
list = [10, 10, 10, 210, 10.8, 210, 10.8, 10, 11.6, 10, 11.6, 210, 12.4, 210, 12.4, 10]
gCodeStart = (
    m104(extruderTemperature)
    + m140(bedTemperature)
    + g17()
    + g21()
    + g28()
    + g90()
    + g92(x, y, z)
    + m82()
    + g0(0, 0, 10, travelSpeed)
    + m109(extruderTemperature)
    + m190(bedTemperature)
    + g1retractreversed(50)
    + g0(list[0], list[1], lineHeigth, travelSpeed)
)
for a in range(0, len(list) - 2, 2):
    X = list[a]
    Y = list[a + 1]
    x = list[a + 2]
    y = list[a + 3]
    gCodeStart = gCodeStart + g1(
        x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeigth, pi
    )
X = list[-2]
Y = list[-1]
x = list[0]
y = list[1]
gCodeStart = (
    gCodeStart
    + g1(x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeigth, pi)
    + g1retract(retractionDistance)
)
gCodeStart = gCodeStart + g0(10, 10, 10, travelSpeed)

gCode = gCodeStart + gCodeFirstLayer + gCodeMiddle + gCodeEnd
print(gCode)

name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(gCode)
