from os import system
system("cls")
print()

entrada = input("Digita um conjunto de números separados por espaço: ")

lista = list(map(int, entrada.split()))

for numero in lista:
    if numero > 0:
        print("Números positivos: {}".format(numero))
    elif numero < 0:
        print("Números negativos: {}".format(numero))
    elif numero == 0:
        print("Quantidade de zeros: {}".format(numero))