from os import system
system("cls")
print()

lista = []

while True:
    n = int(input("Digita um valor: "))
    lista.append(n)
    res = input("Quer continuar? (S/N): ")
    if res in "nN":
        break
    else:
        if res not in "sSnN":
             res = input("Quer continuar? (S/N): ")
print(F"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {lista[-1::]}"
)
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")

  