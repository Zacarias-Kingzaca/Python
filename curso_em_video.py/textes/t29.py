from os import system
system ("cls")
print()
segundos = int(input("Digita uma quantidade de segundos que desejares: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restante = segundos % 60
print(f"{horas}:{minutos}:{segundos_restante}")