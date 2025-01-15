from os import system
system ("cls")
print()

nome = input("Qual é o seu nome? ")

if nome == "Zacarias":
    print("Que nome lindo bom dia, {}".format(nome))
else:
    print("Bom dia, {}".format(nome))