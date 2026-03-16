import random

def jogo():
    print("jogo de adivinhação")

    numero_secreto = random.randint(1, 10)

    tentativa = 0
    acertou = False

    while not acertou:
        palpite = int(input("digite um numero de 1 a 10: "))
        tentativa += 1

        if palpite == numero_secreto:
            acertou = True
            print(f"parabéns, você acertou o número secreto {numero_secreto} em {tentativa} tentativas!")

        elif palpite < numero_secreto:
            print("tente um número maior.")

        else:
            print("tente um número menor.")

jogo()