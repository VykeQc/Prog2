from abc import ABC, abstractmethod


class Employe(ABC):
    liste_employe = []
    next_ID = 1000
    def __init__(self,nom,prenom):
        pass
    
    @abstractmethod
    def test_abs(self):
        pass
    

class Programmeur(Employe):
    def __init__(self, nom, prenom,language_favori) :
        pass

    def test_abs(self):
        print("vla")


employe1 = Programmeur("Anna","Tremblay","python")
employe1.test_abs()
print( isinstance(employe1, Employe) )













#employe1.test_abs()

#employe2 = Employe("Bartholemy","Duchamp")
#prog1 = Programmeur("Desjardins","Carole","Python")
#prog1.test_abs()

# for emp in Employe.liste_employe: 
#     print(f'{emp.prenom} {emp.nom} {emp.ID}')
#     emp.test_abs()


#print("\n")