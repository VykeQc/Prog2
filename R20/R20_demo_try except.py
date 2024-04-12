class Employe:
    def __init__(self, pSalaire) -> None:
        self._salaire = pSalaire

    @property
    def salaire(self):
        return
    
    @salaire.setter
    def salaire(self, nvx_salaire) :
        try :
            if nvx_salaire > self._salaire :
                self._salaire = nvx_salaire
                print("Imprimer uniquement si pas d'erreur")
            
        except TypeError :
            print("!!!Entrer un montant en chiffre")
        

        finally :
            print("Ce block est toujours exécuté.")


emp = Employe(500)
print(emp.salaire)
emp.salaire = "waopeirj"
emp.salaire = 2
print(emp.salaire)
emp.salaire = 984654
print(emp.salaire)