from collections import Counter

texto01 = "Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios: B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação. Por fim, vamos colocar tudo isso em prática para vermos algum exemplo diferente? Então o que eu queria fazer agora não é um contador de palavras, eu fazer um contador de letras para vermos uma coisa interessante que acontece na língua portuguesa e em outras línguas, para ser sincero, também. Então eu vou criar aqui uma nova sessão que é #Testando o uso de diversas coleções."
texto02 = "Então tem um monte de coisa legal para fazermos e de quebra vemos uma coisa aqui da distribuição das frequências das letras na língua portuguesa, que é um toque interessante utilizado para questões básicas de criptografia, de criptografias básicas e chaves de criptografia muito básicas que são razoavelmente tranquilas de quebrar. Então uma curiosidade para vocês. Então com isso vimos como utiliza diversas coleções e no mundo real, aí afora, você vai utilizar diversas delas a medida do possível e do necessário. Não tenha medo de consultar documentação, de procurar um uso de cada uma delas. Utilizamos lista aqui, ou quase tudo, de alguma maneira. Utilizamos lista aqui, iteração em cima lista, list comprehension, dicionário, contador, e laços em cima disso, e impressão, e cálculos em cima disso, várias coisas do gênero. Inclusive no final, vimos que até a API de counter, ela é mais do que uma pura contadora, ela traz funções para trabalharmos em cima da contagem, como por exemplo, os mais comuns."

def frequenciaLetras(texto01):
    aparicoes = Counter(texto01.lower())
    print(aparicoes)
    totalAparicoes = sum(aparicoes.values())
    print(totalAparicoes)

    letra = 1
    frequencia = 1
    for letra, frequencia in aparicoes.items():
        tupla = (letra, frequencia/totalAparicoes)
        print(tupla)

    letra = 1
    frequencia = 1
    lista = [(letra, frequencia/totalAparicoes) for letra, frequencia in aparicoes.items()]
    print(lista)
    dicionario = Counter(dict(lista))
    maisComuns = dicionario.most_common(10)
    caractere = 1
    proporcao = 1
    for caractere, proporcao in maisComuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))

frequenciaLetras(texto01)
frequenciaLetras(texto02)
