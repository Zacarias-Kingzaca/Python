from os import system
system("cls")
print()

fechar = False
while True:
    print("\033[1;35m*\033[m"*50)
    print(f"{"\033[1mZACARIAS ANOTAÇÕES\033[m":^55}")
    print("\033[1;35m*\033[m"*50)

    print("""
    [ 1 ] \033[1;35mAdicionar novo resgistro\033[m
    [ 2 ] \033[1;35mLer todos os registros\033[m
    [ 3 ] \033[1;35mSair\033[m
        """)
    while True:
      op = str(input("\033[1m->\033[m "))
      if op in ["1", "2", "3"]:
          break
      else:
           system("cls")
           print("""\033[1;31mValor inválido, por favor digite apenas[1 ou 2 ou 3]:

        [ 1 ] Para adicionar novo registro
        [ 2 ] Para Ler todos os registros 
        [ 3 ] Para sair do programa

                 \033[m""")

    if op == '1':
        system("cls")
        site = input("Nome do site/plataforma: ")
        usuario = input("Nome do usuário/e-mail/nº tel: ")
        senha = input("Senha: ")
        with open("notas.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"-:\t{site}\n-:\t{usuario}\n-:\t{senha}\n")
            arquivo.write("===========================\n")
        system("cls")
    elif op == '2':
        system("cls")
        with open("notas.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
            while True:
                 sair = input("Desejas sair? [Sim/s]: ").upper().strip()
                 if sair in  ["SIM", "S"]:
                     system("cls")
                     break
                 else:
                     system("cls")
                     print("\033[1;31mPor favor digite apenas[Sim/s]\033[m")
                    
     
    elif op == '3':
        fechar = True
    if fechar == True:
        break
