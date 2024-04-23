from tkinter import messagebox



# Lorsqu'on utilise tkinter, on passe à une interface graphique.
# Rend l'utilisation d'inputs par le CLI compliquer


messagebox.showinfo("Nom", "Entrez votre nom dans l'invite de commande")



from tkinter import simpledialog

repstr = simpledialog.askstring("Nom ?","Entrez votre nom : ")

repint = simpledialog.askinteger("chiffre","Entrez un integer")

repfloat = simpledialog.askfloat("Float","Entrez un float")

messagebox.showinfo("Nom", f"Votre nom est : {repstr}")

try :
    r2 = repstr < 5
except Exception as ex :
    messagebox.showerror("Erreur",f"{type(ex)}\n{ex}")





