from os import system
import re
system("cls")
print()

#verificar se há algo em frente
res1 = re.findall(r"python(?=3)", "python3 é diferente de python2")
print(res1)
#verificar se não há algo em frente
res2 = re.findall(r"python3(?!2)", "python3 é diferente de python2")
print(res2)
#verificar se há algo antes do padrão
res3 = re.findall(r"(?<=R\$)\d+", "O valor é R$100")
print(res3)
#verificar se não há algo antes do padrão
res4 = re.findall(r"(?<!@)\b\w+", "@Zacarias e João")
print(res4)