from collections import defaultdict
from collections import Counter

usuarioDataScience = [15, 23, 43, 56]
print(usuarioDataScience)
usuarioMachineLearning = [13, 23, 56, 42]
print(usuarioMachineLearning)

assistiram = usuarioDataScience.copy()
print(assistiram)
assistiram.extend(usuarioMachineLearning)
print(assistiram)

assistiram = set(assistiram)
print(assistiram)
print(type(assistiram))

usuarioDataScience = set(usuarioDataScience)
usuarioMachineLearning = set(usuarioMachineLearning)

usuarioOu = usuarioDataScience | usuarioMachineLearning # uniao
print(usuarioOu)

usuarioE = usuarioDataScience & usuarioMachineLearning # interseção
print(usuarioE)

usuarioNao = usuarioDataScience - usuarioMachineLearning # diferença
print(usuarioNao)

usuarioOuExclusivo = usuarioDataScience ^ usuarioMachineLearning # Ou Exclusivo
print(usuarioOuExclusivo)

usuario = {1, 5, 76, 34, 52, 13, 17}
print(usuario)
print(len(usuario))

usuario.add(13)
print(len(usuario))
usuario.add(765)
print(len(usuario))
print(usuario)

usuario = frozenset(usuario)
print(type(usuario))

texto = "Bem vindo meu nome é Letícia eu gosto de cachorro e meu cachorro tem o nome de Theo"
print(texto)

texto = texto.split()
print(texto)

texto = set(texto)
print(texto)

aparicoes = {"Letícia" : 1, "cachorro" : 2, "nome" : 2, "vindo": 1}
print(aparicoes)
print(type(aparicoes))
print(aparicoes.get("Letícia", 0))
print(aparicoes.get("xpto", 0))

aparicoesDiferentes = dict(Letícia = 1, cachorro = 2, nome = 2, vindo = 1)
print(aparicoesDiferentes)
aparicoesDiferentes["Marcos"] = 1
print(aparicoesDiferentes)
aparicoesDiferentes["Marcos"] = 3
print(aparicoesDiferentes)
print("cachorro" in aparicoesDiferentes)
print("Theo" in aparicoesDiferentes)

duplas = 1
elemento = 1
chaves = 1
for elemento in aparicoesDiferentes:
    print(elemento)
for chaves in aparicoesDiferentes.keys():
    print(chaves)
for valor in aparicoesDiferentes.values():
    print(valor)
for duplas in aparicoesDiferentes.keys():
    valor = aparicoesDiferentes[duplas]
    print(duplas, valor)
for elemento in aparicoesDiferentes.items():
    print(elemento)
for chave, valor in aparicoesDiferentes.items():
    print(chave, "=", valor)
print(["palavra {}".format(chave) for chave in aparicoesDiferentes.keys()])

texto = "Bem vindo meu nome é Letícia eu gosto de cachorro e meu cachorro tem o nome de Theo"
print(texto)
texto = texto.lower()
print(texto)
palavra = 1
texto = texto.split()
contagem = defaultdict(int)
for palavra in texto:
    contagem[palavra] += 1
print(contagem)

contagem = Counter(texto)
print(contagem)



class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]
contas[17]
