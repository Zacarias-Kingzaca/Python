from os import system
system ("cls")
print()

frase = input("Digita uma frase: ").upper()

procura1 = frase.count("A")
procura2 = frase.count("E")
procura3 = frase.count("I")
procura4 = frase.count("O")
procura5 = frase.count("U")

n = frase.lower()
total = procura1 + procura2 + procura3 + procura4 + procura5
print("O total de vogais que existe na frase {} são {}".format(n,total))