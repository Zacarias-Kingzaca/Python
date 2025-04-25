from os import system
system("cls")
print()

temperatura = int(input("Digita a temperatura atual: "))
if temperatura <= 18:
    print("É aconselhavel usar casaco hoje...")
else:
    print("Não será necessário usar casaco...")