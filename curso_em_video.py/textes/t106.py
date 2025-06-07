from os import system
system("cls")
print()

num = 12, 44, 6, 5, 4, 5, 33, 8, 9, 5
lista = []
for c in num:
    if c % 2 == 0:
        lista.append(c)

tupla = tuple(lista)
print("Tupla original:",num)
print()
print("Tupla pares", tupla)