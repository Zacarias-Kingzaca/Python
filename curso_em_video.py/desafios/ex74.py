from os import system
from random import randint
system("cls")
print("")

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print("Os valores digitados foram: ",end=" ")
for n in numeros:
    print(f"{n}", end=" ")
print(f"\nO maior número digitado foi o {max(numeros)}")
print(f"O menor números digitado foi o {min(numeros)}")