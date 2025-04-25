from os import system
system("cls")
print()
print(30*"=")
print("{:^30}".format("VERIFICADOR DE PALÍNDROMOS"))
print(30*"=")

palavra = input("DIGITA UMA PALAVRA: ")
reverso = palavra[::-1]
if palavra == reverso:
        print(F"A PALAVRA {palavra} é Palíndroma")
else:
        print(f"A PALAVRA {palavra} não é Palíndroma")