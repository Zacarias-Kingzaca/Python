from os import system
system ("cls")
print()
from random import randint
import time

comp = randint(0, 5)

print("=" *50)
print("Vou pensar em um número de 0 a 5...")
print("=" *50)

jogador = int(input("Em que número Eu pensei? "))
print("Processando...")
time.sleep(3)
if jogador == comp:
    print("Parabens! Você venceu.")
else:
    print("Eu ganhei eu pensei no número {} e não no {}".format(comp,jogador))


