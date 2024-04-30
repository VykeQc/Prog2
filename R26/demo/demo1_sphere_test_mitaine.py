from math import pi

class Sphere:
    def __init__(self, pRayon) -> None:
        self._rayon = 0
        self.rayon = pRayon 
    
    @property
    def rayon(self) : return self._rayon
    @property
    def circonference(self): return 2 * pi * self._rayon 
    @property
    def volume(self): return 4 / 3 * pi * (self._rayon ** 3) 
    @property
    def aire(self): return 4 * pi * (self._rayon ** 2)
    
    @rayon.setter
    def rayon(self, pRayon):
        if type(pRayon) != int and type(pRayon) != float: raise TypeError("Le rayon doit être de type <int>. type fourni :",type(pRayon)) 
        if pRayon <= 0 : raise ValueError("Le rayon doit avoir une valeur positive. Valeur fourni:",pRayon)
        self._rayon = pRayon

if __name__ == "__main__" :
    print(pi) #voyez que vous pouvez utilisé la constante pi
    try : s1 = Sphere(-10)
    except ValueError: print("Impossible de faire une sphere avec un rayon de -10")

    try : s2 = Sphere("cinq")
    except TypeError: print("Impossible de faire une sphere avec un rayon de 'cinq'")

    s3 = Sphere(20)

    try : s3.rayon = -10
    except ValueError: print("Impossible de changer un rayon pour -10")

    try : s3.rayon = "cinq"
    except TypeError: print("Impossible de changer un rayon pour 'cinq'")
    
    print("\nValeurs de s3 : ")
    print("rayon:",s3.rayon," circ:",s3.circonference," vol:",s3.volume," aire:",s3.aire)

    s3.rayon = 10
    print("\nOn change le rayon pour 10 : ")
    print("rayon:",s3.rayon," circ:",s3.circonference," vol:",s3.volume," aire:",s3.aire,"\n")


    #Testez votre code, voir l'énoncé

