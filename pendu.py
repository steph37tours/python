print('Jeu du pendu !')
solution="CHEVAL"
for i in range(6):
    lettre = input('Entrez une lettre').upper()
    pos = solution.find(lettre)
    if pos ==-1 :
        print("#"*6)
    else :
       av = pos
       ap = 5 - pos
       print('#'* av,lettre,'#'*ap)
mot = input('Proposez un mot')
if mot == solution :
     print ("GAGNE")
else:
    print ("PERDU")
