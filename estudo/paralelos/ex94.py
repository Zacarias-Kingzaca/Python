from os import system
import re
system("cls")


texto = "Karias00"
padrao = r"[aeiouAEIOU]"

print(bool(re.search(padrao, texto)))
 