from os import system
system("cls")

print("")

nome = input("Digita seu nome: ")
sobrenome = input("Digita seu sobrenome: ")

comp_nome = len(nome)
comp_sobrenome = len(sobrenome)


nome_completo = nome + " " + sobrenome

comp_nome_completo = len(nome_completo)

print(f"Comprimento do nome: {comp_nome}")
print(f"Comprimento do sobrenome: {comp_sobrenome}")

print(f"O nome completo é: {nome_completo}")
print(f"Comprimento do nome completo: {comp_nome_completo}")