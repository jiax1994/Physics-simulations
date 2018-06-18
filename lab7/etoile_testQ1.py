''' ceci est un programme qui teste la validite de E'''
#importation des modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#generer quelques valeurs aleatoires pour la fonction fct
rdm=np.random
Mtab=rdm.random(10)*2*np.pi
e=rdm.random()
err=1.e-6

#definir la fonction qui calcule E
def fct(Mtab,e,err):
    #creer une liste vide
    l=[]
    #definir les valeurs initiales
    for M in Mtab:
        if 0<=M%(2*np.pi)<np.pi:
            E=M+(e/2)
        elif np.pi<=M%(2*np.pi)<2*np.pi:
            E=M-(e/2)
        prec=1
        #methode de newton
        while prec>err:
            dE=-(M-E+e*np.sin(E))/(-1+e*np.cos(E))
            E+=dE
            prec=abs(dE)
        l.append(E)
    E=np.asarray(l)
    return E
#calculer E et la fonction f(E)
y=fct(Mtab,e,err)
z=Mtab-y+e*np.sin(y)
