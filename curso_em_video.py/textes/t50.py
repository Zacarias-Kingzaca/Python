from os import system
system("cls")
print("")

hora = int(input("Digita a Hora para ser convertida: "))
minutos = hora *  60
segundos = hora * 3600
print(f"{0}:{minutos}:{segundos}")