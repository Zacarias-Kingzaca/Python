from os import system
import re
system("cls")
print()

texto = "A casa do joão 1 é grande para ser a casa dele 8.".lower().capitalize()
resultado = re.findall(r"\d", texto)
print(resultado)
