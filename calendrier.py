nbJour = int(input("Entrez le nombre de jour dans le mois ?"))
premJour = int(input("Entrez le premier jour du mois ?"))
colco = 0
print('{0:4}{1:4}{2:4}{3:4}{4:4}{5:4}{6:4}'.format('LUN','MAR','MER','JEU','VEN','SAM','DIM'))
nbVide = premJour -1
print('    '*nbVide,end='')
colco = nbVide
for i in range(1,nbJour+1):
    print ('{:3} '.format(i),end="")
    colco = colco + 1
    if colco == 7: 
        print("")
        colco = 0
