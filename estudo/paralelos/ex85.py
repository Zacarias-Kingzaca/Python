from os import system
system("cls")
print()

matriz = []
for l in range(3):
    lista = []
    for c in range(3):
        n = int(input(f"O valor na posição {[l, c]}: "))
        lista.append(n)
    matriz.append(lista)

for l in range(3):
    for c in range(3):
        print(f"{matriz[l][c]:^5}", end="")
    print()

colun1 = 0
colun2 = 0
colun3  = 0
for l in range(3):
    for c in range(3):
        colun1 += matriz[l][0]
        colun2 += matriz[l][1]
        colun3 += matriz[l][2]

linha1 = 0
linha2 = 0
linha3  = 0
for l in range(3):
    for c in range(3):
        linha1 += matriz[0][c]
        linha2 += matriz[1][c]
        linha3 += matriz[2][c]

print(f"A soma da primeira coluna é {colun1}")
print(f"A soma da segunda coluna é {colun2}")
print(f"A soma da terceira coluna é {colun3}")
print("=============================================")
print(f"A soma da primeira linha é {linha1}")
print(f"A soma da segunda linha é {linha2}")
print(f"A soma da terceira linha é {linha3}")
