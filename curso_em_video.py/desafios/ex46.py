from os import system
from time import sleep
system("cls")
print()

for c in range(10, 0, -1):
    sleep(0.5)
    print("\033[1;32m{}\033[m".format(c))
print("\033[1;31mBUM! BUM! POOOW!\033[m")