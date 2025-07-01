from os import system
system("cls")
print()                 

lista = [2, 4, 8, 12]
def dobra(lis):
    p = 0
    for p in range (0, len(lista)):
        lista[p] *= 2

print(lista)
dobra(lista)
print(lista)