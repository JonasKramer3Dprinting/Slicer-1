import math

#hier werden die Distanzunterschiede angegeben
xD = float(input("x-difference: "))
yD = float(input("y-difference: "))

# es kann nicht durch 0 geteilt werden
if xD == 0:
    xD = 10 ** -12
a = math.atan(yD / xD) / math.pi * 180

# für Winkel zwischen 90 und 270 Grad
if xD < 0:
    a = 180 + a

# für Winkel zwischen 270 und 360 Grad
if xD > 0 and yD < 0:
    a = 360 + a

# für einen Winkel vno 360 Grad
if a == 360:
    a = 0

print("The angle is: " + str(a))
