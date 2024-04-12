
class Employe:
    def __init__(self,nom,prenom,salaire):
        self.nom = nom
        self.prenom = prenom
        self._salaire = salaire
    def nom_complet(self):
        return self.prenom + " " + self.nom
    @property
    def salaire(self):
        return self._salaire
    @salaire.setter
  
    def salaire(self,nvx_salaire:int):
        try:
            nvx_salaire = int(nvx_salaire)
            if nvx_salaire < self._salaire:
                raise ValueError(f"le nouveau salaire {nvx_salaire} doit être plus grand que l'ancien {self.salaire}")
            self._salaire = nvx_salaire

            print("LIGNE DE CODE IMPORTANT")
        except :
            print("erreur type mais on continu")
            self.salaire = input("nouvelle valeur")


    
chimiste = Employe("Belatekallim","Tapputi",45000)
try :
    chimiste.salaire = 2200000000
except :
    print("Salaire trop petit")
print("erreur type mais on continu")
print(chimiste.salaire)
