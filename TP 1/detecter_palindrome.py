word1 = input("Taper Votre Mot :\n=> ")
word2 = ""
letters=[]
for letter in word1:
    letters.append(letter)
for i in range(len(letters),0,-1):
    word2 += letters[i-1]
if word1==word2:
    print("Ce Mot Est Un Palindrome ! ")
else:
    print("Ce Mot N'est pas un palindrome ! ")