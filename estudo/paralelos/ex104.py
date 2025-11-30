from os import system
import re
system("cls")
print()

senha = input("E-mail: ")
padrao = re.search(r"^\w+@\w+\.(.)", senha)
if padrao:
    print("E-mail válido")
else:
    print("E-mail inválido")