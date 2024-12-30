from os import system
import math
system ("cls")
print()

n = float(input("Digita um número: "))

print("A porção inteir do  {} é {}: ".format(n, math.trunc(n)))