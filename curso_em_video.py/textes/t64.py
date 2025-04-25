from os import system
system("cls")
print()
palavra = input("Digita uma palavra: ")
contador1 = palavra.count("a")
contador2 = palavra.count("e")
contador3 = palavra.count("i")
contador4 = palavra.count("o")
contador5 = palavra.count("u")
tot = contador1 + contador2 + contador3 + contador4 + contador5
print(tot)