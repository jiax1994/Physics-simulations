'''ceci est un programme qui trace l orbite et les positions mesurees et calculees'''
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

#definir le calcul de ki carre
def ki(kep,t,masse,x,sigx,y,sigy):
    pos=position(kep,t,masse)
    #x et y calcules par le modele
    xm=pos[0]
    ym=pos[1] 
    k1=((x-xm)/sigx)**2
    k2=((y-ym)/sigy)**2
    kcarre=np.sum(k1+k2)
     
    return kcarre

    

    
#lire les documents des positions mesurees
t,x,sigx,y,sigy=np.loadtxt('mesuresOrbite.txt',unpack=True)
''' cette partie suivante permet de generer le kep0, une fois on trouve les valeurs approximatives, on desactive cette partie du code'''
#while True:
    #rdm=np.random
    #a=rdm.random()*10
    #e=rdm.random()
    #M0=rdm.random()*2*np.pi
    #omega=rdm.random()*np.pi
    #i=rdm.random()*np.pi
    #w=rdm.random()*2*np.pi
    #kep0=np.array([a,e,M0,omega,i,w])

#definir kep0 par la partie precedente
kep0=np.array([4.2,0.3,1.5,4.1,0.75,2.7])
masse=0.85
#definir les bornes
bnds=((0,10),(0,1),(0,2*np.pi),(0,2*np.pi),(0,np.pi),(0,2*np.pi))
#minimiser le ki carre
res=minimize(ki,kep0,args=(t,masse,x,sigx,y,sigy),method='SLSQP',bounds=bnds)
#definir kep reel
kep=res.x

#tracer les points et la courbe
P=np.sqrt((kep[0]**3)/masse)
pos=position(kep,t,masse)
t=np.linspace(0,P,150)
poscomplet=position(kep,t,masse)
plt.plot(pos[0],pos[1],'bo')
plt.plot(poscomplet[0],poscomplet[1],'g')
plt.plot(x,y,'ro')
xerr=sigx
yerr=sigy
plt.errorbar(x,y,xerr,yerr,fmt='rs',ecolor='r')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



