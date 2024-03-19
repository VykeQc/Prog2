cours_S3 = ["Comm. milieux professionnels", "Intro cybersécurité"]
cours_S3_P = ["Prog. 3", "Prog. Web Transactionnelle"]
cours_S3_R = ["Automatisation de tâches","commutatation et routage","Serveurs 2 : Services Intranet"]
cours_S3_general = ["Philosophie et rationalité", "Litt. québecoise"]

amy_liste_cours = cours_S3 + cours_S3_R + cours_S3_general
charle_liste_cours = cours_S3 + cours_S3_P + cours_S3_general
maxime_liste_cours = cours_S3 + cours_S3_P

# Fonction sans paramètres
LISTE_EMPLOYE = ["Ana Smith", "Jonathan Strange"]

def impression_employe() :
    print("Employé du département :")
    for valeur in LISTE_EMPLOYE :
        print(f"    {valeur}")
    print()


a = impression_employe
print()
a()

print( int(5.9) )

# #Fonction avec paramètres par défault
# def impression_liste(texte = "Liste : ", liste = ["Vide"]) :
#     print(texte)
#     for valeur in liste :
#         print(f"    {valeur}")
#     print()

# impression_liste()
# impression_liste("Cours d'Amy : ")
# impression_liste(liste=amy_liste_cours)
# impression_liste("Cours d'Amy : ",liste=amy_liste_cours)