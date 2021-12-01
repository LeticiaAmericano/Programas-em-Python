#static: metodo da classe
class Conta:

    def __init__(self, numero, titular, saldo, limite): # self é a referencia que sabe encontrar o endereço
        print("Construindo objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __podeSacar(self, valor):
        valorDisponivel = self.__saldo + self.__limite
        return valor <= valorDisponivel

    def saca(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigoBanco():
        return {"BB" : "001", "Caixa" : "104", "Bradesco" : "257"}

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

conta01 = Conta(121, "Leticia", 50.0, 100.0)
conta02 = Conta(122, "Marcos", 55.0, 200.0)

conta01.extrato()
conta02.extrato()

conta01.deposita(10)
conta02.saca(15)

conta01.extrato()
conta02.extrato()

conta01.transfere(10.0, conta02)

conta01.extrato()
conta02.extrato()

cliente = Cliente("leticia")
print(cliente.nome)

conta01.saca(1200)
