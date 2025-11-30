from os import system
import re
system("cls")
print()

texto = "0 produto custa R$ 25,00 e o outro R$ 300,50"
padrao = r"\d+\w"
sub = 'XXX'
novo = re.sub(padrao, sub, texto)
print(novo)