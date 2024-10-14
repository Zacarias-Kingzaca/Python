from os import system
system ("cls")
print()

n1 = int(input("Digita o primeiro valor:"))
n2 = int(input("Digita o segundo valor:"))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {}, o produto é  {} e a divisão é {:3f}".format(s, m, d), end=" ")
print("Divisão inteira {} e Potencia {}". format(di,e))