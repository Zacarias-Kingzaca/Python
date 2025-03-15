from os import system
system("cls")
print()
from random import randint
comp = randint(0, 10)
print("\033[1;32m========== SOU O SEU COMPUTADOR ACABEI DE PENSEAR EM UM NÚMERO DE 0 A 10 ==========\033[m")
print("»»»»» TENTA ADIVINHAR »»»»»")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite: "))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("MAIS, tente novamente.")
        elif jogador > comp:
            print("MENOS, tente novamente.")
print("Acertou com {} tentativas.Parabéns!".format(palpites ))

