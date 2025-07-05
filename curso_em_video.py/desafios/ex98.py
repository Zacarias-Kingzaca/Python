from os import system
from time import sleep
system("cls")
print()
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=-" * 18)
    print(f"CONTADOR DE {i} a {f} de {p} em {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")     


contador(1, 10, 1)
print("-=-" * 18)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem: ")
ini = int(input("Início:  "))
fim = int(input("Fim:     "))
passo = int(input("Passo: "))
contador(ini, fim, passo)

