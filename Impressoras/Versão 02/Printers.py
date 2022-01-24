class Printers:

    # Construtores
    def __init__(self, drivername, name, portname, printprocessor):
        self.__name = name
        self.__drivername = drivername
        self.__portname = portname
        self.__printprocessor = printprocessor

    def __init__(self, name):
        self.__name = name
        self.__drivername = 0
        self.__portname = 0
        self.__printprocessor = 0

    # Tratamento feito quando se recebe a resposta do comando prompt
    @staticmethod
    def variableTreatment(table):
        table = table.split("\n")
        table = [table.strip() for table in table if table.strip() != ""]
        return table

    @staticmethod
    # Criação das Impressoras
    def createPrinters(table, printersTable, information):
        element = 0
        factor = 0
        if information == "Name":
            for element in table:
                printersTable[factor] = Printers(element)
                factor = factor + 1
        if information == "DriverName":
            factor = printersTable[factor].inputPrinters(element, factor, information, table, printersTable)
        if information == "PortName":
            factor = printersTable[factor].inputPrinters(element, factor, information, table, printersTable)
        if information == "PrintProcessor":
            factor = printersTable[factor].inputPrinters(element, factor, information, table, printersTable)
        return printersTable

    # Informação das Impressoras
    def inputPrinters(self, element, factor, information, table, printersTable):
        if information == "DriverName":
            for element in table:
                printersTable[factor].drivername = element
                factor = factor + 1
        if information == "PortName":
            for element in table:
                printersTable[factor].portname = element
                factor = factor + 1
        if information == "PrintProcessor":
            for element in table:
                printersTable[factor].printprocessor = element
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