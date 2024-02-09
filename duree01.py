reponse = input("entrez un nombre de minutes")
duree = int(reponse)
nbH = duree // 60
nbMin = duree - 60 * nbH
print("Cela fait " , nbH , " heure et " , nbMin , " minutes.")