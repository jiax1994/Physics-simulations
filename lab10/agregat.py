'''ceci est un programme qui simule la formation de l'agrégat'''
#importation des modules
import numpy as np
import matplotlib.pyplot as plt

N=256                 #taille du réseau
M=5000                #nombre de marcheurs
nIterMax=100000       #nombre maxumal d'itération temporelles

x=np.random.random_integers(1,N,M)              #positions initiales des marcheurs en x
y=np.random.random_integers(1,N,M)              #positions initiales des marcheurs en y

statusMobile=np.ones(M,dtype='bool')            #True pour marcheur mobile
grilleFixe=np.zeros([N+2,N+2],dtype='bool')     #True pour marcheur fixe

grilleFixe[:,0]=True              #sites collants à y=0, au bas du réseau

nFixe=0                 #nombre de marcheurs fixes
niter=0                 #nombre d'itération
while nFixe<M and niter<nIterMax:                    #boucle temporelle sur les pas
    m,=statusMobile.nonzero()                          #inidices des marcheurs mobiles
    pasx=2*np.round(np.random.random(np.size(m)))-1        #choix d'un pas de 1 ou de -1 dans la direction de x pour chaque marcheur
    pasy=2*np.round(np.random.random(np.size(m)))-1        #choix d'un pas de 1 ou de -1 dans la direction de y pour chaque marcheur
    nb=np.round(np.random.random(np.size(m)))              #générer aléatoirement un nombre nb de 0 ou 1 pour chaque marcheur
    nb2=1-nb                                               #générer aléatoirement un nombre nb2 de 0 ou 1 qui est différent de nb1 pour chaque marcheur
   
    x[m]=np.clip(x[m]+pasx*nb,1,N)          #déplacement dans la direction x 
    y[m]=np.clip(y[m]+pasy*nb2,1,N)         #ou dans la direction y
    
    #pour les marcheurs venant de se déplacer, on vérifie si un voisin est collant
    voisinFixe=grilleFixe[x[m]-1,y[m]-1]     
    voisinFixe+=grilleFixe[x[m],y[m]-1]
    voisinFixe+=grilleFixe[x[m]+1,y[m]-1]
    voisinFixe+=grilleFixe[x[m]+1,y[m]]
    voisinFixe+=grilleFixe[x[m]+1,y[m]+1]
    voisinFixe+=grilleFixe[x[m],y[m]+1]
    voisinFixe+=grilleFixe[x[m]-1,y[m]+1]
    voisinFixe+=grilleFixe[x[m]-1,y[m]]
    k=m[voisinFixe.nonzero()[0]]             #tableau des indices de tous les marcheurs 
    if k.size>0:                             #qui se fixent à un voisin a cette itération
        nFixe+=k.size                        #nombre de marcherus fixes
        statusMobile[k]=False                #False pour les marcheurs fixes
        grilleFixe[x[k],y[k]]=True           #True pour les marcheurs fixes
    print('interation{}, nombres de marcheurs fixes{}'.format(niter,nFixe))
    niter+=1
    
plt.plot(x,y,'ro',markersize='2',markeredgecolor='r')             #tracer les marcheurs selon x et y
plt.xlabel('position x')
plt.ylabel('position y')
plt.axis('equal')

plt.show()
