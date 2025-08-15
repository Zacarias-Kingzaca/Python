from os import system
system("cls")
print()

with open("dados.txt", "w+") as arquivo:
    arquivo.writelines("Nome: João\n")
    arquivo.writelines("Idade: 20\n")
with open("dados.txt", "r") as ler:
        abrir = ler.read()
        print(abrir)
