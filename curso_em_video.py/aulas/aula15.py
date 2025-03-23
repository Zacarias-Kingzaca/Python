from os import system
system("cls")
print()
n = 1
s = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    s += n
print(f"A soma vale {s}")