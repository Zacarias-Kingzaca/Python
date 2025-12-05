from os import system
import re 
system("cls")
print()

emails = """Bom dia 
#olá mundo! 
#Tudo bem
#é nós a estudar python!
"""


print(re.findall(r"(?<=#)\w.+(?=!)", emails))