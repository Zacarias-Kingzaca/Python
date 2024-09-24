
from os import system 
system("cls")
print("")


from estudo.POO.paii import Papa
class Filho(Papa):
    def __init__(self):
        super().__init__("Zacarias", "12", "40")
    
    def Mesada(self):
        return f"O {filho.nome} tem a mesada de 100 mil mensal"
    
    def trabalhar(self):
        return " quando ser maior de idade Vai abrir sua própria empresa"
    
filho = Filho()
filho.estudar()
