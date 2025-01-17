from os import system
system ("cls")
print()

n = int(input("Me diga um número qualquer? "))

resultado = n % 2

if resultado == 0:

    print("O {} é um  número Par.".format(n))
else:
    print("O {} é um número Ímpar.".format(n))