x = len(vars())
while True:
    v = int(input())
    if v < x :
        print('plus grand')
    else :
        if v> x :
            print('plus petit')
        else :
            print('gagné')