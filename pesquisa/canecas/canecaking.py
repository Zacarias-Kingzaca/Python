from os import system 
system("cls")
print("")

from canecas.caneca import Caneca


class CanecaKing(Caneca):
    def __init__(self ):
        super().__init__("Caneca King", "Bonito", "Azul")
        self.bebida = "café"
        self.preco = 1500


    def som(self):
        print("Eu sou o King")
 
    def beber(self):
        return super().beber() + f"{self.bebida}"
