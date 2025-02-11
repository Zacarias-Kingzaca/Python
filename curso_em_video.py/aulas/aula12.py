from os import system
system ("cls")
print()

nome = input("Digita o seu nome: ")

if nome == "Zacarias":
   print("Olá, que nome bonito Zacarias!")
elif nome == "Rodrigo" or nome == "Itamar" or nome == "Oliveira":
   print("O seu nome é bonito {}".format(nome))
elif nome in "Zaca kingzaca king":
   print("Que nome legau {}".format(nome))
else:
   print("Olá  {}".format(nome))