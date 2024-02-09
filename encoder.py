nomDepart = input("Entrez le nom à encoder")
nvNom =""
for i in range(len(nomDepart)):
    valLettre = ord(nomDepart[i])
    if valLettre > 97 :
        nvValLettre = valLettre - 23
    else :
        nvValLettre = valLettre + 3
    nvNom = nvNom + chr(nvValLettre)
print (nvNom)
