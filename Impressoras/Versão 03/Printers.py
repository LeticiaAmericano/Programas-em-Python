class Printers:

    # Construtores
    def __init__(self, name):
        self.__name = name
        self.__drivername = 0
        self.__portname = 0
        self.__printprocessor = 0

    # Tratamento feito quando se recebe a resposta do comando prompt
    @staticmethod
    def variabletreatment(table):
        table = table.split("\n")
        table = [table.strip() for table in table if table.strip() != ""]
        return table

    # Criação das Impressoras
    @staticmethod
    def createprinters(table, printerstable, information):
        factor = 0
        if information == "Name":
            for element in table:
                printerstable[factor] = Printers(element)
                factor = factor + 1
        if information == "DriverName":
            printerstable[factor].inputprinters(factor, information, table, printerstable)
        if information == "PortName":
            printerstable[factor].inputprinters(factor, information, table, printerstable)
        if information == "PrintProcessor":
            printerstable[factor].inputprinters(factor, information, table, printerstable)
        return printerstable

    # Informação das Impressoras
    @staticmethod
    def inputprinters(factor, information, table, printerstable):
        if information == "DriverName":
            for element in table:
                printerstable[factor].drivername = element
                factor = factor + 1
        if information == "PortName":
            for element in table:
                printerstable[factor].portname = element
                factor = factor + 1
        if information == "PrintProcessor":
            for element in table:
                printerstable[factor].printprocessor = element
                factor = factor + 1
        return factor

    # Retorna o valor da variavel privada
    @property
    def name(self):
        return self.__name

    @property
    def portname(self):
        return self.__portname

    @property
    def printprocessor(self):
        return self.__printprocessor

    @property
    def drivername(self):
        return self.__drivername

    # Atribui um valor

    @drivername.setter
    def drivername(self, drivername):
        self.__drivername = drivername

    @portname.setter
    def portname(self, portname):
        self.__portname = portname

    @printprocessor.setter
    def printprocessor(self, printprocessor):
        self.__printprocessor = printprocessor

    # Imprimir todos os atributos
    def __str__(self):
        return self.__drivername + self.__name + self.__portname + self.__printprocessor