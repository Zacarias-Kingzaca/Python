from os import system
system("cls")
print()

with open("dados.txt", "a") as arquivo:
    arquivo.write("Peso: 60.3kg\n")
    arquivo.write("Altura: 1.70\n")
with open("dados.txt", "r") as ler:
    print(ler.read())