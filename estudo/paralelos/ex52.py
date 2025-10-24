from os import system
system("cls")
print()

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digita um valor {[i]}{[j]}: "))
        linha.append(n)
    matriz.append(linha)

for i in matriz:
    print(i)
media = []
for j in range(3):
    media_coluna = 0
    soma_coluna = 0
    for i in range(3):
        soma_coluna += matriz[i][j]
    media_coluna += soma_coluna / 3 
    media.append(media_coluna)
    print(f"A soma da coluna {j}: {soma_coluna} com a média: {media_coluna}")
maior = max[media_coluna, lambda a: a.media_coluna]
print(maior)
