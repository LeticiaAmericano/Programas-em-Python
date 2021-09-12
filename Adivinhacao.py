print("Jogo de Adivinhação")

numero_secreto = 10
primeiro_valor = int(input("Digite o seu numero:"))

print("Você digitou ",primeiro_valor)

acertou = numero_secreto == primeiro_valor
maior = primeiro_valor > numero_secreto
menor = primeiro_valor < numero_secreto

if acertou:
    print("Você acertou")
else:
    if maior:
        print("Você errou! Seu chute foi maior que o número secreto.")
    elif menor:
        print("Você errou! Seu chute foi menor que o número secreto.")

print("Fim do Jogo")