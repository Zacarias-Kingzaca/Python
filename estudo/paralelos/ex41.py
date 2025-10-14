from os import system
from op import operacao
system("cls")
print()

class Filme:
    def __init__(self, titulo, genero, avaliacoes):
        self.titulo = titulo
        self.genero = genero
        self.avaliacoes = avaliacoes


    def media_avaliacoes(self):
        if self.avaliacoes:
          return sum(self.avaliacoes) / len(self.avaliacoes)
        return 0
         

class  Catalogo:
    def __init__(self):
        self.filmes = []


    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    
    def listar_por_genero(self, genero):
        encontrou = False
        for f in self.filmes:
            if f.genero.lower() == genero.lower():
                print(f"Título: {f.titulo}")
                print(f"Gênero: {f.genero}")
                print(f"Avaliações: {f.avaliacoes}")
                print("="*55)
                encontrou = True
        if not encontrou:
            print("Nenhum filme encontrado.")

        
    def melhor_avaliacao(self):
        if self.filmes:
            return max(self.filmes, key=lambda a: a.media_avaliacoes())
        return None
    
catalogo = Catalogo()

while True:
    print("1 - Adicionar filme")
    print("2 - Listar por gênero")
    print("3 - Melhor avaliação")
    print("4 - sair")
    op = input("Escolha: ")

    if op == "1":
        system("cls")
        titulo = input("Título do filme: ").capitalize()
        genero = input("Gênero do filme: ").capitalize()
        avaliacoes = list(map(float, input("Digita três notas de 0 a 10 separadas por espaço: ").split()))
        f = Filme(titulo, genero, avaliacoes)
        catalogo.adicionar_filme(f)
        operacao()

    elif op == "2":
        system("cls")
        genero = input("Gênero do filme: ").capitalize()
        catalogo.listar_por_genero(genero)
        operacao()

    elif op == "3":
        system("cls")
        melhor = catalogo.melhor_avaliacao()
        if melhor:
            print(f"\nMelhor filme: {melhor.titulo} com {melhor.media_avaliacoes():.2f}")
        else:
            print("Nenhum filme cadastrado.")    
        operacao()

    elif op == "4":
        system("cls")
        break

    else:
        print("Opçãp inválida.")