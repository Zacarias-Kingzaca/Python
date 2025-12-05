from os import system
import re
system("cls")
print()

palavra = "Hoje falei com (Carlos) e depois com Maria e João"

print(re.findall(r"(?<!\()\b[A-Z][a-z]+\w+", palavra))