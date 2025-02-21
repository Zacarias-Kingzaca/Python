from os import system
system("cls")
print()

n1 = int(input("Digita um valor: "))
n2 = int(input("Digita um valor: "))
n3 = int(input("Digita um valor: "))
n4 = int(input("Digita um valor: "))

menor = n1

if n2 < n1 and n2 < n3 and n2 < n4:
    menor = n2
elif n3 < n1 and n3 < n2 and n3 <n4:
    menor = n3
elif n4 < n1 and n4 < n2 and n4 < n3:
    menor = n4

print("O menor valor digitado foi {}".format(menor))