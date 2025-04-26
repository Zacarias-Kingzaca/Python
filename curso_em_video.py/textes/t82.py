from os import system
system("cls")
print()


hora = int(input("Digita uma quantidade de hora para ser convertida em dias: "))

dias =  hora // 24
print(f"{dias} Dias")