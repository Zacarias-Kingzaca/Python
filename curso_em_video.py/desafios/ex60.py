from os import system
system("cls")
print("")

n = int(input("Digita um valor: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{} ".format(c), end="")
    print("x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print('{}'.format(f))