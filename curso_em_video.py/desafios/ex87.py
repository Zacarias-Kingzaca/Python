from os import system
system("cls")
print()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digita um valor [{l}, {c}]: "))    

print("-=-"*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print("-=-"*30)

print(f"A soma dos valores pares é {somap}")
for l in range(0, 3):
    somac += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {somac}")
for i in matriz[1]:
  if  maior < i:
      maior = i
print(f"O maior valor da segunda alinha é {maior}")

