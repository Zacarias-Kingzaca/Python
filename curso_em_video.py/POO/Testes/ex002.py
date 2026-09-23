from os import system
system("cls")
from rich import print
from rich import inspect
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
       print(Panel(f"{self.nome:^45}\n" 
       "---------------------------------------------"
       f"----------------Kz{self.preco:,.2f}-----------------"
       , title="Produto", width=50, padding=1))

p = Produto("Sansung S25", 2000_000)
p.etiqueta()
p1 = Produto("Note Book Game", 2005_000)
p1.etiqueta()