from os import system
system("cls")
print()
divisiveis = 0
n = int(input("Digita um número: "))
for i in range(1, n):
    if n % i == 0:
     print(f"Os números divisiveis por {n} são {i}")
