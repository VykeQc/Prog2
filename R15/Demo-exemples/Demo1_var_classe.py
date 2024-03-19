class Employe:
    id_1 = 1
    id_2 = 1
    id_3 = 1
    
    def __init__(self,nom,prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.id_1 = 2
        self.id_2 = 2

    def retourne_id(self):
        id_1 = 3
        print(id_1)

exemple = Employe("a","b")

exemple.retourne_id()
print(exemple.id_2)
print(exemple.id_3)