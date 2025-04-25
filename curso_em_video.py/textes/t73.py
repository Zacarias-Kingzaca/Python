from os import system
system("cls")
print()

n1 = int(input("Digita o primeiro valor: "))
n2 = int(input("Digta o primeiro valor: "))

if n1 % n2 == 0:
    print(f"O número {n1} é multiplo de {n2}")
else:
    (f"O número {n1} não é multiplo de {n2}")