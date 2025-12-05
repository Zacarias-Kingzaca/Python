from os import system
import re
system("cls")
print()

palavra = "@Hoje: falei com (Carlos) e @depois: com Maria e João"
print(re.findall(r"(?<=@)\w{5,}(?=:)", palavra))

texto = """
Coragem!
Determinção
Ano de 2025
Bom
LU
Pessoas
Ana
Humanidade
"""
print(re.findall(r"\b\w{3,7}\b", texto))