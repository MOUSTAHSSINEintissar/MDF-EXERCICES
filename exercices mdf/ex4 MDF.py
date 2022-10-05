H= float(input('Donner la hauteur en m'))
M=float(input('donner la valeur de la masse volumique'))
g= float(input('Donner la valeur de la gravité'))
L= float(input('Donner la valeur de la largeur en m'))

P =M*g*H
print("la pression est :",P,"Pa")
S= L*H
F=P*S
print(F"la force est :",F,"N")