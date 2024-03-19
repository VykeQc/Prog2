import csv
#Nous avons une liste d'étudiants. 
liste_etudiants = [ ["Anna",543564,"420-INFO"],
                    ["Greg",987123,"420-INFO"],
                    ["Bob",369852,"238-FRAN"],
                    ["Joseph",753869,"135-PHYS"],
                    ["Hubert",125478,"238-FRAN"],
                    ["Zeus",659327,"135-PHYS"],
                    ["Joel",583649,"420-INFO"] ]


with open("etudiants_ids.csv", "w") as fichier_csv :
    csv_writer = csv.writer(fichier_csv,delimiter="\t")
    csv_writer.writerow(["ID","nom"])
    for etudiant in liste_etudiants:
        csv_writer.writerow([etudiant[1],etudiant[0]])
print()


with open("etudiants_ids.csv", "r") as fichier_csv :
    csv_reader = csv.reader(fichier_csv,delimiter="\t")
    for line in csv_reader:
        print(line)