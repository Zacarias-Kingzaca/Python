from os import system
system ("cls")
print()


nome = str (input("Digita o seu nome: ")).strip()
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome)))

primeiro = nome.split()[0]
print("Seu primeiro nome é {} e ele tem {} letras".format(primeiro,len(primeiro)))