;FLAVOR:Marlin 
;Layer height: 0.12 
;Generated with Cura_SteamEngine 4.9.0 
M140 S70.0
M105 
M190 S70.0
M104 S210.0
M105 
M109 S210.0
M83 ;relative extrusion mode 
; Ender 3 Custom Start G-code 
G92 E0 ; Reset Extruder 
G28 ; Home all axes 
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed 
G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position 
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line 
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little 
G1 X0.4 Y20 Z0.3 F1500.0 E15 ; Draw the second line 
G92 E0 ; Reset Extruder 
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed 
G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish 
G92 E0 
G92 E0 
G1 F3000 E-8 
M104 S210.0
M140 S70.0
G0 X50 Y50 Z0.24 F1200.0
G1 E8
G1 X50 Y70 Z0.24 E0.7982432411073801 F1200.0
G1 X70 Y70 Z0.24 E0.7982432411073801 F1200.0
G1 X70 Y50 Z0.24 E0.7982432411073801 F1200.0
G1 X50 Y50 Z0.24 E0.7982432411073801 F1200.0
