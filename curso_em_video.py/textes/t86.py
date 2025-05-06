from os import system
system("cls")
print()

anos = int(input("Quantos anos tens? "))

meses = anos * 12
dias = anos * 365.25

print(f"MESES: {meses}")
print(f"DIAS: {dias}")