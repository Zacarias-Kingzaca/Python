from os import system
import re
system("cls")
print()

ide = input("Digita o seu iD: ")
res = re.match(r"^[A-Z]{2}\d{4,6}", ide)
if res:
    print("Bem-vindo")
else:
    print("ID inválido.")

