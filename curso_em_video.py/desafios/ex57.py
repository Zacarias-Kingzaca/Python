from os import system
system("cls")
print()


sexo = input("Informe  o seu sexo [M/F]: ").strip().upper()[0]
while sexo not in "Mm/Ff":
    sexo = input("Dados inválido por favor, informe o seu sexo [M/F]: ").strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))