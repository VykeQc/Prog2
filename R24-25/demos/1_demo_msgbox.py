# https://docs.python.org/3/library/tkinter.messagebox.html
# https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/


import tkinter
from tkinter import messagebox

""" 
rep = messagebox.askquestion(title="En-tête", message="Texte ici !")

rep = messagebox.showinfo("1","infos")
messagebox.showwarning("2","avertissement")
messagebox.showerror("3","erreur")

messagebox.askquestion("4","question")

messagebox.askokcancel("5","cancel?")
messagebox.askyesno("6","oui / non ?")
messagebox.askretrycancel("7", "ré-essayer ?")

messagebox.askyesnocancel("8","true/false/None")
 """

messagebox.Message(title="9",message="ret",type='yesno',icon='warning').show() 

try:
    rep = "allo"
    rep / 2
except Exception as ex :
    messagebox.showerror("ERREUR",f"{type(ex)} \n {ex}")
