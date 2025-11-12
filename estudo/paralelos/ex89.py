from os import system
system("cls")
print()

matriz = []

for i in range(3):
    lista = []
    for j in range(3):
        n = int(input(f"Digita o valor na posição [{i}, {j}]: "))
        lista.append(n)
    matriz.append(lista)

for linha in matriz:
    print(linha)

for i in matriz:
    soma1 = matriz[0][0], matriz[1][1], matriz[2][2]
print(f"Os números da diagonal principal são: {soma1}")
for i in matriz:
    soma2 = matriz[0][2], matriz[1][1], matriz[2][0]
print(f"Os números da diagonal secundária são: {soma2}")