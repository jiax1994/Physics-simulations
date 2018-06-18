'''Ceci est le calcul de numpy vectorisé'''
import numpy as np
import time
x=np.linspace(0,10,100000)
tDebut=time.time()
for i in range(100):
    x+=2
    
tFin=time.time()
dt=tFin-tDebut
print('Temps écoulé:',dt)


