from os import system
from op import operacao
from time import sleep
system("cls")
print()


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


class Biblioteca:
    def __init__(self):
        self.livros = []


    def adicionar_livro(self, livro):
        self.livros.append(livro)


    def listar_livros(self):
        if self.livros:
            for i in self.livros:
                print(f"Titulo: {i.titulo}\nAutor: {i.autor}\nAno: {i.ano}")
                print("="*30) 
        else:
            print("\033[m1;31Nenhum Livro cadastrado!\033[m")


    def buscar_por_nome(self, titulo):
        for i in self.livros:
            if i.titulo.lower() == titulo.lower():
                print(f"Titulo: {i.titulo}\nAutor: {i.autor}\nAno: {i.ano}")
                return 
        else:
                print("\033[1;31mNemhum livro encontrado!\033[m")

bibliteca = Biblioteca()

while True:

    print("="*30)
    print(f"{"LIVRARIA ZACARIAS":^30}")
    print("="*30)

    print("1- Adicionar Livro")
    print("2- Listar livros")
    print("3- Buscar por Titulo")
    print("4- Sair")
    op = input("Digita a sua opção: ")

    if op == "1":
        system("cls")
        print("="*30)
        print(f"{"ADICIONAR LIVRO":^30}")
        print("="*30)
        titulo = input("Titulo do Livro: ").strip().title()
        autor = input("Autor do Livro: ").strip().title()
        ano = input("Ano do Lançamento: ").strip()
        livro = Livro(titulo,autor,ano)
        bibliteca.adicionar_livro(livro)
        operacao()

    elif op == "2":
        system("cls")
        print("="*30)
        print(f"{"LISTA DE LIVROS":^30}")
        print("="*30)
        bibliteca.listar_livros()
        operacao()
    
    elif op == "3":
        system("cls")
        print("="*30)
        print(f"{"BUSCAR LIVRO POR NOME":^30}")
        print("="*30)
        print("\n")
        titulo = input("Dita o Titulo: ").strip().title()
        bibliteca.buscar_por_nome(titulo)
        operacao()

    elif op == "4":
        system("cls")
        break

    else:
        print("\033[1;31mOpção inválida.\033[m")
        sleep(3)
        system("cls")
        
        

#biblioteca = Biblioteca()
#l1 = Livro("zacarias", "Lua", 2000)
#l2 = Livro("King", "sol", 2000)

#biblioteca.adicionar_livro(l1)
#biblioteca.adicionar_livro(l2)
#biblioteca.buscar_por_nome("King")