import json
cheminFic = '/home/stephane/Bureau/test.txt'
f = open(cheminFic,'w')
L = [1,2,"toto"]
json.dump(L,f)
f.close()

f = open(cheminFic,'r')
ligne = json.load(f)
print (ligne)




f.close()