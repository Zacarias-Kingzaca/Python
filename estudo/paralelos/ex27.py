from os import system
system("cls")
print()

class Filme:
    def __init__(self, titulo, genero, avaliacoes):
        self.titulo =  titulo
        self.genero = genero
        self.avaliacoes = avaliacoes

    
    def media_avaliacões(self):
      if self.avaliacoes:
         return  sum(self.avaliacoes) / len(self.avaliacoes)
      return 0

    
class Catalogo:
   def __init__(self):
      self.filmes = []

   def adicionar_filme(self,filme):
      encontrou = True
      for f in self.filmes:
         if f.titulo.lower() == filme.titulo.lower():
            encontrou = True
            break
         if not encontrou:
            self.filmes.append(filme)
            print("\033[1;31mFilme adicionado com sucesso!\033[m")
         else:
            print("\033[1;31mEste Filme já está cadastrado!\033[m")
 

   def listar_por_genero(self, genero):

      for f in self.filmes:
          if f.genero.lower() == genero.lower():
            (f"Titulo: {f.titulo}\n Gênero: {f.genero}\n Avaliacões: {f.avaliacoes}\n")
            print("=======================================")
          else:
             print("\033[1;31mNenhum filme desse gênero encontrado.\033[m")

   def filme_com_maior_avaliacao(self):
        return max(self.filmes, key=lambda a: a.media_avaliacoes())
    

F = Catalogo()

f1 = Filme("Jack chan", "Comedia", [10, 7, 9])
f2 = Filme("Mr Bean", "Comedia", [10, 9, 9])
f3 = Filme("Biladen", "Acção", [10, 10, 9])

F.adicionar_filme(f1)
F.adicionar_filme(f1)
F.adicionar_filme(f1)

F.listar_por_genero("Comediia")

