from os import system
system("cls")
print()

contador = 1
n = int(input("Digita um número para ver a sua tabuada: "))

for c in range(1, 11):
    print("{} x {:2} = {}".format(n, c, n*c))