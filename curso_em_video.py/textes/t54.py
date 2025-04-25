from os import system
system("cls")
print()

anos = int(input("Quantos anos você tem? "))
meses = int(input("E quantos meses além dos anos? "))
dias = int(input("E quantos dias além dos meses? "))

totdias_vividos = (anos * 365) + (meses * 30) + dias
print(f"Você vive a {totdias_vividos} dias")