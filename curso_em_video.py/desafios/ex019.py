from os import system
import random
system ("cls")
print()

n1 = input("Primeiro aluno:")
n2 = input("Segundo aluno:")
n3 = input("Terceiro aluno:")
n4 = input("Quarto aluno:")

lista = [n1, n1, n3, n4]
escolhido = random.choice(lista)

print(f"O aluno/a escolhido é o/a {escolhido}")