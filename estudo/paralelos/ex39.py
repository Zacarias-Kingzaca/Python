from os import system
from op import operacao
system("cls")
print()

class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao


class Playlist:
    def __init__(self):
        self.lista = []


    def adicionar_musica(self, musica):
        self.lista.append(musica)

    
    def listar_musicas(self):
        if self.lista:
            for m in self.lista:
                print(f"Titulo: {m.titulo}")
                print(f"Artista: {m.artista}")
                print(f"Duração: {m.duracao}")
                print("="*50)
        else:
            print("Nenhuma música encontrada.")

    def duracao_total(self):
        try:
            duracao = 0
            for m in self.lista:
                duracao += m.duracao
        except:
            print("Nenhuma música encontrada.")
        else:
            print(f"A duração total da Playlist é {duracao} minutos")


playlist = Playlist()

while True:
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Mostrar duração total da playlist")
    print("4 - Sair")
    op = input("Escoha: ")
            
    if op == "1":
        system("cls")
        titulo = input("Titulo da música: ").title()
        artista = input("Nome do artista: ").title()
        duracao = int(input("Duracão da música: ").strip())
        musica = Musica(titulo, artista, duracao)
        playlist.adicionar_musica(musica)
        operacao()

    elif op == "2":
        system("cls")
        playlist.listar_musicas()
        operacao()

    elif op == "3":
        system("cls")
        playlist.duracao_total()
        operacao()

    elif op == "4":
        system("cls")
        break

    else:
        print("Opcão inválida.")
    