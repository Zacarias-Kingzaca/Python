from os import system
import re
system("cls")
print()

padrao = r"Burro|ESTÚPIDO|cão"
sub = "***"
texto = "Ola seu burro tudo bem estúpido."
novo = re.sub(padrao,sub, texto, flags=re.I)
print(novo)
