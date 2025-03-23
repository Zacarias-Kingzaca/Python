from os import system
system("cls")
print()
soma = cont = 0
n = 0
while True:
     n = int(input("Digita um valor (999 para parar): "))
     if n == 999:
        break    
     cont += 1
     soma += n
print(f"A soma dos {cont} valores foi {soma}")