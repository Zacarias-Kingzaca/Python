from os import system
import re
system("cls")

email = "teste@exemplo.com"
padrao = r"\w+@\w+\.\w+"

if re.match(padrao, email):
    print("E-mail válido")
else:
    print("E-mail inválido") 