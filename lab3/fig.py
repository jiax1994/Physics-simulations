'''ceci est un programme qui calcule et affiche les positions de y en fonction de x selon les différents angles, il y a deux graphiques
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
    return x,y,t,Tf

#définir une fonction croissante
def monotone_croissant(d):
    
#définir le rayon de i
    for i in range(len(d)-1):
#définir une condition vraie 
        true=d[i]<d[i+1]
#si la condition est vraie, sauter le reste de l'itération 
        if true: 
            continue
#sinon, afficher la valeur de d[i+1] et arrêter l'itération
        else:
            print('la courbe est décroissant à ',d[i+1],'pour un angle de ',theta)
            break
#retourne le résultat
        return true

#liste des différents angles
thetatab=[30,35,40,45,50,55,60,65,70,75,80]

#création de deux graphiques dans un figure
plt.figure(1,figsize=(8.,4.),dpi=100)

#tracer les courbes pour chaques itérations
for theta in thetatab:
    #calculer f et convertir f en tableau
    f=trajectoire(15,theta,500)
    f=np.asarray(f)
    
    #tracer la première graphique 
    plt.subplot(1,2,1)
    plt.plot(f[0],f[1] ,'b')
    plt.xlabel('x')
    plt.ylabel('y')
    
    #définir la distance d
    d=((f[0]**2)+(f[1]**2))**0.5
    
    #tester si d est croissant
    r=monotone_croissant(d)
    
    #normaliser le temps
    t=f[2]/f[3]
   
    #tracer la deuxième graphique
    plt.subplot(1,2,2)
    plt.plot (t,d,'g',label=theta)
    plt.xlabel('t/Tf')
    plt.ylabel('d')
    
plt.show()


    

