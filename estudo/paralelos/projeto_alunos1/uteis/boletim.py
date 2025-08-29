from os import system
from centralizar import center
from time import sleep
system("cls")
print()

def consultar_boletim():
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       CONSULTAR BOLETIM\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()

    while True:
        try:
            n_estudante = int(input("Nº estudante: ").strip())
        except:
              system("cls")
              print("\033[1;31mIntroduz apenas números inteiros\033[m")
        else:
             break

    try:
            mostrar_boletim = False
            with open("aluno1.txt","r",encoding="UTF-8") as arquivo:
              bloco = []
              for linha in arquivo:
                   if linha.strip == "":
                        continue
                   bloco.append(linha)
                   if "Situação" in linha:
                        for item in bloco:
                             if f"Nº estudante: {n_estudante}".strip() in item:
                                  system("cls")
                                  print("\033[1;32mProcurando...\033[m")
                                  sleep(2)
                                  system("cls")
                                  print("".join(bloco))
                                  mostrar_boletim = True
                                  break
                        bloco = [] 
                        if mostrar_boletim:
                         break
              if not mostrar_boletim:
                   print("\033[1;31mEstudante não encontrado\033[m")           
    except:
            print("\033[1;31mConexão não establecida com A Base de dados.\033[m")