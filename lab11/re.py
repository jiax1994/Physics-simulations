'''ceci est un programme qui simule la propagation de maladie'''

import numpy as np
import matplotlib.pyplot as plt

#une fonction qui montre le déplacement des marcheurs à une itération donnée
def fct(x,y,infect):
    q,=(infect==0).nonzero()
    w,=(infect==1).nonzero()
    e,=(infect==2).nonzero()
    plt.plot(x[q],y[q],'bo')
    plt.plot(x[w],y[w],'ro')
    plt.plot(x[e],y[e],'ko')
    plt.show()




N=128   #taille du réseau
M=5000  #nombre de marcheurs
L=20    #durée de survie
nIterMax=5000   #itération maximum
np.random.seed()    #germe

x=np.random.random_integers(1,N,M)   #positions initiales
y=np.random.random_integers(1,N,M)
infect=np.zeros(M,dtype='int')       #tableaux des infectés et la durée de survie
survie=np.zeros(M,dtype='int')

jj=np.random.random_integers(0,M-1)   #un marcheur est infecté
infect[jj]=1
survie[jj]=L
ninfect=1 
nmort=0

a,b,c=[],[],[]
niter=0
while ninfect>0 and niter<nIterMax:      #itération temporelle
    v,=(infect<2).nonzero()        #indice des marcheurs vivants
    pasx=2*np.round(np.random.random(np.size(v)))-1        #choix d'un pas de 1 ou de -1 dans la direction de x pour chaque marcheur
    nb=np.round(np.random.random(np.size(v)))              #générer aléatoirement un nombre nb de 0 ou 1 pour chaque marcheur
    nb2=1-nb                                               #générer aléatoirement un nombre nb2 de 0 ou 1 qui est différent de nb1 pour chaque marcheur
   
    x[v]=np.clip(x[v]+pasx*nb,1,N)          #déplacement dans la direction x et y
    y[v]=np.clip(y[v]+pasx*nb2,1,N)  
    
    
    for j in (infect==1).nonzero()[0]:       #boucle sur les marcheurs infectées
        k,=((x==x[j])&(y==y[j])&(infect==0)).nonzero()   #même positions et sains?
        
        if k.size>0:                #il devient contagion
            infect[k]=1
            survie[k]=L
            ninfect+=k.size
        survie[j]-=1
        if survie[j]==0:            #il est mort après L=20
            infect[j]=2
            nmort+=1
            ninfect-=1
    print("iter{}: {} malades, {} morts.".format(niter,ninfect,nmort))
    if niter==250:                #montrer le graph des marcheurs 
        f=fct(x,y,infect)
    a.append(niter)
    b.append(ninfect)
    c.append(nmort)
    niter+=1
    
A=np.asarray(a)         #mettre les résultats en tableaux
B=np.asarray(b)
C=np.asarray(c)

plt.plot(A,5000-C,'b')                 #tracer les courbes
plt.yticks(color='b')
plt.xlim(0,np.max(A))
plt.ylabel('vivant',color='b')
plt.xlabel('itération')
plt.twinx()
plt.plot(A,B,'r')
plt.yticks(color='r')
plt.ylabel('malades',color='r')
plt.xlim(0,np.max(A))
plt.show()
