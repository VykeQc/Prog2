exemple = ["1-f00","2-barr","12-exemple"]


exemple.sort()
print(exemple)

newliste = []
for nom in exemple :
    num, nom = nom.split("-")
    num = num.zfill(2)
    newliste.append(f"{num}-{nom}")