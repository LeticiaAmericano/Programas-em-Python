def criaConta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta = criaConta(123, "leticia", 55.0, 1000.0)
deposita(conta, 15.0)
extrato(conta)
saca(conta, 20.0)
extrato(conta)
deposita(conta, 200.0)
extrato(conta)

#numero = 123
#titular = "leticia"
#saldo = 55.0
#limite = 1000.0

#conta02 = {"numero": 123, "titular": "leticia", "saldo": 55.0, "limite": 1000.0}
