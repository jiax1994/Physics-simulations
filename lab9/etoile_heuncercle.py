'''ceci est un programme qui trace l orbite circulaire avec Heun'''

#importation des mondules
import numpy as np
import matplotlib.pyplot as plt

#definir deux fonctions de du dv du2 et dv2
def du(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*x)/(n1**(1.5))

def dv(G,M,x,y):
    n1=(x**2)+(y**2)
    n2=G*M
    return (-n2*y)/(n1**(1.5))

def du2(G,M,M1,x,x2,y,y2):
    nb1=x2**2+y2**2
    nb2=(x2-x)**2
    nb3=(y2-y)**2
    nb4=G*M*x2
    nb5=G*M1*(x2-x)
    return (-nb4/(nb1**(1.5)))-(nb5/((nb2+nb3)**(1.5)))

def dv2(G,M,M1,x,x2,y,y2):
    nb1=x2**2+y2**2
    nb2=(x2-x)**2
    nb3=(y2-y)**2
    nb4=G*M*y2
    nb5=G*M1*(y2-y)
    return (-nb4/(nb1**(1.5)))-(nb5/((nb2+nb3)**(1.5)))


h=1/3650               #le pas du temps
G=4*((np.pi)**2)      #constant
M=1                     #constant
M1=0.02*M                   #constant
t=np.arange(0,50,h)    #maille de temps
npas=t.shape[0]       #nombre de pas
hd2=h/2               #constant pour la methode de Heun
R1,R2=1,1.6           #valeurs initiale des R


x=np.zeros(npas)      #creation du tableau vide x 
y=np.zeros(npas)      #creation du tableau vide y 
u=np.zeros(npas)      #creation du tableau vide u 
v=np.zeros(npas)      #creation du tableau vide v 
x2=np.zeros(npas)     #creation du tableau vide x2
y2=np.zeros(npas)     #creation du tableau vide y2
u2=np.zeros(npas)     #creation du tableau vide u2
v2=np.zeros(npas)     #creation du tableau vide v2

#conditions initiales
x[0]=0
y[0]=-R1
u[0]=0.9*np.pi*2*np.sqrt(M/R1)
v[0]=0   
x2[0]=0
y2[0]=-R2
u2[0]=2*np.pi*np.sqrt(M/R2)
v2[0]=0



#boucle d integration par la methode Heun
for k in range(0,npas-1):
    
    #Euler
    x_ipl=x[k]+h*u[k]    
    u_ipl=u[k]+h*du(G,M,x[k],y[k])
    y_ipl=y[k]+h*v[k]  
    v_ipl=v[k]+h*dv(G,M,x[k],y[k])
    x2_ipl=x2[k]+h*u2[k]
    u2_ipl=u2[k]+h*du2(G,M,M1,x[k],x2[k],y[k],y2[k])
    y2_ipl=y2[k]+h*v2[k]
    v2_ipl=v2[k]+h*dv2(G,M,M1,x[k],x2[k],y[k],y2[k])
    #Heun
    x[k+1]=x[k]+hd2*(u[k]+u_ipl)
    u[k+1]=u[k]+hd2*(du(G,M,x[k],y[k])+du(G,M,x_ipl,y_ipl))
    y[k+1]=y[k]+hd2*(v[k]+v_ipl)
    v[k+1]=v[k]+hd2*(dv(G,M,x[k],y[k])+dv(G,M,x_ipl,y_ipl))
    x2[k+1]=x2[k]+hd2*(u2[k]+u2_ipl)
    u2[k+1]=u2[k]+hd2*(du2(G,M,M1,x[k],x2[k],y[k],y2[k])+du2(G,M,M1,x_ipl,x2_ipl,y_ipl,y2_ipl))
    y2[k+1]=y2[k]+hd2*(v2[k]+v2_ipl)
    v2[k+1]=v2[k]+hd2*(dv2(G,M,M1,x[k],x2[k],y[k],y2[k])+dv2(G,M,M1,x_ipl,x2_ipl,y_ipl,y2_ipl))

#calculer la variation relative de rayon de la petite planete
Rt=np.sqrt(x2**2+y2**2)
varr=np.abs((Rt-Rt[0])/Rt[0])
r12=np.sqrt((x2-x)**2+(y2-y)**2)
#calculer la variation relative de l energie totale de la petite planete
Et=0.5*(u2**2+v2**2)-(G*M/np.sqrt(x2**2+y2**2))-(G*M1/r12)
vare=np.abs((Et-Et[0])/Et[0])

    
#tracer la courbe de l orbite
plt.plot(x2,y2,'r')
plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()

#tracer la courbe de l energie 
plt.plot(t,Et,'g')
plt.xlabel('t')
plt.ylabel('energie')
plt.axis('equal')
plt.show()
