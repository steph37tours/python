compteur = 0
for i in range(10,100):
    dizaine = i//10
    unite = i - dizaine * 10
    if ( dizaine == 7) or (unite == 7) :
        compteur = compteur + 1
print(compteur)