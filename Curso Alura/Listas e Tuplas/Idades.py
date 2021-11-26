idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 19

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [31,30,27,19]
print(idades)
print(type(idades))
print(len(idades))
print(idades[0])
print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)
print(idades)

idade = 1
for idade in idades:
    print(idade)

idades.remove(30)
print(idades)

if 15 in idades:
    idades.remove(15)
    print(idades)

idades.insert(0,20)
print(idades)

idades.append([27, 18])
print(idades)

for idade in idades:
    print("Recebi o elemento", idade)

idades.clear()
print(idades)

idades = [31,30,27,19]
idades.extend([27,18])
print(idades)

idadesAnoQueVem = []
for idade in idades:
    idadesAnoQueVem.append(idade+1)
print(idadesAnoQueVem)

idadesAnoQueVem = [(idade+1) for idade in idades]
print(idadesAnoQueVem)

print([(idade) for idade in idades if idade > 21])

def visualização(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)

visualização()
visualização()
