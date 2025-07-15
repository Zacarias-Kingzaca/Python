from os import system
system("cls")
print("")
 

def fatorial(n):
    f = 1
    for c in range(n,0, -1):
        f *= c
    return f


num = int(input("Digita um valor: "))
fat=fatorial(num)
print(f"O fatorial de {num} é {fat}")