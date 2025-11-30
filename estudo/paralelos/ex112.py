from os import system
import re
system("cls")
print()

texto = "Olá  mundo."
padrao = bool(re.search(r"^[A-Z].*\.$", texto))
if padrao:
    print("Texto válido")
else:
    print("Texto inválido")