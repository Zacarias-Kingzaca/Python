from os import system
system("cls")
print()

n = int(input("Digita um número para ver a sua tabuada: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")