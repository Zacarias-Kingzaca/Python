from os import system
system("cls")
print()

nome = ["ana", "carlos", "João", "maria", "lu", "fernando", "bia"]
nomes_filtrados = [n.capitalize() for n in nome if len(nome) >= 5]
nomes_filtrados = sorted(nomes_filtrados)
print(nomes_filtrados)