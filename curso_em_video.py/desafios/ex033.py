from os import system
system ("cls")
print()

n1 = int(input("Digita o primeiro valor: "))
n2 = int(input("Digita o segundo valor: "))
n3 = int(input("Digita o terceiro valor: "))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
print()
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))