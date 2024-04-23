# https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/simple_example.py

import customtkinter

customtkinter.set_appearance_mode("light")  # Style de la fenêtre"
customtkinter.set_default_color_theme("blue")  # couleurs des éléments

app = customtkinter.CTk()
# Paramètres de l'app telle que la taille de la fenêtre.

# Tous les widgets qui formeront notre interface graphique.

def press_btn():
    text_label = l1._text
    l1.configure(text=f"{text_label}!")
    print(c1.get())

l1 = customtkinter.CTkLabel(master=app,text="Mon Label!",width=150,anchor="w")
l1.grid(column=0,row=0)
b1 = customtkinter.CTkButton(master=app,text="Press ME !",command=press_btn)
b1.grid(column=1,row=1)
c1 = customtkinter.CTkEntry(app)
c1.grid(column=1,row=0)

app.mainloop() # Lance notre application. 