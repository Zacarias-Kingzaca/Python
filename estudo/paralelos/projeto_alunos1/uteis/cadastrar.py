from os import system
from centralizar import center
from time import sleep
system("cls")
print()


def cadastrar_aluno():
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       CADASTRAR ALUNO\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()
    
    while True:
            nome = input("Nome: ").title().strip()
            if not nome.isdigit():
                break
            else:
                sleep(1)
                system("cls")
                print("\033[1;31mO nome não pode conter números nem símbolos.\033[m")
     
    while True:
                   
            try:
                 num = int(input("Nº de estudante: ").strip())
            except:
                    system("cls")
                    print("\033[1;31mIntroduz apenas números inteiros\033[m")
            else:
                 break
            
    while True:
         abrir = False
         with open("aluno1.txt","r", encoding="UTF-8") as arquivo:
             linhas = arquivo.readlines()
             for linha in linhas:
                  if f"Nº estudante: {num}".strip() in linha:
                       system("cls")
                       print("\033[1;31mErro o número digitado já pertecence a um aluno.\033[m")
                       sleep(5)
                       while True:
                          try:
                            num = int(input("Nº de estudante: ").strip())
                          except:
                            system("cls")
                            print("\033[1;31mIntroduz apenas números inteiros\033[m")  
                          else:
                               break             
                  else:
                    abrir = True 
         if abrir == True:
              break 
                                                        
    while True:
         try:
              n1 = float(input("Nota1: ").strip())
              n2 = float(input("Nota2: ").strip())
         except:        
            print("\033[1;31mErro introduz apenas números.\033[m")
         else:
           break

    media = (n1+n2) / 2
    if media >= 10:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    try:
        with open("aluno1.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.write(f"Nº estudante: {num}\nNome: {nome}\nNota1: {n1}\nNota2: {n2}\nSituação: {situacao}\n")
            arquivo.write(f"==========================================\n")
            print("\033[1;32mCadastrado com sucesso!\033[m")
            sleep(2)
    except:
            print("\033[mErro impossível cadastrar, arquivo não encontrado.")