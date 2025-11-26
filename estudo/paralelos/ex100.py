from os import system
import re
system("cls")
print()


texto = input("Digita uma palavra: ")

padrao = re.search(r"(.)\1", texto)
if padrao:
    print("Há letras repetidos")
else:
    print("Não há letras repetidos.")
