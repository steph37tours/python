Liste = [2,3,5,78,6,5]
for i in range(len(Liste)-1):
    if Liste[i] > Liste [i+1]:
        print("erreur",Liste[i], 'est supérieur à ',Liste[i+1])