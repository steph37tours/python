import math
a = int(input('entrez a'))
b = int(input('entrez b'))
c = int(input('entrez c'))
Delta = b**2 - 4 *a *c
if Delta > 0 :
    sol1 = (- b + math.sqrt(Delta)) / 2 * a
    sol2 = (-b - math.sqrt(Delta) )/ 2 * a
    print ('Les solutions sont ', sol1, ' et ', sol2)
else :
    if Delta == 0 :
        sol1 = -b /2 * a
        print ('la solution est ', sol1)
    else :
        print ('Pas de solution')
