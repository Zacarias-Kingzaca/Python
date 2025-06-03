from os import system
system("cls")
print()

num =  (int(input("Digita um valor: ")),
        int(input("Digita um valor: ")),
        int(input("Digita um valor: ")),
        int(input("Digita um valor: ")))
print(f"Você digitou os valores {num}")
print(f"O número 9 foi digitado {num.count(9)}")
if 3 in num:
 print(f"O primeiro valor 3 foi digitado na posição {num.index(3)+1}º")
else:
   print("O número 3 não foi digitado em nenhuma posição")
print("Os números pares digitados foram", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end="")