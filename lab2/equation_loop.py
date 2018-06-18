''' ceci est un programme qui résoud de façcon itérative une équation exponentielle '''

#importation du module de numpy
import numpy

#importation de l'équation exponentielle dans le module numpy
from numpy import exp

#définir la variable a
a=input('entrer une valeur de a: ')

#convertir la réponse entrée de a en nombre
b=eval(a)

#définir la variable x, et l'assigne à b pour la valeur initiale de x
x=b

#définir une variable qui permet de calculer le nombre d'itération dans la boucle
i=0

#création de la boucle, la condition est que l'erreur est supérieur au seuil 
while x-b*(1-exp(-x))>10**(-8):
    
    #chaque itération, la valeur de i ajout 1
    i+=1
	
    #chaque itération, x diminue de façon exponentielle
    x=b*(1-exp(-x))

    #Lorque l'erreur est inférieure au seuil, le calcul s'arrête et afficher les résultats
    print ('Itération',i,'  erreur:',x-b*(1-exp(-x)),'  valeur de x:',x)
