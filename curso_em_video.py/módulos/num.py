from os import system
system("cls")
print("")
from uteis import números
from uteis import strings
num = int(input("Digita um valor: "))
fat=números.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {números.dobro(num)}")
