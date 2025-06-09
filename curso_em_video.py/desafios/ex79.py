from os import system
system("cls")
print()
lista = []
while True:
    n = int(input("digita um valor: "))
    if n in lista:
     print("O número já se emcontra na lista. ")
    else:
     lista.append(n)
     print("Número adicionado com sucesso.")
    res = input("Quer continuar [S/N]: ")[0]
    if res in "Nn":
       break
print(sorted(lista))

    