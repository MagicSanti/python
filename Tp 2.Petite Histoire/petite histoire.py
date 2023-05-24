#Écrire un programme qui affiche le nombre de grains
# à déposer sur chacune des 64 cases du jeu d'echec

#creation du tableau representant les graine sur l'echiquier
gt=[]
#boucle de toute les cases
i=0
while i<64:
    #verifie si il y a deja des grains sur l'echiquier
    #si oui le double pour la prochaine case
    if i!=0:
        gt.append(gt[i-1]*2)
    #sinon en met 1 sur la premiere case
    else:
        gt.append(1)
    #affichage
    print(i+1," : ",gt[i])
    #réitaration de la boucle
    i+=1