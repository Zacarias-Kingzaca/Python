from os import system
from time import sleep
system("cls")
print()

op = 0
soma = 0
mult = 0
maior = 0

n1 = int(input("Primeiro valor: "))
n2  = int(input("Segundo valor: "))
while op != 5:
    print(50*"=")
    print("\t\tESCOLHA A OPÇÃO")
    print(50*"=")

    print("""
            \033[1;31m[ 1 ] \033[m \033[1;32mSomar  \033[m 
            \033[1;31m[ 2 ]\033[m \033[1;32m Multipliacr \033[m 
            \033[1;31m[ 3 ]\033[m \033[1;32m Maior \033[m 
            \033[1;31m[ 4 ]\033[m \033[1;32m Novos números \033[m 
            \033[1;31m[ 5 ]\033[m \033[1;32m Sair do programa \033[m 
        """)
    op = int(input("Qula é a sua opção: "))

    if op == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é igual a {}".format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print("A multiplicação entre {} e {} é igual a {}".format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print("O maior número entre {} e {} é o {} ".format(n1, n2, maior))
        else:
            maior = n2
            print("O maior número entre {} e {} é o {} ".format(n1, n2, maior))
    elif op == 4:
        print()
        n1 = int(input("Primeiro valor: "))
        n2  = int(input("Segundo valor: ")) 
    elif op == 5:
        print("Finalizando")
    else:
        print("Opção inválida tente novamente...") 
    sleep(2)

print("Programa Terminado.")