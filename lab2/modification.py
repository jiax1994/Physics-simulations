'''ceci est la modification du programme de la question 1'''

#définir le rayon de n
n=range(1,100)

#créer la boucle
while n!=0:
    #entrer la variable
    rep=input('SVP entrez une valeur entre 1 et 100 (ou 0 pour quitter):')
    #assigner n à rep et convertir ce dernier en entier
    n=int(rep)
    #recommencer l'itération si la valeur n'est pas dans le rayon de n
    if n!=0 and n<1 or n>100 :
        print('Valeur hors de l’intervalle! Recommencez.')
        continue
    
    #afficher la valeur de n sauf n=0
    if n!=0: print(n,end=' ')
    
    #calcul de n si sa valeur est dans le rayon et n'est pas égale à 0 et à 1    
    while n!=1 and n!=0:
        n=n//2 if n%2==0 else 3*n+1
        print(n,end=' ')
    print()
 
#sortir du programme si n est 0 
print('Sortie du programme...')
