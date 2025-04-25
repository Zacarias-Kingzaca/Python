from os import system
from time import sleep
system("cls")
print()

segundos = 300
for i in range(segundos,0,-1):
    system("cls")
    print(f"Restam {i} segundos para o despertador tocar.", end="")
    sleep(1)