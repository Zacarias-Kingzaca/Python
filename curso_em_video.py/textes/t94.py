from os import system 
from random import randint
from time import sleep
system("cls")
print()
um = dois = tres = quatro = cinco = seis = 0
for i in range(1,100):
    computador = randint(1,50)

    print(computador)
    if computador == 1:
        um += 1
    elif computador == 2:
        dois += 1
    elif computador == 3:
        tres += 1
    elif computador == 4:
        quatro += 4
    elif computador == 5:
        cinco += 1
    elif computador == 6:
        seis += 1

print(f"foram lançado o número 1 {um} vezes ")
print(f"foram lançado o número 2 {dois} vezes ")
print(f"foram lançado o número 3 {tres} vezes ")
print(f"foram lançado o número 4 {quatro} vezes ")
print(f"foram lançado o número 5 {cinco} vezes ")
print(f"foram lançado o número 6 {seis} vezes ")
