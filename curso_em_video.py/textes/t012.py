from os import system
system("cls")
print("")

n = int(input("Digita um valor: "))

if n % 3 == 0 and n % 5 == 0:
    print("O número {} é divisivel pelo 3 e pelo 5 ao mesmo tempo.".format(n))
else:
    print("O número {} não é divisivel por 3 e por 5 ao mesmo tempo.".format(n))