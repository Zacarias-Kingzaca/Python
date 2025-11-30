from os import system
import re
system("cls")
print()

nome = "Zacarias Eduardo João"
padrao = re.search(r"(\w+)\s(\w+)\s(\w+)", nome)

if padrao:
    print("Primeiro nome: ", padrao.group(1))
    print("Segundo nome: ", padrao.group(2))
    print("Terceiro nome: ", padrao.group(3))