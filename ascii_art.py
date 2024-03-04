import matplotlib.image as img

image = img.imread("/home/stephane/python_space/portrait.jpg")
max = image.max()
hauteur = len(image)
largeur = len(image[0])
pas=10
ascii = ["@","#","O","o","n","=","+",":","."," "]
for y in range(0,hauteur,pas):
    for x in range (0,largeur,pas):
        val = image[y][x]
        val = sum(val)/len(val)
        lum = int(10*val/max)
        print(ascii[lum]+ascii[lum],end="")
    print("")