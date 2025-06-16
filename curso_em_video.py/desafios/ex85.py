from os import system
system("cls")
print()

num = [[], []]
valor = 0
for i in range(1,8):
    valor = int(input(f"Digita o {i}º valor: "))
    i + 1
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(20*"-=-")
num[0].sort()
num[1].sort()
print(f"Os valores pares da lista são {num[0]}")
print(f"Os valores ímpares da lista são {num[1]}")