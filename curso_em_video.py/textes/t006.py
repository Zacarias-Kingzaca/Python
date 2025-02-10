from os import system
system ("cls")
print()

nome = input("Digita o seu nome: ")
print(nome)
print()
n = nome.split()

letra1 = n[0][0]

print("A primeira letra do nome {} é {}".format(n[0],letra1))
