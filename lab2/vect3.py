'''ceci est le calcul en utilisant la liste'''
import numpy as np
import time
x=np.linspace(0,10,100000)
tDebut=time.time()
for i in range(100):
    for k in range(len(x)):
        x[k]+=2
    
tFin=time.time()
dt=tFin-tDebut
print('Temps écoulé:',dt)

