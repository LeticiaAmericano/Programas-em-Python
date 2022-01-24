import tkinter

from Aplication import Aplication
from tkinter import *

app = Tk()

app.tk.call('wm', 'iconphoto', app._w, tkinter.PhotoImage(file="Images/TRE-MG.png"))

app.title("CONIMP")

app.grid_columnconfigure(0, minsize=100)
app.grid_columnconfigure(1, minsize=150)
app.grid_columnconfigure(2, minsize=150)
app.grid_columnconfigure(3, minsize=150)
app.grid_columnconfigure(4, minsize=100)

app.grid_rowconfigure(0, minsize=100)
app.grid_rowconfigure(1, minsize=50)
app.grid_rowconfigure(2, minsize=10)
app.grid_rowconfigure(3, minsize=25)
app.grid_rowconfigure(4, minsize=300)
app.grid_rowconfigure(5, minsize=50)

app["bg"] = "#F8F8FF" #141E9D
app.resizable(False, False)


Aplication(app)

app.mainloop()