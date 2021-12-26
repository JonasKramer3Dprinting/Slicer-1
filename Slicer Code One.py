import math

gCode = ""
gCodeStartList = [
    "G17",
    "G21",
    "G28",
    "G91",
    "92 X0 Y0 Z0",
    "G0 X0 Y0 Z10",
    "M82",
    "M104 S210",
    "M140 S70",
    "M109 S210",
    "M190 S70",
    "G0 X10 Y10 Z10",
    "G0 X10 Y10 Z0.32",
]
for a in range(0, len(gCodeStartList), 1):
    gCode = gCode + gCodeStartList[a] + "\n"
print(gCode)
h = float(input("Layer heigth: "))
w = float(input("Line width: "))
xa = float(input("xa: "))
xb = float(input("xb: "))
ya = float(input("ya: "))
yb = float(input("yb: "))
d = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
print(d)
p = math.pi
a = (4 * h * w) / (1.75 ** 2 * p)
e = a * d
print(e)
