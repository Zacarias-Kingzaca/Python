from os import system
system ("cls")
print()


nome = input("Digita o seu nome completo: ")
print(nome)
print()
n = nome.split()
print("O primeiro nome é {}".format(n[0]))
print("O último nome é {}".format(n[len(n)-1]))