from os import system
system("cls")
print()
numeros  = []
pares = []
for i in range(1, 11):
    num = int(input("Digita um número: "))
    numeros.append(num)
system("cls")
print(f"Maior número da lista {max(numeros)} Menor número {min(numeros)}")
media = sum(numeros) / len(numeros)
print(f"Média é igula: {media}")
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
print(f"Números pares da lista {pares}")