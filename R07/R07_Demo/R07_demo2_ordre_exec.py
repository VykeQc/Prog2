import inspect

def lineno():
    return inspect.currentframe().f_back.f_lineno

def formatage_de_nom(nom:str,prenom:str):
    nom = nom.strip()       ; print(f"Ligne {lineno()} : Retire les espaces sueprflues")
    nom = nom.capitalize()  ; print(f"Ligne {lineno()} : Capitalise le nom")
    prenom = prenom.strip().capitalize() ; print(f"Ligne {lineno()} : fait les mêmes opérations pour le prénom")
    return f"{prenom} {nom}"; print(f"Ligne {lineno()} : Retourne le nom complet dans le bon format")




if __name__ == "__main__":
    print(f"Ligne {lineno()} : La fonctione 'lineno()' retourne le numéro de la ligne de code actuel.")

    formatage_de_nom("  bob","temblay  ")
    nom = formatage_de_nom(" lisa    ", "DUPONT")
    
    print(f"Nom bien formaté : {nom}")
    
