Liste1 = [4,5,9]
Liste2 = [1,6,10]
Liste3 = []
i = 0
j = 0
while True:
    if ( i>= 3 & j >= 3) :
        break
    if(Liste1[i]<=Liste2[j]):
        Liste3.append(Liste1[i])
        i+=1
    else :
        Liste3.append(Liste2[j])
        j+=1
print(Liste3)