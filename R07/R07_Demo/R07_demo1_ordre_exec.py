def formatage_de_nom(nom,prenom):
    nom = nom.strip()
    nom = nom.capitalize()
    prenom = prenom.strip().capitalize()
    return f"{prenom} {nom}"

print("Bonjour utilisateur : ", end=" ")
print(formatage_de_nom("BOB", "  tremblay "))
print("Votre compte est a jour.")



