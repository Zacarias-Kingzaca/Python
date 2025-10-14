from os import system
system("cls")
print()

class Filme:
    def __init__(self, titulo, genero, avaliacoes):
        self.titulo =  titulo
        self.genero = genero
        self.avaliacoes = avaliacoes

    def media_avaliacoes(self):
        if self.avaliacoes:
         return sum(self.avaliacoes) / len(self.avaliacoes)
        return 0
         

class Catalogo:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        for f in self.filmes:
            if f.titulo.lower() == filme.titulo.lower():
                print("\033[1;31mEste filme já cadastrado.\033[m")
                return
        self.filmes.append(filme) 
        print("\033[1;32mFilme adicionado com sucesso!\033[m")

    def listar_genero(self, genero):
        encontrou = False
        for f in self.filmes:
            if f.genero.lower() == genero.lower():
                print(f"\nTitulo: {f.titulo}")
                print(F"Gênero: {f.genero}")
                print(f"Avaliações: {f.avaliacoes}")
                encontrou = True
        if not encontrou:
            print("\033[1;31mNenhum filme desse gênero encontrado.\033[m")

    def  filme_com_maior_avaliacoes(self):
        if self.filmes:
            return max(self.filmes, key=lambda a: a.media_avaliacoes())
        return None
    

catalogo = Catalogo()

while True:
    print("\n1 - Adicionar Filme")
    print("2 - Listar por Gênero")
    print("3 - Listar Avaliado")
    print("0 - Sair")
    op = input("Escolha: ")

    if op == "1":
        titulo = input("Título do filme: ")
        genero = input("Gênero do filme: ")
        avaliacoes = list(map(float, input("Digita 3 notas separadas por espaço: ").split()))
        f = Filme(titulo, genero, avaliacoes)
        catalogo.adicionar_filme(f)

    elif op == "2":
        genero = input("Qual gênero deseja listar? ")
        catalogo.listar_genero(genero)

    elif op == "3":
        melhor = catalogo.filme_com_maior_avaliacoes()
        if melhor:
            print(f"\nMelhor filme: {melhor.titulo} com {melhor.media_avaliacoes():.2f}")
        else:
            print("Nenhum filme cadastrado.")
            
    elif op == "0":
        break
    
    else:
        print("Opção inválida")

    