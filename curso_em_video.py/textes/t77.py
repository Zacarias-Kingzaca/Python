from os import system
from random import randint
from time import sleep
system ("cls")
print()

computador = randint(0, 15)
print("="*30)
print("{:^30}".format("JOGO DE PAR OU ÍMPAR"))
print("="*30)

print("ESCOLHE UM NÚMERO DE 0 A 10")
jogador = int(input("ESCOLHA [par/impar]: "))
print("Sorteando...")
sleep(1)
if jogador % 2 == 0 and computador % 2 == 0:
    print(f"O JOGADOR VENCEU, JOGANDO {jogador} E O COMPUTADOR JOGANDO {computador}, AMBOS NÚMEROS PAR")
elif jogador % 2 == 1 and computador % 2 == 1:
    print(f"O JOADOR VENCEU, JOGANDO {jogador} E O COMPUTADOR JOGANDO {computador}, AMBOS NÚMEROS ÍMPAR")
else:
    print(f"O COMPUTADOR VENCEU, JOGANDO {computador} E O JOADOR {jogador}")
