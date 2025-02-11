from os import system
system ("cls")
print()

num = int(input("Digite um número inteiro: "))

print("""Escolha uma base para conversão:

     \033[33m [ 1 ] CONVERTER PARA BINÁRIO
      [ 2 ] CONVERTER PARA OCTAL
      [ 3 ] CONVERTER PARA HEXADECIMAL\033[m """)
print()
op = int(input("Sua opção: "))

if op == 1:
    print("{} convertido para BINÁRIO é igual a \033[32m{}\033[m ".format(num, bin(num)[2:]))
elif op == 2:
    print("{} convertido para OCTAL é igual a \033[32m{}\033[m ".format(num, oct(num)[2:]))
elif op == 3:
    print("{} convertido em HEXADECIAML é igual a \033[32m{}\033[m ".format(num, hex(num)[2:]))
else:
    print("\033[31mOpcão invalída, Tente novamente...\033[m")