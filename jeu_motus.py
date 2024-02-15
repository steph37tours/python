print('Jeu Motus !')
solution="CHEVAL"
for i in range(8):
    proposition = input('Entrez un mot de 6 lettres').upper()
    if proposition == solution :
        print ("GAGNE")
        exit()
    if len(proposition) > 6 :
        print('-------------------')
    else:
        for i in range(6):
            pos = solution.find(proposition[i])
            if pos < 0 :
                print (proposition[i].lower(),' ',end='')
            if pos >= 0 :
                if pos == i :
                    print(proposition[i]+'#', end='')
                else :
                    print(proposition[i]+'?',end='')