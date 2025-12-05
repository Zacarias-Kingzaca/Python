from os import system
import re
system("cls")
print()

p = re.search(r"(R\$\d\.)(\d{3})(\,\d{2})", "R$1.223,00")

try:
    print(p.group(1), end="")
    print(p.group(2), end="")
    print(p.group(3))
except:
    print("Algo deu errado...")