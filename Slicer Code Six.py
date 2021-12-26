import math
pi = math.pi

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

option = 0
placementX = 0
placementY = 0
list = []

def find_factor(x,y,X,Y,lineWidth,lineHeigth,pi):
    lineDistance = ((X - x)**2 + (Y - y)**2)**0.5
    e = (lineDistance * lineWidth * lineHeigth * 4)/(1.75**2 * pi)
    return e
def g0(x,y,z,travelSpeed):
    s = "G0 X" + str(x) + " Y" + str( y)+ " Z" + str(z) + " F" + str(travelSpeed) + "\n"
    return s
def g1(x,y,z,extrusionSpeed,X,Y,lineWidth,lineHeigth,pi):
    s = "G1 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " E" + str(find_factor(x,y,X,Y,lineWidth,lineHeigth,pi)) + " F" + str(extrusionSpeed) + "\n"
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
def g92(x,y,z):
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
    global retractionDistance
    extruderTemperature = tei
    bedTemperature = tbi
    lineHeigth = lh
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
    
def printOptions():
    global option
    option = int(input("What do you want to print? \nEnter 0 for printing a quader. \nEnter 1 for printing a zylinder. \nEnter 2 for printing an extruded equilateral polygon. \nEnter 3 for printing an extruded surface made of connected corners. \nEnter your number here: "))

def placement():
    global placementX
    global placementY
    print("Where should the object be placed?")
    placementX = float(input("Give the x-Coordinate, which should be between 60 and 180: "))
    placementY = float(input("Give the Y-Coordinate, which should be between 60 and 180: "))

def optionZero():
    global placementX
    global placementY
    global lineWidth
    global list
    list = []
    length = float(input("Give the length of the quader: "))
    width = float(input("Give the width of the quader: "))
    heigth = float(input("Give the heigth of the quader: "))
    local = 0
    if length < width:
        local = length
    else:
        local = width    
    l = length
    w = width
    local = round(local * 10**12,0)
    local = int(local)
    print(heigth,local)
    for a in range (0,local//int(lineWidth * 2 * 10**12),1):
        list.append(w/2 - lineWidth/2)
        list.append(l/2 - lineWidth/2)
        list.append(lineWidth/2 - w/2)
        list.append(l/2 - lineWidth/2)
        list.append(lineWidth/2 - w/2)
        list.append(lineWidth/2 - l/2)
        list.append(w/2 - lineWidth/2)
        list.append(lineWidth/2 - l/2)
        list.append(w/2 - lineWidth/2)
        list.append(l/2 - lineWidth/2)
        l = l - 2 * lineWidth
        w = w - 2 * lineWidth
        print(local)
        print(int(lineWidth * 2 * 10**12))
        print(local%(int(lineWidth * 2 * 10**12)))
    if local%(int(lineWidth * 2 * 10**12)) >= 10**12:
        if length > width:
            list.append(w/2 - lineWidth/2)
            list.append(l/2 - lineWidth/2)
            list.append(w/2 - lineWidth/2)
            list.append(lineWidth/2 - l/2)
        else:
            list.append(w/2 - lineWidth/2)
            list.append(l/2 - lineWidth/2)
            list.append(lineWidth/2 - w/2)
            list.append(l/2 - lineWidth/2)
    print(list)
    for a in range (0,len(list),2):
        list[a] = list[a] + placementX
        list[a + 1] = list[a + 1] + placementY
    print(list)    

printOptions()

printSettings()

changeOne()
gCodeStart = ";FLAVOR:Marlin \n;Layer height: " + str(lh) +" \n;Generated with Cura_SteamEngine 4.9.0 \n" + m140(bedTemperature) + "M105 \n" + m190(bedTemperature) + m104(extruderTemperature) + "M105 \n" + m109(extruderTemperature) + "M83 ;relative extrusion mode \n; Ender 3 Custom Start G-code \nG92 E0 ; Reset Extruder \nG28 ; Home all axes \nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position \nG1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line \nG1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little \nG1 X0.4 Y20 Z0.3 F1500.0 E15 ; Draw the second line \nG92 E0 ; Reset Extruder \nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish \nG92 E0 \nG92 E0 \nG1 F3000 E-8 \n"

list = [75.0, 50, 74.21457902821578, 56.21724717912137, 71.9076670010966, 62.04384185254288, 68.22421568553528, 67.11367764821722, 63.39566987447491, 71.10819813755037, 57.72542485937369, 73.77641290737884, 51.56976298823283, 74.9506682107068, 45.31546713535688, 74.55718126821722, 39.35551771087318, 72.62067631165048, 34.06440025628275, 69.26283106939474, 29.774575140626318, 64.69463130731182, 26.755587852793713, 59.20311381711694, 25.197132467138054, 53.1333308391076, 25.197132467138054, 46.86666916089241, 26.755587852793713, 40.79688618288305, 29.774575140626315, 35.30536869268818, 34.06440025628276, 30.737168930605264, 39.355517710873194, 27.379323688349505, 45.31546713535688, 25.442818731782783, 51.569762988232846, 25.049331789293213, 57.72542485937368, 26.22358709262116, 63.3956698744749, 28.89180186244961, 68.2242156855353, 32.886322351782795, 71.9076670010966, 37.95615814745712, 74.21457902821578, 43.782752820878635, 75.0, 50]
list = [102.2, 101.4, 97.8, 101.4, 97.8, 98.6, 102.2, 98.6, 102.2, 101.4, 101.8, 101.0, 98.2, 101.0, 98.2, 99.0, 101.8, 99.0, 101.8, 101.0, 101.4, 100.6, 98.6, 100.6, 98.6, 99.4, 101.4, 99.4, 101.4, 100.6, 101.0, 100.2, 99.0, 100.2, 99.0, 99.8, 101.0, 99.8, 101.0, 100.2]

changeTwo()

placement()

if option == 0:
    optionZero()
    print(list)

z = lineHeigth
gCodeFirstLayer = m104(extruderTemperature) + m140(bedTemperature) + g0(list[0],list[1],z,travelSpeed) + g1retractreversed(8)
for a in range (0,len(list) - 2,2):
    X = list[a]
    Y = list[a + 1]
    x = list[a + 2]
    y = list[a + 3]
    gCodeFirstLayer = gCodeFirstLayer + g1(x,y,z,extrusionSpeed,X,Y,lineWidth,lineHeigth,pi)

gCode = gCodeStart + gCodeFirstLayer + gCodeMiddle + gCodeEnd
print(gCode)

name = input("Name: ")
with open(name + ".gcode","w") as file:
    file.write(gCode)