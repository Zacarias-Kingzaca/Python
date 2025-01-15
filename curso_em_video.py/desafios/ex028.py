from os import system
system ("cls")
print()
import random

comp = random.choices("1,5")

n = int(input("Dita um numero de 1 a 5: "))

if n == comp:
    print("Usuário você venceu!")
else:
    print("O computador venceu!")