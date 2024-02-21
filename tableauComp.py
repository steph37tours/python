Liste1 = [5,4,3,2]
Liste2 = [7,8,9,5]
print(' ' , Liste2)
for i in Liste1:
    print(i, end='')
    for j in Liste2:
        if (j<i) :
            var ='<'
        if (j>i):
            var = '>'
        if (j==i):
            var ='='
        print('{0:3}'.format(var),end='')
    print('')