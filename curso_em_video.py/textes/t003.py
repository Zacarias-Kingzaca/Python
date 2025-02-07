from os import system
system ("cls")
print()

n1 = int(input("\033[1m Digita o Primeiro valor: \033[m"))
n2 = int(input("\033[1m Digita o segundo valor: \033[m"))
n3 = int(input("\033[1m Digita o terceiro valor: \033[m"))

media = (n1 + n2 + n3)/3

if media > 7:
    print("\033[1m A média é maior que\033[m \033[32m 7\033[m ")
else:
    print("\033[1m A média não é maior que \033[m \033[31m 7\033[m")