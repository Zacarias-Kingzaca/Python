from os import system
from math import pi
system("cls")
print()

r = int(input("Digita o valor do Raio:  "))
a = int(input("Digita o valor da altura:  "))

v = pi * r**2 * a
print(f"O volume será igual a {v:.2f}")