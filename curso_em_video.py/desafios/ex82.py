from os import system
system("cls")
print()

lista = []
pares = []
impares = []
while True:
    n = int(input("Digita um valor: "))
    lista.append(n)
    res = input("Quer continuar? (S/N): ")
    if res in "Nn":
        break 
print()
print("="*50)
print(f"Lista digitada: {lista}")
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"A lista de números pares: {pares}") 
print(f"A lista de números ímpares: {impares}") 
print("="*50)