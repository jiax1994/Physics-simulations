'''ceci est un programme qui trace les orbites lies et non liees'''

#importation des modules
import numpy as np
import matplotlib.pyplot as plt

#definir les fonctions du et dv
def du(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*x)/(n1**(1.5))

def dv(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*y)/(n1**(1.5))


h=1/3650                         #le pas du temps
G=4*((np.pi)**2)                 #constant
M=1                              #constant
t=np.arange(0,3,h)               #maille de temps
npas=t.shape[0]                  #nombre de pas
hd2=h/2                          #constant pour la methode de Heun
ntab=np.arange(0.4,2.2,0.2)      #tableau des valeurs de k
#tableau de couleurs pour chaque courbe
ctab=np.array(['blue','black','green','red','cyan','magenta','yellow','goldenrod','salmon'])

#boucle qui trace les courbes pour chaque valeur de k avec des couleurs differentes
for n,c in zip(ntab,ctab):
    x=np.zeros(npas)   #creation du tableau vide x
    y=np.zeros(npas)   #creation du tableau vide y
    u=np.zeros(npas)   #creation du tableau vide u
    v=np.zeros(npas)   #creation du tableau vide v

    #conditions initiales
    x[0]=0
    y[0]=-1
    u[0]=n*np.sqrt(G*M)
    v[0]=0   
    


    #boucle d integration par la methode Heun
    for k in range(0,npas-1):
        #Euler
        xint=x[k]+h*u[k]    
        uint=u[k]+h*du(G,M,x[k],y[k])
        yint=y[k]+h*v[k]  
        vint=v[k]+h*dv(G,M,x[k],y[k])
        #Heun
        x[k+1]=x[k]+hd2*(u[k]+uint)
        u[k+1]=u[k]+hd2*(du(G,M,x[k],y[k])+du(G,M,xint,yint))
        y[k+1]=y[k]+hd2*(v[k]+vint)
        v[k+1]=v[k]+hd2*(dv(G,M,x[k],y[k])+dv(G,M,xint,yint))
    #calculer l energie totale de chaque courbe    
    Et=0.5*(u**2+v**2)-(G*M/np.sqrt(x**2+y**2))
    print(Et)
    #tracer les courbes dans un graphique
    plt.plot(x,y,color=c,label=n)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.legend(loc='upper left')
plt.show()

