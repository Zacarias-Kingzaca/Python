from os import system
from op import operacao
from time import sleep
system("cls")
print()

class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano


    def set_buscar_por_ano(self, ano):
    
        if ano < 1499:
            print("\033[1;31mAno inválido.\033[m")
        else:
            if self.__ano == ano:
                print(f"Título: {self.__titulo}\nAutor: {self.__autor}\nAno: {self.__ano}")
            else:
                print("\033[1;31mNenhum livro encontrado.\033[m")                      
    

    def get_ver_livro(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nAno: {self.__ano}"
                    
                    
while True:
    print("1 Adicionar Livro")
    print("2 Ver Livro")
    print("3 Bucar por ano")
    print("4 Sair")
    try:
        op = input("Escolha: ").strip()
    except:
        print("\033[1;31mErro tente novamente\033[m")
        sleep(2)
        system("cls")

    if op == "1":
        system("cls")
        try:
            titulo = input("Título do Livro: ").title()
            autor  = input("Autor: ").title()
            ano    = int(input("Ano: ").strip())
        except:
            print("\033[1;31mErro tente novamente\033[m")
            sleep(2)
            system("cls")
        else:
            livro = Livro(titulo, autor, ano)
            print("\033[1;32mLivro adicionado com sucesso\033[m")
            operacao()

    elif op == "2":
        system("cls")
        try:
            print(livro.get_ver_livro())
        except:
            print("\033[1;31mErro tente novamente\033[m")
            sleep(2)
            system("cls")
        else:
            operacao()
            
    elif op == "3":
        system("cls")
        try:
            ano = int(input("Ano: ").strip())
            livro.set_buscar_por_ano(ano)
        except:
            print("\033[1;31mNenhum livro encontrado\033[m")
            sleep(2)
            system("cls")
        else:
            operacao()

    elif op == "4":
        system("cls")
        break
    
    else:
        print("\033[1;31mEscolha inválida.\033[m")
        sleep(2)
        system("cls")
        