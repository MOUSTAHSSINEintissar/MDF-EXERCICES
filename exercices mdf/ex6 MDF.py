M=float(input('Donner la valeur du masse volumique du mercure'))
M1=float(input('Donner la valeur du masse volumique du platine'))
M2=float(input('Donner la valeur du masse volumique du zinc'))
min=((M1-M)/(M-M2))
print("la valeur minimal de h2/h1 est :",min,"m")
import numpy as np
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)
print("la valeur maximal de h2/h1 est :",sol,"m")