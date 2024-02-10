liste = [1,2,3,8,10,13,56,7]
pair=[]
impair=[]
for i in liste:
    if i%2 == 0:
        pair.append(i)
    else :
        impair.append(i)
print('Voici la liste des pairs ',pair)
print('Voici la liste des impairs ',impair)