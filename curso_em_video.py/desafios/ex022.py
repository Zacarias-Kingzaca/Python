from os import system
system ("cls")
print()

nome = str(input("Digita o seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiscúlas é {}".format(nome.upper()))
print("Seu nome em menúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras ".format(len(nome) - nome.count('')))
#print("Seu primeiro nome tem {} letras".format(nome.find('')))
separa = nome.split()

print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))


