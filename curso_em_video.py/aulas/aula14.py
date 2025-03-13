from os import system
system("cls")
print()
n = 1
pares = impares = 0
while n != 0:
    n = int(input("Digita um valor: "))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print("Você digitou o total de {} números pares e {} números ímpares".format(pares,impares))