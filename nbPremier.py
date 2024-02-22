#trouver les nb premiers dans les 100 premiers nombres
for k in range (1,100+1):
    premier = True
    for i in range(2,k-1):
        if (k%i)==0:
            premier = False
    if premier== True :
        print(k , end=' ')
