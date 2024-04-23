# https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/simple_example.py
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# fenêtre de l'application.
app = customtkinter.CTk()
app.geometry("250x150")
app.title(__name__)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# premier widget, un label
label_1 = customtkinter.CTkLabel(master=app,text="Voici une fenêtre avec un label", justify=customtkinter.LEFT)
label_1.grid(column=0,row=0,padx=10,pady=20,sticky="wn")
label_2 = customtkinter.CTkLabel(master=app,text="Label 2", justify=customtkinter.RIGHT)
label_2.grid(column=0,row=1,padx=10,pady=20)

def press_btn():
    txt = label_2._text
    print(":()")
    label_2.configure(text=f"{txt}!")

btn_1 = customtkinter.CTkButton(master=app,width=100,height=100,command=press_btn)
btn_1.grid(column=1,row=2,)

app.mainloop()