from os import system
import re
system("cls")
print()

senha = input("Senha com números: ")
padrao = re.search(r"\d+\,*\.", senha)
if padrao:
    print("UOUUU")
else:
    print("eeheehe.")