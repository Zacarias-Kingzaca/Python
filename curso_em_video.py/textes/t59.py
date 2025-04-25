from os import system
system("cls")
print()

n1 = int(input("Digita o primeiro valor: "))
n2 = int(input("Digita o segundo valor: "))
n3 = int(input("digita o terceiro valor: "))

if n1 < n2 and n2 < n3:
    print('Os números estão ordenados  em ordem crescente.')
elif n1 > n2 and n2  > n3:
    print("os números estão ordenados em ordem decrescente. ")
else:
    print("Os números estão desordenados")