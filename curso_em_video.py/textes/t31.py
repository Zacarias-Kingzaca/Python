from os import system

system("cls")
print()

ano = int(input("Digita um ano para verificar se é ou não é BISSEXTO: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é BISSEXTO")
else:
    print(f"O ano de {ano} NÃO É BISSEXTO")
