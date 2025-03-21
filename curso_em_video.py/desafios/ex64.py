from os import system
system("cls")
print()
n =  total = vezes = 0
while n != 999:
    n = int(input("Digite um número [999 para parar]:"))
    if n != 999:
        total += n
        vezes += 1
    else:
        print("Terminou")
print("Você digitou {} numeros e a soma entre eles foi {}".format(vezes, total))