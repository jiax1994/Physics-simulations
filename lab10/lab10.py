'''ceci est un programme qui simule la marche aléatoire en 2D'''
#importation des modules
import numpy as np
import matplotlib.pyplot as plt
nM=1000       #nombre de marcheurs
nPas=1001     #nombre de pas
x=np.zeros([nM,nPas])      #position x de chaque marcheur à chaque pas, initialement à 0
y=np.zeros([nM,nPas])      #position y de chaque marcheur à chaque pas, initialement à 0

for k in range(1,nPas):    #boucle sur les pas

    
    pasx=(2*np.round(np.random.random(nM))-1)     #choix d'un pas de 1 ou de -1 dans la direction de x
    pasy=(2*np.round(np.random.random(nM))-1)     #choix d'un pas de 1 ou de -1 dans la direction de x
    nb=np.round(np.random.random(nM))             #générer aléatoirement un nombre nb de 0 ou 1
    nb2=1-nb                                      #générer aléatoirement un nombre nb2 de 0 ou 1 qui est différent de nb1
    x[:,k]=x[:,k-1]+pasx*nb                       #déplacement dans la direction x
    y[:,k]=y[:,k-1]+pasy*nb2                      #ou dans la direction y

dQuad=x**2+y**2                                   #déplacement quadratique
dQuadmoy=dQuad.mean(axis=0)                       #déplacement moyen quadratique
xmoy=(x).mean(axis=0)                             #déplacement moyen en x

plt.plot(x[:,1000],y[:,1000],'bo')                #tracer les points à pas=1000
plt.plot(x[:,300],y[:,300],'go')                  #tracer les points à pas=300
plt.plot(x[:,100],y[:,100],'ro')                  #tracer les points à pas=100
plt.plot(x[:,30],y[:,30],'yo')                    #tracer les points à pas=30
plt.plot(x[:,10],y[:,10],'ko')                    #tracer les points à pas=10
plt.xlabel('position x')
plt.ylabel('position y')
plt.axis('equal')
plt.show() 

plt.plot(dQuadmoy)                                #tracer la courbe du déplacement moyen quadratique
plt.plot(np.arange(nPas))                         #tracer la courbe de variation de n
plt.xlabel('itération')
plt.ylabel('déplacement moyen quadratique')
plt.show()

plt.plot(xmoy)                                    #tracer la courbe du déplacement moyen dans la direction x
plt.xlabel('itération')
plt.ylabel('déplacement moyen en x')
plt.show()
