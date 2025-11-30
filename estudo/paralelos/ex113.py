from os import system
import re
system("cls")
print()


num = "Ligue para (11) 99243-7292 ou (21) 93243-7293"
padrao = re.search(r"(.\d+.)(.\d+.)\-(.\d+.)\s\w+\s(.\d+.)(.\d+.)\-(.\d+.)", num)
if padrao:
    print("DDD: ", padrao.group(1))
    print("DDD: ", padrao.group(4))
  
