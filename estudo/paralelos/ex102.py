from os import system
import re
system("cls")
print()

senha = input("Senha: ")
padrao = re.search(r"^[A-Z].*\.", senha)
if padrao:
    print("UOUUU")
else:
    print("eeheehe.")