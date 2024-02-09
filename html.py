html = "<html><head><title>Titre de la page</title></head></html>"
inde_depart = 0
for i in range(len(html)):
    if html[i]=="<":
        indice_depart=i
        indice_fin = html.find(">",indice_depart)
        balise = html[indice_depart+1:indice_fin]
        print (balise)