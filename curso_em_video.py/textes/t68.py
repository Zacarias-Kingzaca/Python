from os import system
system("cls")
print()

horas = int(input("Digita uma quantidade de horas: "))
minutos = int(input("Digita uma quantidade de minutos: "))
segundos = int(input("Digita uma quantidade de segundos: "))

minuto = (horas * 3600 /  60) + minutos
segundo = minuto * 60 + segundos
print(f"A quantidade de segundos convertido será de {segundo:.0f} segundos.")