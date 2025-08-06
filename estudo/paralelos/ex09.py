from os import system
system("cls")
print()

class SenhaFracaError(Exception):
    pass
class senhaMenorDeOitoCaracteres(Exception):
    pass
def introduzir_senha(senha):
    string = any(letra.isalpha() for letra in senha)
    numero = any(num.isdigit() for num in senha)
    if string and numero and len(senha) > 7:
        print("\033[1;32mSenha forte\033[m")
    else:
        if len(senha) < 8:
            raise senhaMenorDeOitoCaracteres("\033[1;31ma senha deve conter mas de 8 caracteres\033[m")
        else:
            raise SenhaFracaError("\033[1;31ma senha deve conter números e letras.\033[m")

while True:
    try:
        sen = introduzir_senha(input("Senha -> "))
        break
    except senhaMenorDeOitoCaracteres as senha:
        print("\033[1;31mErro\033[m", senha)
    except SenhaFracaError as senha:
        print("\033[1;31mErro\033[m", senha)

    
