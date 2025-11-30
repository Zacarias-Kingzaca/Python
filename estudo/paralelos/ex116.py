from os import system
import re
system("cls")
print()

print(bool(re.search(r"linha1.*linha2","linha1\nlinha2", re.S)))