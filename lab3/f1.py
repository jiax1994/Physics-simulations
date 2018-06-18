'''ceci est un programme qui calcule et affiche les positions de y en fonction de x selon les différents angles
'''

#importation de module numpy et la librairie matplotlib
import numpy as np
import matplotlib.pyplot as plt

#définir la fonction de la trajectoire de projectile
def trajectoire(v0,theta,pas):

    #définir la constante g et le temps final Tf
    g=9.8
    Tf=2*v0*np.sin(np.deg2rad(theta))/g
    
    #définir la différence de temps entre chaque position
    dt=Tf/pas
    
    #définir les formules et les variables
    t=np.arange(0,Tf,dt)
    x=v0*t*np.cos(np.deg2rad(theta))
    y=v0*t*np.sin(np.deg2rad(theta))-g*t**2/2
    
    #retourner les valeurs 
    return x,y

#liste des différents angles
thetatab=[30,35,40,45,50,55,60,65,70,75,80,85]

#une boucle pour calculer et tracer la trajectoire selon chaque angle
for theta in thetatab:
    f=trajectoire(15,theta,500)
    #convertir f en tableau
    f=np.asarray(f)
    print(f)
    #tracer la courbe pour chque itération
    plt.plot(f[0],f[1] ,'b')
    
#nommer les axes et tracer les courbes
plt.xlabel('x')
plt.ylabel('y')

plt.show()
