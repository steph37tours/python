mot= input("Entrez un mot")
compteur = 0
nb_lettres = len(mot)
print (nb_lettres)
motMaj = mot.upper()
print(motMaj)
for i in range(len(mot)):
    print(motMaj[i])
    if (motMaj[i]== "A") or (motMaj[i] == "O") or (motMaj[i]== "I") or (motMaj[i]== "E") or( motMaj[i]== "U") :
        compteur = compteur +1
        print ("voyelle")

total = len(mot)-compteur

print("Dans ce mot, le nombre de consonnes est : ", total)