from os import system
system ("cls") 
print()

soma = 0
cont = 0 

for c in range(1,7):
    n = int(input("Digita o {} valor: ".format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print("Voçê informou {} números pares e a soma foi {}".format(cont,soma))