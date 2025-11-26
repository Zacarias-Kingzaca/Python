from os import system
import re
system("cls")
print()

texto = "Angola é um belo lugar1"
resultado = re.search(r"(.)\1", texto)
print(bool(resultado))