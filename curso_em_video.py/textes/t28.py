from os import system
system("cls")
print()
n = int(input("Digita um número inteiro: "))
print(f"O número {n} é par" if n % 2 == 0 else "O número {n} é ímpar")