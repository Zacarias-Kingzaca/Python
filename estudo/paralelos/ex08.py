from os import system
system("cls")
print()

class NomeInvalidoError(Exception):
    pass
def cadastrar_usuario(nome):
    if len(nome) < 5:
        raise NomeInvalidoError(f"\033[1;31mNome com\033[m \033[m{len(nome)}\033[m \033[1;31mcaractere(s), inválido por favor digite um nome válido.\033[m")
    print(f"Usuário \033[1;32m{nome.capitalize()}\033[m cadastrado com sucesso.")

while True:
    try:
        n = cadastrar_usuario(input("Nome: "))
        break
    except NomeInvalidoError as n:
        print("\033[1;31mError\033[m", n)