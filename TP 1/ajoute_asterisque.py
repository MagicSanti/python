
word1 = input("Taper Votre Mot :\n=> ")
word2 = ""
letters=[]
for letter in word1:
    letters.append(letter)
for i in range(len(letters)-1):
    word2 += letters[i]+"*"
word2 += letters[len(letters)-1]
print(word2)

