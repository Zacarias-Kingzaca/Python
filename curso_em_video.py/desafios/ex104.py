from os import system
system('cls')
print()

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:  
            print(' \033[31mErro! digita um número inteiro válido.\033[m')
        if ok:
            break
    return valor
    

#programa principal
n = leiaInt("Digita um número: ")
print(f"Você acabou de digitar o número {n}")