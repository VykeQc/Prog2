from tkinter import filedialog
import json

print((filedialog.askopenfilename()))

with filedialog.askopenfile() as f_lu :
    text = f_lu.read()
    data = json.loads(text)

print(data)

with filedialog.asksaveasfile() as f_ec:
    print(f_ec)
    f_ec.write("eproi")