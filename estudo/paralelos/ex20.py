from os import system
from op import operacao
system("cls")
print()
filmes = []
def adicionar_filme(lista):
    print("="*30)
    print(f"{"Adicionar Filme":^30}")
    print("="*30)

    try:   
        titulo = input("TÍTULO: ").strip().upper()
        ano = int(input("ANO: ").strip())
        genero = input("GÊNERO: ").strip().upper()    
    
        f = {
            "Título": titulo,
            "Ano": ano,
            "Gênero": genero
        }

        lista.append(f)
    except:
        print("\033[mErro ao tentar gravar o filme\033[m")


def listar_filmes_por_genero(lista):
    print("="*30)
    print(f"{"Lista de filmes":^30}")
    print("="*30)
    bloco = []
    genero = input("Gênero: ").strip().upper()
    for filme in lista:
      if filme["Gênero"] == genero:
          bloco.append(filme)
    if bloco:
        for i in bloco:
            for i,j in i.items():
                print(f"{i}: {j}")
            print("========================")
    else:
        print("Nenhum filme encontrado com este gênero.")



def listar_filmes_por_ano(lista):
    print("="*30)
    print(f"{"Lista de filmes":^30}")
    print("="*30)
    bloco = []
    ano = int(input("Ano: ").strip())
    for filme in lista:
        if filme["Ano"] == ano:
            bloco.append(filme)
    if bloco:
            for i in bloco:
                for i,j in i.items():
                    print(f"{i}: {j}")
                print("========================")
    else:
        print("Nenhum filme encontrado com este ano.")


while True:
    print("="*30)
    print(f"{"Menu":^30}")
    print("="*30)

    print(" 1 - Adicionar Filme")
    print(" 2 - Buscar por gênero")
    print(" 3 - Buscar por ano")
    print(" 4 - Sair")

    op = (input("Escolhe uma opção: "))
    
    if op not in ["1", "2", "3", "4"]:
        print("opção inválida")
  
    elif op == "1":
        system("cls")
        adicionar_filme(filmes)
        operacao()

    if op == "2":  
        system("cls")
        listar_filmes_por_genero(filmes)
        operacao()
    
    if op == "3":  
        system("cls")
        listar_filmes_por_ano(filmes)
        operacao()
    
    if op == "4":  
        system("cls")
        break