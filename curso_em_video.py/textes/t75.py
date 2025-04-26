from os import system
system("cls")
print()

frase = input("Digita uma frase: ").strip()
contador = frase.split()
palavras = len(contador)
print(palavras)
 