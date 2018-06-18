'''ceci est un programme qui trace l orbite elliptique avec Heun'''

#importation des mondules
import numpy as np
import matplotlib.pyplot as plt

#definir deux fonctions de du et de dv
def du(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*x)/(n1**(1.5))

def dv(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*y)/(n1**(1.5))


h=1/365                #le pas du temps
G=4*((np.pi)**2)       #constant
M=1                    #constant
t=np.arange(0,5,h)     #maille de temps
npas=t.shape[0]        #nombre de pas
hd2=h/2                #constant pour la methode de Heun

x=np.zeros(npas)       #creation du tableau vide x
y=np.zeros(npas)       #creation du tableau vide y
u=np.zeros(npas)       #creation du tableau vide u
v=np.zeros(npas)       #creation du tableau vide v

#conditions initiales
x[0]=0
y[0]=-1
u[0]=0.8*np.sqrt(G*M)
v[0]=0   



#boucle d integration par la methode Heun
for k in range(0,npas-1):
    
    #extrapolation par Euler
    x_ipl=x[k]+h*u[k]    
    u_ipl=u[k]+h*du(G,M,x[k],y[k])
    y_ipl=y[k]+h*v[k]  
    v_ipl=v[k]+h*dv(G,M,x[k],y[k])
    #Heun
    x[k+1]=x[k]+hd2*(u[k]+u_ipl)
    u[k+1]=u[k]+hd2*(du(G,M,x[k],y[k])+du(G,M,x_ipl,y_ipl))
    y[k+1]=y[k]+hd2*(v[k]+v_ipl)
    v[k+1]=v[k]+hd2*(dv(G,M,x[k],y[k])+dv(G,M,x_ipl,y_ipl))
    
#Tracer la courbe
plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()
#calculer la variation relative de l energie
Et=0.5*(u**2+v**2)-(G*M/np.sqrt(x**2+y**2))
var=np.abs((Et-Et[0])/Et[0])
