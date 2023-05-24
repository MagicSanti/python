#Declaration des tableaux
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin ','Juillet', 'Août ', 'Septembre ', 'Octobre', 'Novembre', 'Décembre ']
t3=[]
#boucle pour chaque mois du tableaux
for i in range(len(t2)):
    #ajoute les mois dans le tableau
    t3.append(t2[i])
    #ajoute le nombre de jours de chaque mois dans le tableau
    t3.append(t1[i])
#affiche le tableau
print(t3)