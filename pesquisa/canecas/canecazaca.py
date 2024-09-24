from os import system 
system("cls")
print("")

from canecas.caneca import Caneca


class CanecaZaca(Caneca):
    def __init__(self ):
        super().__init__("Caneca Angola", "Cidade Luanda", "Branca")
        self. bebida = "água"
        self.preco = 1200

    def extras(self):
        print("como bonus vc ganha uma caneca a mais")

    def beber(self):
        return "Ta na hora de beber a sua água"
