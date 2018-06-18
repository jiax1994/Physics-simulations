'''ceci est le calcul sans être vectorisé'''
import numpy as np
import time
x=np.linspace(0,10,100000)
tDebut=time.time()
for i in range(100):
    for i in range(x.size):
        x[i]+=2
    
tFin=time.time()
dt=tFin-tDebut
print('Temps écoulé:',dt)



