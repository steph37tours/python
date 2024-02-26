Liste1 = [4,5,9]
Liste2 = [1,6,10,15]
Liste3 = []
ll1 = len(Liste1)
ll2 = len(Liste2)
i = 0
j = 0
while True:
    if ( i>= ll1) :
        Liste3.append(Liste2[j:])
        break
    if (j >= ll2):
        Liste3.append(Liste1[i:])
        break
    if(Liste1[i]<=Liste2[j]):
        Liste3.append(Liste1[i])
        i+=1
    else :
        Liste3.append(Liste2[j])
        j+=1
print(Liste3)