nbkm = int(input ("Quel est le nombre de km parcouru ?"))
if nbkm < 100 :
    montant = nbkm *.60
else :
    montant = 100 * .60 + (nbkm-100)*0.50
print("Le prix est ", montant)

