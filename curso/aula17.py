from os import system
system("cls")
print('')
mat = []

for i in range(3):
    linha = [int (input(f"Digita o elemento da posicao [{i}][{j}]: ")) for j in range(4)]
    mat.append(linha)

maior = max([max(linha) for linha in mat])
menor = min([min(linha) for linha in mat])
pos_maior = [(i, linha.index(maior)) for i,linha in enumerate(mat) if maior in linha][0]
pos_menor = [(i, linha.index(menor)) for i,linha in enumerate(mat) if menor in linha][0]
print("")
print(20*"=")
print(f"O maior elemento é {maior} na posição {pos_maior}")
print(f"O menor elemento é {menor} na posição {pos_menor}")
print(20*"=")