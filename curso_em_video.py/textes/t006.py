from os import system
system ("cls")
print()

nome = input("Digita o seu nome: ")
print(nome)
print()
n = nome.split()

letra1 = n[0][0]
letra2 = n[len(n)-1][0]

print("A primeira letra do nome {} é {}".format(n[0],letra1))
print("A primeira letra do nome {} é {}".format(n[len(n)-1],letra2))
