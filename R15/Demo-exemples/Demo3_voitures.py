class Voiture:
    def __init__(self,marque) -> None:
        self.marque = marque
    
    def klaxon(self):
        print("honk!")

print("\n")

class Voiture_moteur(Voiture):
    def __init__(self, marque,reservoir):
        super().__init__(marque)
        self.reservoir = reservoir

class Pickup(Voiture_moteur):
    def __init__(self, marque, reservoir,puissance):
        super().__init__(marque, reservoir)
        self.puissance = puissance
    
    def klaxon(self):
        print("HOOONKKK!")

remorque = Pickup("Ford","60L","1200hp")
remorque.klaxon()

print("\n\n")


class Voiture_de_luxe(Voiture_moteur):
    def __init__(self, marque, reservoir,prix):
        super().__init__(marque, reservoir)
        self.prix = prix

fancy_car = Voiture_de_luxe("Mercedes","60L","120000")
fancy_car.klaxon()




print("\n\n")