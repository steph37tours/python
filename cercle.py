import math
n = 16
l = 2/n
K=0
for x in range(n):
    for y in range (n):
        Cx = x*l
        Cy = y*l
        d = math.sqrt((Cx - 1)**2 + (Cy-1)**2)
        if d < 1:
             K+=1
Pi = K * 4/n**2
print (Pi)