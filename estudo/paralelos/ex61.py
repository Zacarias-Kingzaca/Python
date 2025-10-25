from os import system
system("cls")
print()

num = [[], []]
valor = 0

for c in range(1, 8):
    n = int(input(f"Digita o primeiro valor {c}º : "))
    valor = n
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print()
print(f"Os número pares encontrados na lista são: {sorted(num[0])}")
print(f"Os número ímpares encontrados na lista são: {sorted(num[1])}")
