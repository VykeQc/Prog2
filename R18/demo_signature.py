class Employe:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return 
class Programmeur(Employe):
    def __init__(self, nom, prenom, langage) -> None:
        super().__init__(nom, prenom)
        self.langage_favori = langage
    def __str__(self):
        return 
class Vendeur(Employe):
    def __init__(self, nom, prenom, taux) -> None:
        super().__init__(nom, prenom)
        self.taux_commission = taux
    def __str__(self):
        return 
print()
print()
print()

emp = Employe("Gallant","Pierre")
print(emp)
emp_prog = Programmeur("Tremblay","Ana","Python")
print(emp_prog)
emp_vendeur = Vendeur("Borne","Margaut",2)
print(emp_vendeur)

print()
print()
print()