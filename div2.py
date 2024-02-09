print('XX',end='')
for j in range(5):
    print('0123456789',end='')
print('')
resultat = 1
for i in range(50):
    resultat = resultat / 2
    print('{0:2.50F}'.format(resultat))