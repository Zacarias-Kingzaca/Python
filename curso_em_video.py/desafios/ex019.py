from os import system
import random
system ("cls")
print()

n1 = str (input("Primeiro aluno:"))
n2 = str (input("Segundo aluno:"))
n3 = str (input("Terceiro aluno:"))
n4 = str (input("Quarto aluno:"))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f"O aluno sorteado é {escolhido}")


