from os import system
system ("cls")
print()

frase = str(input("Digita uma frase: ")) .strip()

fr = frase.upper()

print("A letra *A* aparece {} vezes na frase".format(fr.count("A")))
print("A letra *A* aparece na {} posição na sua primeira vez".format(fr.find("A")+1))
print("A letra *A* aparece na  {} posição na sua última vez".format(fr.rfind("")+1))
