from os import system
system ("cls")
print()


n = input("digita o seu nome: ").strip().upper()
print(n[:4]=="KING")
print("ZACA" in n)
print("O seu nome em maiúscula é {}".format(n.upper()))
print("O seu nome em minúscula é {}".format(n.lower()))
print("A letra *A* aparece {} vezes no nome {}".format(n.count("A"),n))
print("A letra *A* aparece na {} posição pela primeira vez".format(n.find("A")+1))
print("A letra *A* aparece na {} posição pela última vez".format(n.rfind("A")+1))
nome = n.split()
print("O seu primeiro nome digitado foi {}".format(nome[0]))
print("O segundo nome digitado foi {}".format(nome[len(nome)-1]))
