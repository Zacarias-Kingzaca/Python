from os import system
system ("cls")
print()


n1 = int(input("Primeior valor: "))
n2 = int(input("Segundo valor: "))

if n1 > n2:
    print("O primeiro valor digitado {} é maior".format(n1))
else:
    print("O segundo valor digitado {} é maior".format(n2))