from tkinter import *#Importação da biblioteca de interface grafica

class Application: #Criação da classe aplicação
    def __init__(self, master=None): #Definição de função
        self.widget1 = Frame(master)  #Criação do primeiro container widget1 e passar por referencia o conteiner pai
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack () #Informar o gerenciador da geometria pack
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack ()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"



root = Tk() #Instanciar classe: copia de um objeto existente  // Classe permite que os widgets possam ser utilizados na aplicação
Application(root) #Passagem das variavel root como parametro do metodo construtor da classe
root.mainloop() #Exibição em tela

#Width = Largura do widget
#Height = Altura do widget
#Text = Texto a ser exibido no widget
#Font = Familia da fonte do texto
#Fg = Cor do texto do widget
#Bg = Cor de fundo do widget
#Side = top

#Evento Loop: Ações executadas como resposta a determinado evento // Interpreta ações como strings
#Botão esquerdo do mouse = " "
#Botão enter = ""
#Botão direito do mouse = ""