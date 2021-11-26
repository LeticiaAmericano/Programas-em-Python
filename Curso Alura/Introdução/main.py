import Forca
import Adivinhacao

print("Escolha seu Jogo")
print("(1) Forca")
print("(2) Adivinhação")
jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando forca")
    Forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    Adivinhacao.jogar()