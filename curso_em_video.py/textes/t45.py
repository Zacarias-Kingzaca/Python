from os import system
system("cls")
print()
impar = 0
for n in range(1,11):
    if n % 2 == 0:
        impar += 1
print(f"Existe {impar} números ímpar nesse intervalo.")