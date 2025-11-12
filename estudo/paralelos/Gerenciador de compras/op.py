from os import system
def operacao():
    while True:
            per = input("Voltar para o menu? [Sim(s)/Não(n)]: ").strip().upper()
            if per in ["SIM","S"]:
                system("cls")
                break
            elif per in ["NÃO", "N"]:
                system("cls")
                exit()
            else:
                system("cls")
                print("\033[1;31mErro digite apenas [Sim(s)/Não(n)].\033[m")