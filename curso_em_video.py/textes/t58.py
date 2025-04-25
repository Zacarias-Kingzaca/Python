from os import system
system("cls")
print()
print("======================================")
print("{:^2}".format("CONVERSOR DE SEGUNDOS"))
print("======================================")

segundos = int(input("Digita uma quantidade de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600 ) // 60
segundos_restantes = segundos % 60
print(f"{horas}:{minutos}:{segundos_restantes}")