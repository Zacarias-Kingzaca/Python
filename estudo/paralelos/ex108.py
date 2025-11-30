from os import system
import re
system("cls")
print()


num = "(244) 9471-85654"
padrao = re.search(r"(.\d+.)\s(\d+)\-(\d+)", num)

if padrao:
    print("DDD: ", padrao.group(1))
    print("Início: ", padrao.group(2))
    print("Fim: ", padrao.group(3))