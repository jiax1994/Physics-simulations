'''ceci est un programme de simulation d'intéraction radiation-matière'''
#importation des modules de numpy et de graphique
import numpy as np
import matplotlib.pyplot as plt

#définir la fonction qui accepte les paramètres pa ps lambda d et N
def fct(pa,ps,lamda,d,N):
    #initialisation des positions des neutrons
    sr,sa,st=0,0,0
    #création d'une boucle pour chaque neutrons
    for k in range(N):
        #initialisation de la position et de la direction du neutron
        x,costheta=0.,1.
        #création d'une boucle qui compte et catégorisent les neutrons en sr sa et st selon les résultats
        while True:
            #générer trois nombres aléatoires entre 0 et 1
            r1=np.random.random()
            r2=np.random.random()
            r3=np.random.random()
            #calculer la valeur de l
            l=-lamda*np.log(r1)
            #calculer la variation de déplacement en x
            deltax=l*costheta
            #calculer la nouvelle position du neutron
            x+=deltax
            #si la nouvelle position est négatif, le neutron est réfléchi
            if x<0:
                sr+=1
                #on commence une nouvelle itération pour le prochain neutron
                break
            #si la nouvelle position est supérieure à d, le neutron est transmis
            elif x>d:
                st+=1
                #on commence une nouvelle itération pour le prochain neutron
                break
            #la nouvelle position est dans la plaque
            else:
                #si le neutron est absorbé dans la plaque
                if r2<pa:
                    sa+=1
                    #on commence une nouvelle itération pour le prochain neutron
                    break
                #si le neutron est dispersé dans la plaque, on calcule un nouveau costheta pour la prochaine itération, sinon costheta ne change pas dans le cas r2>pa+ps
                elif pa<=r2 and r2<pa+ps:
                    costheta=1-2*r3
    
    #calcul de réflectance, d'absorbance, de transmittance et des erreurs                    
    R,A,T=sr/N,sa/N,st/N
    sigR=(R*(1-R)/(N-1))**(1/2)
    sigA=(A*(1-A)/(N-1))**(1/2)
    sigT=(T*(1-T)/(N-1))**(1/2)
    e=1/T
    return R,A,T,sr,sa,st,sr+sa+st,sigR,sigA,sigT,e

#tracer la graphique de l'étape 1
pa=0.2
#ps varie de 0 à 1-pa avec un pas de 0.1
pstab=np.arange(0,1-pa,0.1)
lamda=0.2
d=1
N=10000
#créer les listes vides de réflectance, d'absorbance, de transmittance et des leurs incertitudes
R,A,T=[],[],[]
sigR,sigA,sigT=[],[],[]
#créer une boucle pour pstab
for ps in pstab:
    #trouver les valeurs que le fonction retourne
    f=fct(pa,ps,lamda,d,N)
    #print(f)
    #ajouter ces valeurs à leur liste correspondantes
    R.append(f[0])
    A.append(f[1])
    T.append(f[2])
    sigR.append(f[7])
    sigA.append(f[8])
    sigT.append(f[9])

#tracer une graphique de R en fonction de ps
plt.plot(pstab,R,'b',label='R')
#tracer les erreurs
x,y=pstab,R
plt.errorbar(x,y,xerr=0,yerr=sigR)
#tracer une graphique de A en fonction de ps
plt.plot(pstab,A,'g',label='A')
#tracer les erreurs
x,y=pstab,A
plt.errorbar(x,y,xerr=0,yerr=sigA)
#tracer une graphique de T en fonction de ps
plt.plot(pstab,T,'r',label='T')
#tracer les erreurs
x,y=pstab,T
plt.errorbar(x,y,xerr=0,yerr=sigT)
#afficher le graphique
plt.legend(loc='upper right')
plt.xlabel('ps')
plt.ylabel('coefficients')
plt.show()
