from os import system
system("cls")
print()

matriz = []
for l in range(4):
    lista = []
    for c in range(3):
        n = int(input(f"Digita o valor na posição [{l}, {c}]: "))
        lista.append(n)
    matriz.append(lista)

for linha in matriz:
    print(linha)

for linha in range(4):
    maior = max(matriz[linha])
    print(f"O maior valor da linha {linha + 1} é: {maior}")
    