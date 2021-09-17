import random

def jogar():

    print("Jogo de Adivinhação")

    numero_secreto = round(random.randrange(1,101))
    acertou = False
    rodada = 1
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade deseja escolher?")
    print("(1) Facil")
    print("(2) Medio")
    print("(3) Dificil")
    nivel = int(input("Definir o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        primeiro_valor = int(input("Digite o seu numero entre 1 e 100:"))
        print("Você digitou ",primeiro_valor)

        if(primeiro_valor < 1 or primeiro_valor > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == primeiro_valor
        maior = primeiro_valor > numero_secreto
        menor = primeiro_valor < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            print("Você acertou")
        else:
            if maior:
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - primeiro_valor)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo")

jogar()

#for rodada in range (x,y,z)
#x = inicio - y = fim - z = quantidade que soma

#break = quebra de laço
#continue = sai da interação e continua na proxima

#formatação de numeros
#{:f}.format() = tamanho float
#{:7.2f} = sete espaços sendo 2 apos o ponto

#random gera um numero entre 0.0 e 1.0

#// = devolve o valor inteiro da divisão