from os import system
import re
system("cls")
print()

#re.IGNORECASE (re.I)
print(re.findall(r'PYTHON', "o python é uma grande linguagem.", re.I))
print()
#re.IGNORECASE (re.M)
print(re.findall(r'python', "o python é uma grande linguagem, amo python.", re.M))
print()
#re.DOTAL (re.S)
print(re.findall(r'olá.+', "olá, o python é uma grande linguagem, amo python.", re.S))
print()
#re.IGNORECASE (re.M)
p = re.compile(r"""123-23""", re.X)
print(p)
