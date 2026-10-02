from os import system
system("cls")
from rich import print
from time import sleep


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):
        return f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} paginas no total, você está na pagina 1."

    def avancar_paginas(self, page):
        num_pagina = 1
        for p in range(page):
            num_pagina =+ 1
            print(f"Você avançou {num_pagina} paginas.")


l1 = Livro("King", 10)
print(l1)
l1.avancar_paginas(2)