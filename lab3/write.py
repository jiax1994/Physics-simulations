'''ceci est un programme qui écrit les positions de la projectile en fonction du temps dans un fichier
'''
#importation de module numpy
import numpy as np

#ouverture de fichier
fichier=open('position.txt',mode='w')

#définir les constantes
v=15
theta=60
g=9.8

#définir les formules 
Tf=2*v*np.sin(np.deg2rad(theta))/g
t=np.arange(0,Tf,0.01)
x=v*t*np.cos(np.deg2rad(theta))
y=v*t*np.sin(np.deg2rad(theta))-g*t**2/2

#boucle pour créer un tableau des résultats des calculs
for i in range(len(t)):

    #formater les résultats
    T='{:10.2f} '.format(t[i])
    X='{:10.4f} '.format(x[i])
    Y='{:10.4f} '.format(y[i])
    
    #écrire l'entête dans le fichier
    fichier.write('    Temps:     X:         Y:      vitesse initiale=15m/s, angle=60degré')
    
    #écrire une nouvelle ligne
    fichier.write('\n')
    
    #écrire les résultats de T,X et Y
    fichier.write(T)
    fichier.write(',')
    fichier.write(X)
    fichier.write(',')
    fichier.write(Y)
	
	#finir la ligne
    fichier.write('\n')

#fermeture de fichier    
fichier.close()
