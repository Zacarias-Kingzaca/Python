from os import system
import re

system('cls')
print()

texto = "joao@gmail.com"
padrao = re.search(r"(\w+)@(\w+)\.(\w+)", texto)

if padrao:
    print("DDD: ", padrao.group(1))
    print("Início: ", padrao.group(2))
    print("Fim: ", padrao.group(3))
