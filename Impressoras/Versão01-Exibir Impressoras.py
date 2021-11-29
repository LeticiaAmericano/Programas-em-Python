from tkinter import *
import subprocess as sp

class Aplication:
    def __init__(self, master = None):

        self.printersTable = []

        self.standardFont = ("Segoe UI", "12")

        self.fullScreem = Frame(master)
        self.fullScreem["padx"] = 100
        self.fullScreem.pack()

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 15
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 20
        self.secondContainer.pack()

        self.title = Label(self.fullScreem, text = "Impressoras", font = self.standardFont)
        self.title.pack()

        self.toList = Button(self.firstContainer, text = "Listar", font = self.standardFont, command = self.Printers)
        self.toList["width"] = 12
        self.toList.pack()

        self.toListBox = Listbox(self.secondContainer)
        self.toListBox.font = self.standardFont
        self.toListBox["width"] = 30
        self.toListBox.pack()

    def Printers(self):
        table = sp.getoutput('wmic printer get name')
        self.printersTable = table.split("\n")
        self.printersTable = [self.printersTable.strip() for self.printersTable in self.printersTable if self.printersTable.strip() != ""]
        element = 1
        listSize = len(self.printersTable)
        for element in range(element, listSize):
            self.toListBox.insert(END, self.printersTable[element])

root = Tk()
Aplication(root)
root.mainloop()
