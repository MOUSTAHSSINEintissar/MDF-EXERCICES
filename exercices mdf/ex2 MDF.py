m= float(input('Donner la masse'))
M=float(input('donner la valeur de la masse volumique de mercure'))
H= float(input('Donner la valeur de la hauteur en m'))
l= float(input('Donner la valeur de la longeur en m'))
L= float(input('Donner la valeur de la largeur en m'))
s=float(input('Donner la valeur de la surface en m^2'))
V =m/M
print("le volume versé de mercure est :",V,"m^3")
Vt=[V-(s*H)]/3
print("le volume de mercure dans chaque tube est :",V,"m^3")
h= Vt/s
print("la hauteur de mercure  est :",h,"m")