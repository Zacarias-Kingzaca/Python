from os import system
import re
system("cls")
print()

email = "Zacarias@gmail.com zacarias@gmail.org zaca@gmail.org zacariaskingzaca@gmail.com"
padrao = re.findall(r"\w+@\w+\.com", email)
print(padrao)