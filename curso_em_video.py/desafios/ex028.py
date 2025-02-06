from os import system
system ("cls")
print()
from random import randint
import time

comp = randint(0, 5)

print("\033[33m=\033[m" *50)
print("\033[1mVou pensar em um número de 0 a 5\033[m...")
print("\033[33m=\033[m" *50)

jogador = int(input("\033[1mEm que número Eu pensei\033[m? "))
print("\033[4;32mProcessando...\033[m")
time.sleep(3)
if jogador == comp:
    print()
    print("\033[1;332mParabens! Você venceu\033[m.")
else:
    print("\033[1;31mEu ganhei eu pensei no número {} e não no {}\033[m".format(comp,jogador))


