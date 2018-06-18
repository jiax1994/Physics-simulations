''' ceci est un programme qui lit le fichier de résultat des positions de la projectile
'''
#importation de module numpy et la librairie matplotlib
import numpy as np
import matplotlib.pyplot as plt

#ouverture de fichier de position
fichier=open('position.txt',mode='r')

#lecture de fichier ligne par ligne
lignes=fichier.read().split('\n')

#créer 3 listes vides et définir i initiale
x=[]
y=[]
t=[]
i=1

#un boucle qui ajoute les valeurs de positions et de temps dans les listes vides
while i<len(lignes):
    
    #convertir chaque lignes sous forme d'une liste
    v=lignes[i].split(',')
   
    #ajouter les trois éléments de la liste v dans les trois listes vides désirées
    t.append(v[0])
    x.append(v[1])
    y.append(v[2])
    
    #sauter les lignes de l'entête
    i+=2
#fermeture de fichier
fichier.close()

#convertir les 3 listes sous forme de tableau
t=np.asarray(t)
x=np.asarray(x)
y=np.asarray(y)

#aficher les 3 tableaux
print(t)
print(x)
print(y)

#tracer la courbe de y en fonction de x
plt.plot(x,y,'b',marker='D', markevery=10)

#mettre les axes en même échelles
plt.axis('scaled')

#donner les noms aux échelles et montrer la courbe
plt.xlabel('x')
plt.ylabel('y')
plt.show()


