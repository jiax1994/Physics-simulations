'''ceci est un programme qui fait les 10 essais'''

import numpy as np
import matplotlib.pyplot as plt

ctab=np.array(['blue','black','green','red','cyan','yellow','salmon','magenta']) #tableau de couleurs
ptab=np.arange(0.15,0.55,0.05)
M=5000
L=20
um=0
umoytab=np.zeros(ptab.size)   #tableaux vides initaux des résultats
sigutab=np.zeros(ptab.size)
tmoytab=np.zeros(ptab.size)
sigttab=np.zeros(ptab.size)
for p,c in zip(ptab,ctab):    #boucle sur les densités
    N=np.sqrt(M/p)
    nIterMax=5000  
    utab,ttab=[],[]
      
    fois=0
    while fois<10:            #boucle sur les essais
        np.random.seed()

        x=np.random.random_integers(1,N,M)
        y=np.random.random_integers(1,N,M)
        infect=np.zeros(M,dtype='int')
        survie=np.zeros(M,dtype='int')

        jj=np.random.random_integers(0,M-1)
        infect[jj]=1
        survie[jj]=L
        ninfect=1 
        nmort=0
        niter=0
        while ninfect>0 and niter<nIterMax:
            v,=(infect<2).nonzero()
            pasx=2*np.round(np.random.random(np.size(v)))-1        #choix d'un pas de 1 ou de -1 dans la direction de x pour chaque marcheur
            nb=np.round(np.random.random(np.size(v)))              #générer aléatoirement un nombre nb de 0 ou 1 pour chaque marcheur
            nb2=1-nb                                               #générer aléatoirement un nombre nb2 de 0 ou 1 qui est différent de nb1 pour chaque marcheur
           
            x[v]=np.clip(x[v]+pasx*nb,1,N)          #déplacement dans la direction x 
            y[v]=np.clip(y[v]+pasx*nb2,1,N)  
          
            for j in (infect==1).nonzero()[0]:
                k,=((x==x[j])&(y==y[j])&(infect==0)).nonzero()
                
                if k.size>0:
                    infect[k]=1
                    survie[k]=L
                    ninfect+=k.size
                survie[j]-=1
                if survie[j]==0:
                    infect[j]=2
                    nmort+=1
                    ninfect-=1
            print("iter{}: {} malades, {} morts.".format(niter,ninfect,nmort))
            
            iteration=niter
            niter+=1
        
        
        
        u=nmort/5000
        utab.append(u)
        ttab.append(iteration)
        
        fois+=1 

    Utab=np.asarray(utab)           #mettre les résultats en tableaux
    Ttab=np.asarray(ttab)
    umoy=np.mean(Utab)
    tmoy=np.mean(Ttab)
    sigu=Utab.std(ddof=1)
    sigt=Ttab.std(ddof=1)
    umoytab[um]=umoy
    tmoytab[um]=tmoy
    sigutab[um]=sigu
    sigttab[um]=sigt
    um+=1


    plt.plot(Ttab,Utab,color=c,linestyle=' ',marker='o',label=p)      #tracer taux de mortalité vs durée
    plt.legend(loc='upper left')
plt.xlabel('durée')
plt.ylabel('taux de mortalité')
plt.show()        
plt.plot(ptab,umoytab)                          #tracer densité vs taux de mortalité
yerr=sigutab
plt.errorbar(ptab,umoytab,yerr,ecolor='r')
plt.xlabel('densité')
plt.ylabel('taux moyen de mortalité')           
plt.show()   
plt.plot(ptab,tmoytab)                          #tracer densité vs durée
yerr=sigttab
plt.errorbar(ptab,tmoytab,yerr,ecolor='r')
plt.xlabel('densité')
plt.ylabel('durée moyenne')
plt.show()
