from os import system
system("cls")
print()

n1 = int(input("Digita um valor: "))
n2 = int(input("Digita um valor: "))
n3 = int(input("Digita um valor: "))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1 :
    print("Os lados digitados podem formarm um teiângulo.")
else:
    print("Os lados digitados  não podem formar um triângulo.")