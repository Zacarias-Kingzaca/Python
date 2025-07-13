from os import system
from time import sleep
system("cls")
print()

c = ("\033[m",         # 0 - sem cores
     "\033[0; 30; 41m" # 1 - vermelho
     "\033[0;30; 42m"  # 2 - verde
     "\033[0; 30; 43m" # 3 - amarelo
     "\033[0; 30; 44m" # 4 - azul
     "\033[0; 30; 45m" # 5 - roxo
     "\033[7; 30"      # 7 - branco 
     )

def ajuda(com):
     system("cls")
     titulo(f"Acessando o manual do comando > {com} ")
     help(com)
     sleep(2)

    
def titulo(msg, cor=0):
    tam =len(msg) + 4
    print("\033[0; 30; 41m^" * tam)
    print(f'  {msg}')
    print("^" * tam)

  
  
#progrma principal

comando =  ""
while True:
    titulo("SISTEMA DE AJUDA PYHELP")
    comando = str(input("Comando ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')