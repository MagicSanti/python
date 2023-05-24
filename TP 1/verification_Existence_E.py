word1=input("Taper Votre Mot :\n=> ")
bool_E = False
for letter in word1:
    if letter == "e":
        bool_E = True
if(bool_E):
    print('Il y a 1 ou plusieurs "e" !')
else:
    print('Il n\'y a pas de "e" !')
