from os import system
from time import sleep
system("cls")
print()

n1 = int(input("Digita o primeiro número: "))
n2 =int(input("Digita o segundo número: "))
print("Agora espera a numeração dos mesmos.")
sleep(1)
for i in range(n1, n2+1):
    print(i,end=" ")