from os import system
system("cls")
print("")

matriz = []

for i in range(3):
    lista = []
    for j in range(3):
        n = int(input(f"Digita o valor na posição [{i}, {j}]: "))
        lista.append(n)
    matriz.append(lista)
print()
print("Primeira matriz")
for linha in matriz:
    print(linha) 
print()  
nova = list()
for i in range(3):
    lista = []
    for j in range(3):
        lista.append(matriz[j][i])
    nova.append(lista)
print("Segunda matriz")
for lista in nova:
    print(lista)