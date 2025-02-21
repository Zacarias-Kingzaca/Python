from os import system
system("cls")
print()

n1 = int(input("Digita um valor: "))
n2 = int(input("Digita um valor: "))
n3 = int(input("Digita um valor: "))
n4 = int(input("Digita um valor: "))

media = (n1 + n2 + n3 + n4) / 4

print("A media da soma de {} + {} + {} + {} é = {}".format(n1, n2 ,n3 ,n4, media))