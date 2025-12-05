from os import system
import re 
system("cls")
print()

emails = """Zacarias123@gmail.com
    zaca123@gmail.ao.com
    zacA@gmail.edu
    zacarias@gmail.org"""


print(re.findall(r"\w+@\w+\.edu|\w+@\w+\.org|\w+@\w+\.com", emails, re.I))