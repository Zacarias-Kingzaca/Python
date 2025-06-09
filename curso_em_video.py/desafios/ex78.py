from os import system
system("cls")
print()

lista = []
maior = 0
menor = 0

for i in range(5):
    n = int(input("Digita um valor: "))
    lista.append(n)
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
           maior = lista[i]
        if lista[i] < menor:
           menor = lista[i]

print(30*"=")
print(f"o maior valor digitado é o {maior} digitado nas posições", end=" ")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}....", end="")
print()
print(f"o menor valor digitado é o {menor} digitado nas posições", end=" ")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}....", end="")
print()