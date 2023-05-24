#importation librairie pour gerer l'aleatoire
import random
#variable qui contiendrat toute les lettre du joueur
player_letters = []

#fonction pour choisir le mot
def choix():
    #enregistrement du fichier contenant les mots dans la variable texte
    fichier = open("database.txt", "r")
    texte = fichier.read()
    #fermeture du fichier
    fichier.close()
    #diviser le texte en tout les mots puis enregistrement dans un tableau
    tableau = texte.split("\n")
    #choix du mot
    _mot = tableau[random.randint(0, len(tableau) - 1)]
    return _mot

#fonction vérifiant si les lettres taper par le joueur
#sont dans le mot choisi par l'ordinateur
#puis qui l'affiche dans une variable
def affichage(_mot, _player_letters):
    #mot a afficher
    _mot_afficher = ""
    #boucle de toute les lettres du mot
    for x in range(len(_mot)):
        #initialisation du prochain charactère a ajouter
        #dans le mot a afficher
        c = "-"
        #boucle de toute les lettres choisie par le joueur
        for i in range(len(_player_letters)):
            #si la lettre actuel de la boucle est dans le mot choisie
            #affiche la lettre sinon affiche "-"
            if _player_letters[i] == _mot[x]:
                c = _mot[x]
        _mot_afficher += c
    #retourne le mot a afficher
    return _mot_afficher

#fonction contenant le jeu
def Game(tentative_max=5):
    #choix du mot
    mot = choix()
    #initialisation mot a afficher
    mot_afficher = affichage(_mot=mot, _player_letters=player_letters)
    #conteur de tentatives
    tentative = 0
    print("Devinette : \n=> Essayer de deviner mon mot tirer au hasars \n=> En tappant 1 lettre ou le mot directement...")
    #boucle du jeu
    while mot != mot_afficher:
        #affiche les partie visible du mot
        print(mot_afficher)
        #demande de la lettre
        letter = input("Saisiser votre lettre => ")
        #si lettre = mot alors gagner
        if (letter == mot):
            break
        #verifie si il n'y a qu'un seul charactere
        if (len(letter) == 1):
            #ajoute la lettre a la liste des lettres du joueur
            player_letters.append(letter)
            #verifie si la lettre est dans le mot
            identique = False
            for x in range(len(mot)):
                if (letter == mot[x]):
                    identique = True
            #si elle n'y est pas +1 tentative
            if(identique==False):
                tentative+=1
        #explique qu'il ne faut tapper qu'une seul lettre
        else:
            print("Ne saisiser qu'une seul lettre ! ")
        #met a jour le mot a afficher
        mot_afficher = affichage(_mot=mot, _player_letters=player_letters)
        #perdu si plus de tentatives
        if(tentative>=tentative_max):
            break
    #Fin
    if(tentative<tentative_max):
        print("Bravo mon mot était bien : ", mot)
    else:
        print("Perdu mon mot était : ",mot)
#Lancement de la partie
Game()
