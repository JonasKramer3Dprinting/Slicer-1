import math

lineWidth = 0.4
placementX = 100
placementY = 100

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