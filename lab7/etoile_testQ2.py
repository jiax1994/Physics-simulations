'''ceci est un programme qui teste les formes des orbites'''

#importation des modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

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



#definir la fonction qui calcule les positions
def position(kep,t,masse):
    
    #convertir le temps en tableau
    if not isinstance(t,np.ndarray): t=np.array([t])
    #calculer la periode et les autres parametres
    p=np.sqrt((kep[0]**3)/masse)
    Mtab=kep[2]+(2*np.pi)*(t/p)
    e=kep[1]
    err=1.e-6
    fy=fct(Mtab,e,err)
    #creer deux listes vides
    l1,l2=[],[]
    #calculer les positions pour tous les E
    for E in fy:
        
        r=kep[0]*(1-kep[1]*np.cos(E))
        v1=((1-kep[1])**(1/2))*np.cos(E/2)
        v2=((1+kep[1])**(1/2))*np.sin(E/2)
        theta=2*np.arctan2(v2,v1)
        #calculer les positions primes x1 et y1
        x1=r*np.cos(theta)
        y1=r*np.sin(theta)
        nb1=np.cos(kep[5])*np.cos(kep[3])
        nb2=np.cos(kep[4])*np.sin(kep[3])*np.sin(kep[5])
        nb3=np.sin(kep[5])*np.cos(kep[3])
        nb4=np.cos(kep[4])*np.sin(kep[3])*np.cos(kep[5])
        nb5=np.cos(kep[5])*np.sin(kep[3])
        nb6=np.cos(kep[4])*np.cos(kep[3])*np.sin(kep[5])
        nb7=np.sin(kep[5])*np.sin(kep[3])
        nb8=np.cos(kep[4])*np.cos(kep[3])*np.cos(kep[5])
        #calculer les positions finales x et y
        x=(nb1-nb2)*x1-(nb3+nb4)*y1
        y=(nb5+nb6)*x1-(nb7-nb8)*y1
        l1.append(x)
        l2.append(y)
        x=np.asarray(l1)
        y=np.asarray(l2)
    return x,y,t
#definir les parametres
kep=np.array([5,0,3,0.5,0,0.7])
masse=0.85
P=np.sqrt((kep[0]**3)/masse)
t=np.linspace(0,P,120)
#calculer les positions
pos=position(kep,t,masse)
#tracer la courbe
plt.plot(pos[0],pos[1],'b')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
