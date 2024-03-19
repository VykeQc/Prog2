#list copy

cours_info_S2 = [['Programmation 2', 'Math', 'Réseaux locaux', 'Services Intranet'],['Philosophie', 'Francais', 'Anglais']]
amy_liste_cours = cours_info_S2.copy()
print("\n\n")

print("liste de cours")
for valeur in cours_info_S2:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("")

print("liste de cours d'Amy")
for valeur in amy_liste_cours:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("")

#On ajoute le cours d'éducation physique "volley-ball" à Amy
print("\n\n")
amy_liste_cours[1].append("Volley-ball")

print("liste de cours d'Amy avec volley-ball")
for valeur in amy_liste_cours:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("")


print("liste de cours original" )
for valeur in cours_info_S2:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("")
    
# liste de cours de Steve
print("\n\n")
steve_liste_cours = cours_info_S2.copy()
print("liste de cours de Steve")
for valeur in steve_liste_cours:
    print(f"ID: {id(valeur)}  Cours: {valeur}")
print("")
