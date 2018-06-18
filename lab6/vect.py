''' ceci est le programme vectorisé '''

#importation du module
import numpy as np

#définir la fonction qui accepte les paramètres pa ps lambda d et N
def fct(pa,ps,lamda,d,N):
    #initialisation de x et costheta sous forme de tableau de taille N
    x=np.zeros(N)
    costheta=np.ones(N)
    #tableau qui indique si les neutrons sont actifs ou non en nombre binaire, initialement ils sont tous actifs, donc la taille de tableau est N
    actif=np.full(N,True,'int')
    iActif=actif.nonzero()    
    #taille du tableau de résultat
    nb=np.size(iActif)
    #initialisation des positions des neutrons 
    sr,sa,st=0,0,0    
    
    #une boucle qui collecte les résultat lorsque le nombre des neutrons sont actifs, jusqu'à ce dernier devient 0
    while nb!=0:
        #les positions des neutrons actifs sous forme de tableau
        x=x[iActif]
        #les directions des neutrons actifs sous forme de tableau
        costheta=costheta[iActif]
        #générer trois tableaux de nombres aléatoires entre 0 et 1, leur taille est le même que le nombre de neutrons actifs
        r1=np.random.random(nb)
        r2=np.random.random(nb)
        r3=np.random.random(nb)
        #trouver les valeurs de l pour les neutrons actifs
        l=-lamda*np.log(r1)
        #trouver les valeurs de delta x pour les neutrons actifs
        deltax=l*costheta
        #trouver les nouvelles positions de neutrons après le déplacement
        x+=deltax        
        #définir la taille de la plaque, entre x0 et xd, ce sont des constantes sous formes de tableaux
        x0=np.full_like(x,0)
        xd=np.full_like(x,d)
        #probabilité d'absorption sous forme de tableau de même taille que r2
        Pa=np.full_like(r2,pa)
        #probabilité de la dispersion de neutrons, pa+ps, la taille est le même que celle de r2
        PaPs=np.full_like(r2,pa+ps)        
        #valeurs booléennes si les positions dépasse x0
        result1=x>=x0
        #convertir les valeurs en nombre binaire
        res1=np.array(result1,'int')  
        #le nombre des neutrons réfléchis
        sr+=np.size(res1)-np.size(res1.nonzero())
        #valeurs booléennes si les positions sont à inférieur de la plaque
        result2=x<=xd
        #convertir les valeurs en nombre binaire
        res2=np.array(result2,'int')
        #le nombre des neutrons transmis
        st+=np.size(res2)-np.size(res2.nonzero())       
        #valeurs booléennes si les neutrons sont dans la plaque
        resultx=result1*result2
        #les indices des neutrons dans la plaque
        resx=np.nonzero(np.array(resultx,'int'))    
        #valeurs booléennes si r2 est supérieur ou égale à pa
        result3=r2>=Pa
        #valeurs booléennes si r2 est supérieur à pa pour les neutrons dans la plaque
        res3=result3[resx]
        #convertir les résultats en nombre binaire
        res3=np.array(res3,'int')
        #nombre de neutrons absorbés lorsque r2 est inférieur à pa pour les neutrons dans la plaque
        sa+=np.size(res3)-np.size(res3.nonzero())        
        #valeurs booléennes si les neutrons sont dans la plaque et leur r2 correspondant est supérieur ou égale à pa, c'est-à-dire si les neutrons sont actifs.
        resultfinal=resultx*result3
        #valeurs booléennes si r2 sont inférieurs à pa+ps
        result4=r2<PaPs
        #convertir les résultats en nombre binaire
        res4=np.array(result4,'int')
        #pour les r2 supérieurs à pa+ps, r3 devient 0 pour que costheta soit 1 pour la prochaine itération. sinon, r3 restent telles qu'elles.
        r3=res4*r3
        #convertir les résultat des neutrons actifs ou non-actifs en nombre binaire        
        actif=np.array(resultfinal,'int')
        #les indices des neutrons actifs
        iActif=actif.nonzero()
        #le nombre des neutrons actifs
        nb=np.size(iActif)
        #variation de direction pour les neutrons actifs dispersé.Les directions des neutrons non-dispersé ne change pas: costheta=1
        costheta=1-2*r3
    
    #calcul de réflectance, d'absorbance, de transmittance et des erreurs
    R,A,T=sr/N,sa/N,st/N
    sigR=(R*(1-R)/(N-1))**(1/2)
    sigA=(A*(1-A)/(N-1))**(1/2)
    sigT=(T*(1-T)/(N-1))**(1/2)
    T=st/N
    e=1/T
    return R,A,T,sr,sa,st,sr+sa+st,sigR,sigA,sigT,e
    
    
        
        
        
    
