class Employe:
    def __init__(self,nom,prenom,salaire) -> None:
        self._nom = nom
        self._prenom = prenom
        self._salaire = salaire
    
    def __exemple(self):
        return "Ca fonctionne ?"

    @property
    def nom(self):
        return f"{self._prenom} {self._nom}"

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, nvx_salaire):
        if type(nvx_salaire) == str:
            nvx_salaire = int(nvx_salaire)
        if nvx_salaire > self._salaire : 
            self._salaire = nvx_salaire
    
    @salaire.deleter
    def salaire(self):
        self._salaire = 0

    

emp1 = Employe("Tremblay","Jonathan",60000)
print(emp1.nom)
print(emp1.salaire)
#print(emp1.__exemple())
#emp1.nom = "Joe Tremblay"
#print(emp1.prenom)

del emp1.salaire
print(emp1.salaire)





#print(emp1._salaire)

#emp1.salaire = 70000
#print(emp1.salaire)

#del emp1.salaire
#print(emp1.salaire)