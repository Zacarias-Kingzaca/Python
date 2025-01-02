from os import system
import random
system ("cls")
print()

n1 = input("Digita o nome do primeiro aluno :")
n2 = input("Ditgita o nome do segundo aluno :")
n3 = input("Ditgita o nome do terceiro aluno :")
n4 = input("Ditgita o nome do quarto aluno :")

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print("A ordem de aprsentação será: {} ".format(lista))
