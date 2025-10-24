from os import system
system("cls")
print()

matriz = []
tamanho = int(input("Digita o tamanho da matriz: "))

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        valor = int(input(f"Digita o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_total = 0
soma_diagonal = 0
elementos_diagonal = []

for i in range(tamanho):
    for j in range(tamanho):
        soma_total += matriz[i][j]
        if i == j:
            soma_diagonal += matriz[i][j]
            elementos_diagonal.append(str(matriz[i][j]))

print("Matriz digitada")
for linha in matriz:
    print(linha)

print(f"\nSoma de todos os elmentos: {soma_total}")
print(f"Soma da diagonal principal: {soma_diagonal} ({"+".join(elementos_diagonal)})")