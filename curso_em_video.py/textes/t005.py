from os import system
system ("cls")
print()

n = int(input("Digita um valor: "))

fun = n

if fun % 2 == 0:
   print("O número  {} é par".format(fun))
else:
   print("O número {} é ímpar ".format(fun))