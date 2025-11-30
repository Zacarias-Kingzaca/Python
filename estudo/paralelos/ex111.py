from os import system
import re

system('cls')
print()
texto = "maria123@gmail.com"
padrao = re.search(r"(\w+)@(\w+)\.(\w+)", texto)

if padrao:
    print("parte antes @: ", padrao.group(1))
    print("Domínio: ", padrao.group(2))
    print("TLD: ", padrao.group(3))
