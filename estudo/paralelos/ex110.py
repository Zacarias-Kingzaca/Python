from os import system
import re
system("cls")
print()

data_nascimento = "15/9/2002"

padrao = re.search(r"(\d+)\/(\d+)\/(\d+)", data_nascimento)

if padrao:
    print("Dia: ", padrao.group(1))
    print("MÊS: ", padrao.group(2))
    print("ANO: ", padrao.group(3))
