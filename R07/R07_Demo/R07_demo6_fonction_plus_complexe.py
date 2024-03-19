#list copy
cours_S3 = ["Comm. milieux professionnels", "Intro cybersécurité"]
cours_S3_P = ["Prog. 3", "Prog. Web Transactionnelle"]
cours_S3_R = ["Automatisation de tâches","commutatation et routage","Serveurs 2 : Services Intranet"]
cours_S3_general = ["Philosophie et rationalité", "Litt. québecoise"]


cours_amy = cours_S3 + cours_S3_R + cours_S3_general
cours_charlie = cours_S3 + cours_S3_P + cours_S3_general
cours_maxime = cours_S3 + cours_S3_P


def impression_cours(liste_de_cours:list = None,  personne:str =""):
    if liste_de_cours is None: 
          print("Vous devez entrez une liste de cours")
          return
    print(f"Cours de {personne}:")
    for cours in liste_de_cours:
            print(f"    {cours}")
    print()

def nombre_de_cours(liste_de_cours:list):
      nbr = len(liste_de_cours)
      return nbr


impression_cours(personne="Amy")
#impression_cours(cours_charlie,"Charlie")
#impression_cours(cours_maxime,"Maxime")

nombre_cours = nombre_de_cours(cours_amy)

print(nombre_cours)


def impression_liste(en_tete, liste) :
      print(en_tete)
      for valeur in liste :
            print(f"    {valeur}")
      print()
      return None











# def impression_liste(texte,liste) :
#     print(texte)
#     for valeur in liste :
#         print(f"    {valeur}")
#     print()
    
# impression_liste("Cours d'Amy : ", amy_liste_cours)
# impression_liste("Cours de Charle : ", charle_liste_cours)
# impression_liste("Cours de Maxime : ", maxime_liste_cours)

