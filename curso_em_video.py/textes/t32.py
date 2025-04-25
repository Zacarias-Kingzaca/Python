from os import system
system("cls")
print()
positivo = negativo = 0
for i in range(1,11):
    n = int(input("Digita um valor: "))
    if n > 0 :
     positivo += 1
    else:
       negativo += 1
print(f"Foram digitados {positivo} números positivos.")
print(f"Foram digitados {negativo} números negativos")
