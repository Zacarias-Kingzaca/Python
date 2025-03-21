from os import system
system("cls")
print()


n = int(input("Digita um valor para ver o seu Fatorial: "))
i = n
f = 1

for i in range(n+1, 1, -1):
    c = i -1
    f *= c
print(" {} != {} ".format(n,f))
