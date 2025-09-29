from os import system
from op import operacao
system("cls")
print()

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def aplicar_desconto(self,porcentagem):
        desconto = self.preço * (porcentagem / 100)
        self.preço -= desconto
        print(f"{self.nome} custa {self.preço}")
    
p1 = Produto("Camisola", 1000)
p2 = Produto("Tênis", 2000)
desconto = float(input("Desconto: "))
p1.aplicar_desconto(desconto)
print("=================================")
p2.aplicar_desconto(desconto)
     