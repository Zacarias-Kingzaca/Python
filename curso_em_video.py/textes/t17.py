from os import system
system("cls")
print()

frase = input("Digita uma frase: ").split()

for palavra in frase:
 if len(palavra) > 3:
    print("A palavra {} tem mas de três letras".format(palavra))
else:
    print("A palavras {} tem menos de três letras".format(palavra))