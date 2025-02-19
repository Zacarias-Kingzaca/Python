from os import system
system("cls")
print("")


entrada = input("Digita os números separdos por espaço: ")

numeros = list(map(int, entrada.split()))

for numero in numeros:
    if numero > 0:
        print(numero)