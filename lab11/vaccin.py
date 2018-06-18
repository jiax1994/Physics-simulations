'''ceci est un programme qui simule la pandémie avec la vaccination'''

import numpy as np
import matplotlib.pyplot as plt
import random


p=0.5
M=5000
L=25
nvacctab=np.arange(0,M-1,100)        #tableau de nombre de marcheurs à vacciner 
coutmoytab=np.zeros(nvacctab.size)   #tableau vide des coûts moyens       
sigcoutmoy=np.zeros(nvacctab.size)
m=0
for nvacc in nvacctab:    #boucle sur la vaccination des marcheurs
    N=np.sqrt(M/p)
    nIterMax=5000
    fois=0
    couttab=[]
    while fois<3:         #boucle sur le nombre des essais
        np.random.seed()
        x=np.random.random_integers(1,N,M)
        y=np.random.random_integers(1,N,M)
        infect=np.zeros(M,dtype='int')
        duree=np.zeros(M,dtype='int')
        immunite=np.zeros(M,dtype='int')   #tableaux des personnes immunisées 

        jj=np.random.random_integers(0,M-1)
        while True:                      #boucle qui génère le nombre de marcheurs à vacciner
            r=random.sample(range(M-1),nvacc)    #l'indice DIFFÉRENTES des nombres de marcheurs à vacciner
            o,=(jj==r).nonzero()     #on ne veut pas que l'indice d'infecté soit dans celles des marcheurs vaccinés
            if o.size==0:
                vj=r
                break
        infect[jj]=1
        duree[jj]=L
        immunite[vj]=1
        ninfect=1 
        nimmunite=nvacc   #nombre de macheurs vaccinés 

        
        niter=0
        
        while ninfect>0 and niter<nIterMax:
            #tout les marcheus déplacent
            pasx=2*np.round(np.random.random(M))-1        #choix d'un pas de 1 ou de -1 dans la direction de x pour chaque marcheur
            nb=np.round(np.random.random(M))              #générer aléatoirement un nombre nb de 0 ou 1 pour chaque marcheur
            nb2=1-nb                                               #générer aléatoirement un nombre nb2 de 0 ou 1 qui est différent de nb1 pour chaque marcheur
           
            x=np.clip(x+pasx*nb,1,N)          #déplacement dans la direction x 
            y=np.clip(y+pasx*nb2,1,N)  
            
            
            for j in (infect==1).nonzero()[0]:
                k,=((x==x[j])&(y==y[j])&(infect==0)&(immunite==0)).nonzero() #il faut ajouter la condition que le marcheur est non immunisé
                
                if k.size>0:
                    p=np.random.random(k.size)
                    imalade,=(p<0.5).nonzero()      #tenir compte de la propabilité d'être infecté
                    f=k[imalade]
                    infect[f]=1
                    duree[f]=L
                    ninfect+=f.size
                duree[j]-=1
                if duree[j]==0:
                    infect[j]=0
                    immunite[j]=1    #devenir immunisé
                    nimmunite+=1
                    ninfect-=1
            print("iter{}: {} malades, {} immune".format(niter,ninfect,nimmunite))
        
            niter+=1
        
        cout=50*nvacc+100*(nimmunite-nvacc)     #le coût total
        couttab.append(cout)
        
        fois+=1
    Couttab=np.asarray(couttab)     #mettre des valeurs dans les tableaux
    coutmoy=np.mean(Couttab)
    sigcout=Couttab.std(ddof=1)
    coutmoytab[m]=coutmoy
    sigcoutmoy[m]=sigcout
    m+=1

pourcentage=(nvacctab/5000)*100       #tracer la courbe coût vs pourcentage de vaccination
Pourcentage=np.asarray(pourcentage)
plt.plot(Pourcentage,coutmoytab,'b')
yerr=sigcoutmoy
plt.errorbar(Pourcentage,coutmoytab,yerr,ecolor='r')
plt.xlabel('pourcentage %')
plt.ylabel('coût total moyen')
plt.show()
