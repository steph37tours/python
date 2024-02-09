import random
nbTirage = int(input("Entrez le nombre de tirage ?"))
nbPile = 0
nbFace = 0
for i in range(nbTirage):
    PileFace = random.randint(0,1)
    if PileFace == 0 :
        nbPile +=1
    else :
        nbFace +=1
print('{0:2d} -- {1:2d}'.format(nbPile*100//nbTirage, nbFace*100//nbTirage))