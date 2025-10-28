from os import system
system("cls")
print()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira_coluna = 0
m_segunda_linha = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digita um número [{i}, {j}]: "))
print("=-"*50)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end=" ")
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j] 
        if matriz[i][j] == matriz[i][2]:
            terceira_coluna += matriz[i][j]
        if matriz[i][j] == matriz[1][j]:
            if m_segunda_linha == 0:
                m_segunda_linha = matriz[i][j]
            if m_segunda_linha < matriz[i][j]:
                m_segunda_linha = matriz[i][j]
    print()
print()
print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da terceira coluna é {terceira_coluna}")
print(f"O maior valor da segunda linha é {m_segunda_linha}")
