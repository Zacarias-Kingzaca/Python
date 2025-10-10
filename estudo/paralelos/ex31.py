from os import system
from time import sleep
system("cls")
print()

print("="*30)
print(f"{"Cadastro de nome":.^30}")
print("="*30)
nomes = []
while True:
    nome = input("Digita um nome: ").title()
    if nome in nomes:
        print("O nome digitado já existe.")
    else:
        nomes.append(nome)
        print("Nome adicionado com sucesso!")
    p = input("Desejas continuar? [S/N]").strip().upper()
    if p in "S":
        continue
    elif p in "N":
        break
    else:
        print("Opção inválida.")
        while True:
            p = input("Desejas continuar? [S/N]").strip().upper()
            if p in "SN":
                break
            else:
               print("Opção inválida.")

               
system("cls")
lista = sorted(nomes)
print("="*30)
print(f"{"Nome Cadastrados":.^30}")
print("="*30)
for i in lista:
    print(i)
    