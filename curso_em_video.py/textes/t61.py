from os import system
system("cls")
print()
from time import sleep
from random import randint
computador = randint(1,10)
usuario = int(input("Escolhe um número de 1 a 10: "))
print("Verificando...")
sleep(2)
if computador == usuario:
    print("Você venceu!")
else:
    print("Você perdeu!")