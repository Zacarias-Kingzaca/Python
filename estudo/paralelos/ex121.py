from os import system
import re
system("cls")
print()

texto = "Olá mundo, amanhã será maravilhosoo!"

padrao = re.match(r"^[A-Z].*(.)\1.*[.!]", texto)
if padrao:
    print("Frase correta!")
else:
    print("Frase incorreta...")
