class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    #lista
    def deposita(self, valor):
        self.saldo += valor

    #tupla
    def deposita(self, conta):
        novosaldo = conta[1]+100
        codigo = conta[0]
        return codigo, novosaldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

    @staticmethod
    def depositaparatodas(contas):
        for conta in contas:
            conta.deposita(100)

conta_da_leticia = ContaCorrente(15)
print(conta_da_leticia)

conta_da_leticia.deposita(500)
print(conta_da_leticia)

conta_do_marcos = ContaCorrente(101)
conta_do_marcos.deposita(100)
print(conta_do_marcos)

contas = [conta_da_leticia, conta_do_marcos]
print(contas)

for conta in contas:
    print(conta)

print(contas[0])
conta_da_leticia.deposita(100)
print(contas[0])

ContaCorrente.depositaparatodas(contas)
for conta in contas:
    print(conta)

contas.insert(71)
for conta in contas:
    print(conta)

leticia = ("Letícia", 20, 2001) #tupla
marcos = ("Marcos", 21, 2001)