cheminFic = '/home/stephane/Bureau/test.txt'
f = open(cheminFic,'r')
ligne = f.readline()

while(len(ligne))>0 :
    print(ligne,end='')
    ligne = f.readline()

f.close()