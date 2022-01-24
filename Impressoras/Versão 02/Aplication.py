from tkinter import *
import subprocess
import Printers

printersTable = {}

class Aplication:
    def __init__(self, master = None):

        self.standardFont = ("Segoe UI", "10")

        #Container do titulo
        self.fullScreem = Frame(master)
        self.fullScreem["padx"] = 30
        self.fullScreem.pack()

        #Container do Botão
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 15
        self.firstContainer.pack()

        #Container do ListBox
        self.secondContainer = Frame(master)
        self.secondContainer["pady"] = 10
        self.secondContainer.pack()

        #Titulo
        self.title = Label(self.fullScreem, text = "CONFIGURADOR DE IMPRESSORA V.1.0")
        self.title["font"] = ("Segoe UI", "15")
        self.title.pack()

        #Botão
        self.toList = Button(self.firstContainer, text = "Listar", font = self.standardFont, command = self.PrintersList)
        self.toList["width"] = 12
        self.toList.pack()

        #ListBox
        self.toListBox = Listbox(self.secondContainer)
        self.toListBox.font = self.standardFont
        self.toListBox["width"] = 35
        self.toListBox.pack()

    def PrintersList(self):
        printerInformation = ["Name", "DriverName", "PortName", "PrintProcessor"]
        for information in printerInformation:
            table = subprocess.getoutput(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./Commands\";", information])
            table = Printers.Printers.variableTreatment(table)
            Printers.Printers.createPrinters(table, printersTable, information)
        key = 0
        for key in range(key, len(printersTable)):
            if printersTable[key].portname[0:3] == #portname:
                self.toListBox.insert("", "end", values=(printersTable[key].name, printProcessor))