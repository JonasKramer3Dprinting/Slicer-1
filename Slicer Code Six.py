import math

pi = math.pi

# hier werden die globalen Variablen aufgelistet
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

# hier ist die Funktion zur Extrusionsberechnung für lineare Bewegungen
def find_factor(x, y, X, Y, lineWidth, lineHeigth, pi):
    lineDistance = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
    e = (lineDistance * lineWidth * lineHeigth * 4) / (1.75 ** 2 * pi)
    return e


# nun werden alle Funktionen geschrieben, die als Rückgabe den benötigten gCode ausgeben
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


# hier wird die Funktion definiert, mit der die Druckeinstellungen gesetzt werden
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


# hier werden die Druckeinstellungen auf die Werte der ersten Extrusionslinien gesetzt
def changeOne():
    global extruderTemperature
    global bedTemperature
    global lineHeigth
    global retractionDistance
    extruderTemperature = tei
    bedTemperature = tbi
    lineHeigth = lh
    retractionDistance = 10


# hier werden die Druckeinstellungen auf die Werte der ersten Ebene gesetzt
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


# hier werden die Druckeinstellungen auf die Werte der zweiten bis zur letzten Ebene gesetzt
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


# mit dieser Funktion wird abgefragt, was genau gedruckt werden soll
def printOptions():
    global option
    option = int(
        input(
            "What do you want to print? \nEnter 0 for printing a quader. \nEnter 1 for printing a zylinder. \nEnter 2 for printing an extruded equilateral polygon. \nEnter 3 for printing an extruded surface made of connected corners. \nEnter your number here: "
        )
    )


# mit dieser Funktion wird abgefragt, wo das zu druckende Bauteil platziert wird
def placement():
    global placementX
    global placementY
    print("Where should the object be placed?")
    placementX = float(
        input("Give the x-Coordinate, which should be between 60 and 180: ")
    )
    placementY = float(
        input("Give the Y-Coordinate, which should be between 60 and 180: ")
    )


# mit dieser Funktion wird die erste Obtion verwirklicht innerhalb der ersten Ebene
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
    local = round(local * 10 ** 12, 0)
    local = int(local)
    print(heigth, local)
    for a in range(0, local // int(lineWidth * 2 * 10 ** 12), 1):
        list.append(w / 2 - lineWidth / 2)
        list.append(l / 2 - lineWidth / 2)
        list.append(lineWidth / 2 - w / 2)
        list.append(l / 2 - lineWidth / 2)
        list.append(lineWidth / 2 - w / 2)
        list.append(lineWidth / 2 - l / 2)
        list.append(w / 2 - lineWidth / 2)
        list.append(lineWidth / 2 - l / 2)
        list.append(w / 2 - lineWidth / 2)
        list.append(l / 2 - lineWidth / 2)
        l = l - 2 * lineWidth
        w = w - 2 * lineWidth
        print(local)
        print(int(lineWidth * 2 * 10 ** 12))
        print(local % (int(lineWidth * 2 * 10 ** 12)))
    if local % (int(lineWidth * 2 * 10 ** 12)) >= 10 ** 12:
        if length > width:
            list.append(w / 2 - lineWidth / 2)
            list.append(l / 2 - lineWidth / 2)
            list.append(w / 2 - lineWidth / 2)
            list.append(lineWidth / 2 - l / 2)
        else:
            list.append(w / 2 - lineWidth / 2)
            list.append(l / 2 - lineWidth / 2)
            list.append(lineWidth / 2 - w / 2)
            list.append(l / 2 - lineWidth / 2)
    print(list)
    for a in range(0, len(list), 2):
        list[a] = list[a] + placementX
        list[a + 1] = list[a + 1] + placementY
    print(list)


printOptions()

printSettings()

changeOne()

# mit folgendem Code wird der Startcode festgelegt
gCodeStart = (
    ";FLAVOR:Marlin \n;Layer height: "
    + str(lh)
    + " \n;Generated with Cura_SteamEngine 4.9.0 \n"
    + m140(bedTemperature)
    + "M105 \n"
    + m190(bedTemperature)
    + m104(extruderTemperature)
    + "M105 \n"
    + m109(extruderTemperature)
    + "M83 ;relative extrusion mode \n; Ender 3 Custom Start G-code \nG92 E0 ; Reset Extruder \nG28 ; Home all axes \nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position \nG1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line \nG1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little \nG1 X0.4 Y20 Z0.3 F1500.0 E15 ; Draw the second line \nG92 E0 ; Reset Extruder \nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed \nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish \nG92 E0 \nG92 E0 \nG1 F3000 E-8 \n"
)

# hier wird die Liste, die später von dem Extruder abgefahren wird festgelegtd
list = [
    75.0,
    50,
    74.21457902821578,
    56.21724717912137,
    71.9076670010966,
    62.04384185254288,
    68.22421568553528,
    67.11367764821722,
    63.39566987447491,
    71.10819813755037,
    57.72542485937369,
    73.77641290737884,
    51.56976298823283,
    74.9506682107068,
    45.31546713535688,
    74.55718126821722,
    39.35551771087318,
    72.62067631165048,
    34.06440025628275,
    69.26283106939474,
    29.774575140626318,
    64.69463130731182,
    26.755587852793713,
    59.20311381711694,
    25.197132467138054,
    53.1333308391076,
    25.197132467138054,
    46.86666916089241,
    26.755587852793713,
    40.79688618288305,
    29.774575140626315,
    35.30536869268818,
    34.06440025628276,
    30.737168930605264,
    39.355517710873194,
    27.379323688349505,
    45.31546713535688,
    25.442818731782783,
    51.569762988232846,
    25.049331789293213,
    57.72542485937368,
    26.22358709262116,
    63.3956698744749,
    28.89180186244961,
    68.2242156855353,
    32.886322351782795,
    71.9076670010966,
    37.95615814745712,
    74.21457902821578,
    43.782752820878635,
    75.0,
    50,
]
list = [
    102.2,
    101.4,
    97.8,
    101.4,
    97.8,
    98.6,
    102.2,
    98.6,
    102.2,
    101.4,
    101.8,
    101.0,
    98.2,
    101.0,
    98.2,
    99.0,
    101.8,
    99.0,
    101.8,
    101.0,
    101.4,
    100.6,
    98.6,
    100.6,
    98.6,
    99.4,
    101.4,
    99.4,
    101.4,
    100.6,
    101.0,
    100.2,
    99.0,
    100.2,
    99.0,
    99.8,
    101.0,
    99.8,
    101.0,
    100.2,
]

changeTwo()

placement()

# hier wird die erste Option verwendet, falls dies zuvor angegeben wurde
if option == 0:
    optionZero()
    print(list)

list = [119.74118095489749, 100.0, 117.09636420764676, 109.87059047744874, 109.87059047744874, 117.09636420764676, 100.0, 119.74118095489749, 90.12940952255127, 117.09636420764676, 82.90363579235324, 109.87059047744874, 80.25881904510251, 100.0, 82.90363579235324, 90.12940952255126, 90.12940952255126, 82.90363579235324, 100.0, 80.25881904510251, 109.87059047744874, 82.90363579235324, 117.09636420764676, 90.12940952255126, 119.74118095489749, 100.0, 119.22354286469243, 100.0, 116.64807647156273, 109.61177143234622, 109.61177143234622, 116.64807647156273, 100.0, 119.22354286469243, 90.38822856765378, 116.64807647156273, 83.35192352843727, 109.61177143234622, 80.77645713530757, 100.0, 83.35192352843727, 90.38822856765378, 90.38822856765377, 83.35192352843727, 100.0, 80.77645713530757, 109.61177143234622, 83.35192352843727, 116.64807647156273, 90.38822856765377, 119.22354286469243, 100.0, 118.7059047744874, 100.0, 116.1997887354787, 109.35295238724369, 109.3529523872437, 116.1997887354787, 100.0, 118.7059047744874, 90.64704761275631, 116.1997887354787, 83.8002112645213, 109.35295238724369, 81.2940952255126, 100.0, 83.8002112645213, 90.6470476127563, 90.6470476127563, 83.8002112645213, 100.0, 81.2940952255126, 109.3529523872437, 83.8002112645213, 116.1997887354787, 90.6470476127563, 118.7059047744874, 100.0, 118.18826668428235, 100.0, 115.75150099939468, 109.09413334214118, 109.09413334214118, 115.75150099939468, 100.0, 118.18826668428235, 90.90586665785882, 115.75150099939468, 84.24849900060532, 109.09413334214118, 81.81173331571765, 100.0, 84.24849900060532, 90.90586665785882, 90.90586665785881, 84.24849900060534, 100.0, 81.81173331571765, 109.09413334214118, 84.24849900060532, 115.75150099939466, 90.90586665785881, 118.18826668428235, 100.0, 117.6706285940773, 100.0, 115.30321326331065, 108.83531429703865, 108.83531429703865, 115.30321326331065, 100.0, 117.6706285940773, 91.16468570296135, 115.30321326331065, 84.69678673668935, 108.83531429703865, 82.3293714059227, 100.0, 84.69678673668935, 91.16468570296135, 91.16468570296134, 84.69678673668936, 100.0, 82.3293714059227, 108.83531429703865, 84.69678673668935, 115.30321326331064, 91.16468570296134, 117.6706285940773, 100.0, 117.15299050387226, 100.0, 114.85492552722661, 108.57649525193614, 108.57649525193614, 114.85492552722661, 100.0, 117.15299050387226, 91.42350474806388, 114.85492552722661, 85.14507447277339, 108.57649525193614, 82.84700949612774, 100.0, 85.14507447277339, 91.42350474806386, 91.42350474806386, 85.14507447277339, 100.0, 82.84700949612774, 108.57649525193614, 85.14507447277339, 114.85492552722661, 91.42350474806386, 117.15299050387226, 100.0, 116.63535241366722, 100.0, 114.40663779114259, 108.31767620683361, 108.31767620683361, 114.40663779114259, 100.0, 116.63535241366722, 91.68232379316639, 114.40663779114259, 85.59336220885741, 108.31767620683361, 
83.36464758633278, 100.0, 85.59336220885741, 91.68232379316639, 91.68232379316638, 85.59336220885741, 100.0, 83.36464758633278, 108.31767620683361, 85.59336220885741, 114.40663779114259, 91.68232379316638, 116.63535241366722, 100.0, 116.11771432346218, 100.0, 113.95835005505856, 108.05885716173108, 108.05885716173108, 113.95835005505856, 100.0, 116.11771432346218, 91.94114283826892, 113.95835005505856, 86.04164994494144, 108.05885716173108, 83.88228567653782, 100.0, 86.04164994494144, 91.94114283826892, 91.9411428382689, 86.04164994494144, 100.0, 83.88228567653782, 108.05885716173108, 86.04164994494144, 113.95835005505856, 91.9411428382689, 116.11771432346218, 100.0, 115.60007623325714, 100.0, 113.51006231897453, 107.80003811662857, 107.80003811662857, 113.51006231897453, 100.0, 115.60007623325714, 92.19996188337143, 113.51006231897453, 86.48993768102547, 107.80003811662857, 84.39992376674286, 100.0, 86.48993768102547, 92.19996188337143, 92.19996188337143, 86.48993768102547, 100.0, 84.39992376674286, 107.80003811662857, 86.48993768102547, 113.51006231897453, 92.19996188337143, 115.60007623325714, 100.0, 115.08243814305209, 100.0, 113.06177458289051, 107.54121907152604, 107.54121907152604, 113.06177458289051, 100.0, 115.08243814305209, 92.45878092847396, 113.06177458289051, 86.93822541710949, 107.54121907152604, 84.91756185694791, 100.0, 86.93822541710949, 92.45878092847396, 92.45878092847394, 86.93822541710949, 100.0, 84.91756185694791, 107.54121907152604, 86.93822541710949, 113.06177458289051, 92.45878092847394, 115.08243814305209, 100.0, 114.56480005284705, 100.0, 112.61348684680648, 107.28240002642353, 107.28240002642353, 112.61348684680648, 100.0, 114.56480005284705, 92.71759997357648, 112.61348684680648, 87.38651315319352, 107.28240002642353, 85.43519994715295, 100.0, 87.38651315319352, 92.71759997357647, 92.71759997357647, 87.38651315319352, 100.0, 85.43519994715295, 107.28240002642353, 87.38651315319352, 112.61348684680648, 92.71759997357647, 114.56480005284705, 100.0, 114.04716196264201, 100.0, 112.16519911072245, 107.023580981321, 107.023580981321, 112.16519911072245, 100.0, 114.04716196264201, 92.976419018679, 112.16519911072245, 87.83480088927755, 107.023580981321, 85.95283803735799, 100.0, 87.83480088927755, 92.976419018679, 92.97641901867898, 87.83480088927755, 100.0, 85.95283803735799, 107.023580981321, 87.83480088927755, 112.16519911072245, 92.97641901867898, 114.04716196264201, 100.0, 113.52952387243697, 100.0, 111.71691137463843, 106.76476193621849, 106.76476193621849, 111.71691137463843, 100.0, 113.52952387243697, 93.23523806378152, 111.71691137463843, 88.28308862536157, 106.76476193621849, 86.47047612756303, 100.0, 88.28308862536157, 93.23523806378151, 93.23523806378151, 88.28308862536157, 100.0, 86.47047612756303, 106.76476193621849, 88.28308862536157, 111.71691137463843, 93.23523806378151, 113.52952387243697, 100.0, 113.01188578223193, 100.0, 111.2686236385544, 106.50594289111596, 106.50594289111596, 111.2686236385544, 100.0, 113.01188578223193, 93.49405710888404, 111.2686236385544, 88.7313763614456, 106.50594289111596, 86.98811421776807, 100.0, 88.7313763614456, 93.49405710888404, 93.49405710888404, 88.7313763614456, 100.0, 86.98811421776807, 106.50594289111596, 88.7313763614456, 111.2686236385544, 93.49405710888404, 113.01188578223193, 100.0, 112.49424769202689, 100.0, 110.82033590247038, 106.24712384601344, 106.24712384601345, 110.82033590247038, 100.0, 112.49424769202689, 93.75287615398656, 110.82033590247038, 89.17966409752962, 106.24712384601344, 87.50575230797311, 100.0, 89.17966409752962, 93.75287615398655, 93.75287615398655, 89.17966409752962, 100.0, 87.50575230797311, 106.24712384601345, 89.17966409752962, 110.82033590247038, 93.75287615398655, 112.49424769202689, 100.0, 111.97660960182185, 100.0, 110.37204816638635, 105.98830480091092, 105.98830480091092, 110.37204816638635, 100.0, 111.97660960182185, 94.01169519908908, 110.37204816638635, 89.62795183361365, 105.98830480091092, 88.02339039817815, 100.0, 89.62795183361365, 94.01169519908908, 94.01169519908908, 89.62795183361365, 100.0, 88.02339039817815, 105.98830480091092, 89.62795183361365, 110.37204816638635, 94.01169519908908, 111.97660960182185, 100.0, 111.45897151161681, 100.0, 109.92376043030232, 105.7294857558084, 105.7294857558084, 109.92376043030232, 100.0, 111.45897151161681, 94.2705142441916, 109.92376043030232, 90.07623956969768, 105.7294857558084, 88.54102848838319, 100.0, 90.07623956969768, 94.2705142441916, 94.27051424419159, 90.07623956969768, 100.0, 88.54102848838319, 105.7294857558084, 90.07623956969768, 109.92376043030232, 94.27051424419159, 111.45897151161681, 100.0, 110.94133342141177, 100.0, 109.4754726942183, 105.47066671070588, 105.47066671070588, 109.4754726942183, 100.0, 110.94133342141177, 94.52933328929412, 109.4754726942183, 90.5245273057817, 105.47066671070588, 89.05866657858823, 100.0, 90.5245273057817, 94.52933328929412, 94.52933328929412, 90.5245273057817, 100.0, 89.05866657858823, 105.47066671070588, 90.5245273057817, 109.4754726942183, 94.52933328929412, 110.94133342141177, 100.0, 110.42369533120672, 100.0, 109.02718495813427, 105.21184766560336, 105.21184766560336, 109.02718495813427, 100.0, 110.42369533120672, 94.78815233439664, 109.02718495813427, 90.97281504186573, 105.21184766560336, 89.57630466879328, 100.0, 90.97281504186573, 94.78815233439664, 94.78815233439664, 90.97281504186573, 100.0, 89.57630466879328, 105.21184766560336, 90.97281504186573, 109.02718495813427, 94.78815233439664, 110.42369533120672, 100.0, 109.90605724100168, 100.0, 108.57889722205024, 104.95302862050085, 104.95302862050085, 108.57889722205024, 100.0, 109.90605724100168, 95.04697137949915, 108.57889722205024, 91.42110277794976, 104.95302862050085]

# hier wird der Code für die erste Schicht angefangen zu schreiben
z = lineHeigth
gCodeFirstLayer = (
    m104(extruderTemperature)
    + m140(bedTemperature)
    + g0(list[0], list[1], z, travelSpeed)
    + g1retractreversed(8)
)

# hier werden die vier gegebenen Punkte abgefahren
print(len(list))
for a in range(0, len(list) - 2, 2):
    print(a)
    X = list[a]
    Y = list[a + 1]
    x = list[a + 2]
    y = list[a + 3]
    gCodeFirstLayer = gCodeFirstLayer + g1(
        x, y, z, extrusionSpeed, X, Y, lineWidth, lineHeigth, pi
    )

# hier werdden die verschiedenen Codes addiert
gCode = gCodeStart + gCodeFirstLayer + gCodeMiddle + gCodeEnd
print(gCode)

# hier wird der Code abgespeichert
name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(gCode)
