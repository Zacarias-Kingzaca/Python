from os import system
system("cls")
print()

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digita o valor para posição [{i}, {j}]: "))
        linha.append(n)
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(3):
    soma_linha = sum(matriz[i])
    print(f"Soma da linha {i + 1}: {soma_linha}")

for j in range(3):
    soma_colum = matriz[0][j] + matriz[1][j] +matriz[2][j]
    print(f"Soma da coluna {i + 1}: {soma_colum}")