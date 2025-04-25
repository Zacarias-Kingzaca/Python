from os import system
system("cls")
print()


idade = int(input("Digita a sua idade: "))
print("Você é maior de idade" if idade >= 18 else "Você é menor de idade.")