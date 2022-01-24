# sticky = "x", sendo x : n = norte, e = leste, w = oeste, s = sul
# columnspan = "x", sendo x o numero de colunas que deseja mesclar
# padx = x, sendo x o tamanho do espaço interno que deseja ser adicionado para separar colunas
# command = lambda:[funcA(),funcB(), funcC()], sendo uma forma de colocar mais que uma função no commando do botão

from tkinter import *
from tkinter import ttk
import subprocess
import Printers


class Aplication:

    def __init__(self, master):

        self.defaultfont = "Rockwell", "10"

        # Titulo
        self.title = Label(master)
        self.title["text"] = "CONFIGURADOR DE IMPRESSORA V.1.0"
        self.title["font"] = "Rockwell", "18", "bold"
        self.title["bg"] = "#F8F8FF"
        self.title["pady"] = 10

        # Label Nome
        self.lb_name = Label(master)
        self.lb_name["text"] = "Nome"
        self.lb_name["font"] = "Rockwell Condensed", "15"
        self.lb_name["bg"] = "#F8F8FF"

        # Label Perfil
        self.lb_profile = Label(master)
        self.lb_profile["text"] = "Local"
        self.lb_profile["font"] = "Rockwell Condensed", "15"
        self.lb_profile["bg"] = "#F8F8FF"

        # Label Ip
        self.lb_ip = Label(master)
        self.lb_ip["text"] = "Ip"
        self.lb_ip["font"] = "Rockwell Condensed", "15"
        self.lb_ip["bg"] = "#F8F8FF"

        # Listbox Nome
        self.name = Listbox(master)
        self.name["font"] = "Rockwell", "10"
        self.name["width"] = 15
        self.name["height"] = 1

        # Listbox Perfil
        self.profile = Listbox(master)
        self.profile["font"] = "Rockwell", "10"
        self.profile["width"] = 20
        self.profile["height"] = 1

        # Listbox Ip
        self.ip = Listbox(master)
        self.ip["font"] = "Rockwell", "10"
        self.ip["width"] = 15
        self.ip["height"] = 1

        # Botao Configurar
        self.setting = PhotoImage(file="Images/Setting.png").subsample(35, 35)
        self.bt_setting = Button(master, text="Configurar", image=self.setting, command=self.settingwindow)

        # Botao Recarregar
        self.reload = PhotoImage(file="Images/Reload.png").subsample(35, 35)
        self.bt_reload = Button(master, text="Recarregar", image=self.reload, command=self.printerslist)

        # Treeview de Listar
        self.guide = ttk.Treeview(master, columns=("Impressora", "Tipo"), show="headings", height=10)
        self.guide.column("Impressora", minwidth=0, width=100)
        self.guide.column("Tipo", minwidth=0, width=100)
        self.guide.heading("Impressora", text="IMPRESSORA")
        self.guide.heading("Tipo", text="TIPO")

        # Treeview de Conexão
        self.conexion = ttk.Treeview(master, columns=("Computador", "Conexão"), show="headings", height=10)
        self.conexion.column("Computador", minwidth=0, width=100)
        self.conexion.column("Conexão", minwidth=0, width=100)
        self.conexion.heading("Computador", text="COMPUTADOR")
        self.conexion.heading("Conexão", text="CONEXÃO")

        # Grid
        self.title.grid(column=0, row=0, columnspan=5)

        self.lb_name.grid(column=1, row=1, ipadx="20")
        self.lb_profile.grid(column=2, row=1, ipadx="20")
        self.lb_ip.grid(column=3, row=1, ipadx="20")

        self.name.grid(column=1, row=2)
        self.profile.grid(column=2, row=2)
        self.ip.grid(column=3, row=2)

        self.bt_setting.grid(column=0, row=5)
        self.bt_reload.grid(column=2, row=4)

        self.guide.grid(column=0, row=4, columnspan=2, sticky="e")
        self.conexion.grid(column=3, row=4, columnspan=2, sticky="w")

        self.nameprofilecomputer()
        self.computerip()
        self.printerslist()
        self.computerconexion()

    @staticmethod
    def commandspowershell(item):
        command = subprocess.getoutput(
            ["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./Commands\";", item])
        return command

    def printerslist(self):
        for item in self.guide.get_children():
            if len(self.guide.get_children()) != 0:
                self.guide.delete(item)
        printerstable = {}
        printerinformation = ["Name", "DriverName", "PortName", "PrintProcessor"]
        for information in printerinformation:
            table = self.commandspowershell(information)
            table = Printers.Printers.variabletreatment(table)
            printerstable = Printers.Printers.createprinters(table, printerstable, information)
        key = 0
        for key in range(key, len(printerstable)):
            if printerstable[key].portname[0:3] == #portname:
                if printerstable[key].printprocessor == "winprint":
                    printprocessor = "Rede"
                else:
                    printprocessor = "Local"
                self.guide.insert("", "end", values=(printerstable[key].name, printprocessor))

    def nameprofilecomputer(self):
        name = self.commandspowershell("hostname")
        self.name.insert("end", name)

        if name[0] == "z":
            profile = "Zona Eleitoral"
        elif name[0] == "r":
            profile = "Secretaria"
        elif name[0] == "c":
            profile = "Central de Atendimento"
        self.profile.insert("end", profile)

    def computerip(self):
        ip = self.commandspowershell("((ipconfig | findstr [0-9].\.)[0]).Split()[-1]")
        self.ip.insert("end", ip)

    def settingwindow(self):
        settingwindow = Toplevel()
        settingwindow.title("Configuração")
        settingwindow.geometry("500x400")
        settingwindow.focus_force()
        settingwindow.grab_set()

        self.title = Label(settingwindow)
        self.title["text"] = "CONFIGURAÇÃO"
        self.title["font"] = "Segoe UI", "18"
        self.title["pady"] = 10

        settingwindow.grid_columnconfigure(0, minsize=100)
        settingwindow.grid_columnconfigure(1, minsize=100)
        settingwindow.grid_columnconfigure(2, minsize=100)
        settingwindow.grid_columnconfigure(3, minsize=100)
        settingwindow.grid_columnconfigure(4, minsize=100)

        self.title.grid(column=0, row=0, columnspan=5)

    def computerconexion(self):
        ip = "10.2.154.38"
        conexion = self.commandspowershell("Test-Connection -Computername {} -quiet".format(ip))
        self.conexion.insert("", "end", values=(ip, conexion))
