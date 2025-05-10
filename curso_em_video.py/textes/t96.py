from os import system
from random import randint
from time import sleep
system("cls")
print()
computador = randint(1, 50)

jogador = int(input("Digita um número de 1, 50 ve se acerta: "))
sleep(1)
print("verificando...")
sleep(1)
if computador == jogador:
    print(f"O jogador venceu digitando {jogador} o mesmo que o computador {computador}")
else:
    print(f"O jogador perdeu digitando {jogador} diferente do que o computador que foi {computador}")
