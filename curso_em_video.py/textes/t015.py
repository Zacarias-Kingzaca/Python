from os import system
from random import randint
system("cls")
print()

comp = randint(1,100)

print("Usuário qual foi o número que o computador escolheu entre 1 a 100? ")
n = int(input("Digita: "))

if comp == n:
    print("\033[1;32m Usuário você acertou, o computador escolheu {} e tu escolheu também {} \033[m".format(comp, n))
else:
    print("\033[1;31m Você errou o computador escolheu {} e tu escolheu {} \033[m".format(comp,n))