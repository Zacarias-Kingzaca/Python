from os import system
system("cls")
print()
import re

#Ex 1
print(re.findall(r"python", "eu amo PYTHON e  python3", re.I))
#Ex 2
texto = """Olá mundo
python é legal 
JavaScript também."""
resultado = re.findall(r"^[a-z].*", texto, re.M)
print(resultado)
#Ex 3
texto = """<div>
Conteúdo IMPORTANTE
</div>"""
resultado = re.findall(r".*\w.*", texto, re.S+re.I)
print(resultado)
#Ex 4
regex = re.compile(r"""
[\w.]+ #usuário (letras, número, ponto)              
@      #arroba 
[\w.]+ #domínio
\.     #ponto
[\w.]+  #extensão
""", re.I | re.X)
texto = ("Zacarias123@Gmail.com")
print(bool(regex.match(texto)))
