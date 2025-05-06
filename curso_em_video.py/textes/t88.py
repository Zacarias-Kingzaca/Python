from os import system
system("cls")
print()

horas_extras = int(input("Digita a quantidade de horas extras trabalhada: "))

total =  15 *  horas_extras
print(f"O valor a ser recebido será de {total:.2f}kzs")