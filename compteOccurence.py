Liste = [0,2,2,5,6,9,9,2]
for i in range(10):
    totalOccurence = Liste.count(i)
    if totalOccurence > 0 :
        print ("Nombre occurence " + str(i) + "  " + str(totalOccurence))