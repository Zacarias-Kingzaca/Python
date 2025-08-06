from os import system
system("cls")
print()

class NomeMuitoCurtoError(Exception):
    pass

def cadastar_usuario(nome):
    if len(nome) < 3:
        raise NomeMuitoCurtoError("\033[1;31mO nome deve ter pelo menos 3 letras.\033[m")
    print(f"\033[1;32mUsuário {nome} cadastrado com sucesso.\033[m")


try:
    cadastar_usuario("Za")
except NomeMuitoCurtoError as e:
    print("\033[1;31mError\033[m", e)