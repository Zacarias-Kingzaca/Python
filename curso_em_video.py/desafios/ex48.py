from os import system
system ("cls")
print()

soma = 0
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
     cont += + 1
     soma += n
print("A soma de todos os {} valores soliciados é {}".format(cont, soma))
