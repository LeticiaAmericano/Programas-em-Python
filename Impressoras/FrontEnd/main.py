import tkinter

from tkinter import *

app = Tk()


app.title("CONIMP")
app.geometry("500x1000")
app["bg"] = "#F8F8FF" # 141E9D
app.resizable(False, False)

app.grid_columnconfigure(0, minsize=100)
app.grid_columnconfigure(1, minsize=100)
app.grid_columnconfigure(2, minsize=100)
app.grid_columnconfigure(3, minsize=100)
app.grid_columnconfigure(4, minsize=100)

app.grid_rowconfigure(0, minsize=100)
app.grid_rowconfigure(1, minsize=100)
app.grid_rowconfigure(2, minsize=100)
app.grid_rowconfigure(3, minsize=100)
app.grid_rowconfigure(4, minsize=100)
app.grid_rowconfigure(5, minsize=100)
app.grid_rowconfigure(6, minsize=100)
app.grid_rowconfigure(7, minsize=100)
app.grid_rowconfigure(8, minsize=100)
app.grid_rowconfigure(9, minsize=100)

app.mainloop()
