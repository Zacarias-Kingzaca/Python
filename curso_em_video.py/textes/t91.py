from os import system
from random import randint
from time import sleep
system("cls")
print()
while True:
    computador = randint(1,100)
    print(computador)
    sleep(0.5)
    if computador > 90:
        print(f"STOP NÚMERO MAIOR QUE 90 ENCONTRADO:{computador}")
        break


