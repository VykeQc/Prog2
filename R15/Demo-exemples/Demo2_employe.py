import random

class Employe:
    liste_employe = []
    next_ID = 1000
    
    def __init__(self,nom,prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.ID = Employe.next_ID
        
        Employe.next_ID += 1
        Employe.liste_employe.append(self)
print("\n")


# employe1 = Employe("Anna","Tremblay")
# employe2 = Employe("Bartholemy","Duchamp")


# for emp in Employe.liste_employe: 
#     print(f'{emp.prenom} {emp.nom} {emp.ID}')

# for emp in employe1.liste_employe: 
#     print(f'{emp.prenom} {emp.nom} {emp.ID}')


# print(employe1.__dict__)



print("\n")



class Programmeur(Employe):
    def __init__(self, nom, prenom,language_favori) -> None:
        super().__init__(nom, prenom)
        self.language_favori = language_favori


prog1 = Programmeur("Desjardins","Carole","Python")
employe1 = Employe("Anna","Tremblay")
employe2 = Employe("Bartholemy","Duchamp")


for emp in Employe.liste_employe: 
    print(f'{emp.prenom} {emp.nom} {emp.ID}')
    
    
    
    
print("\n")