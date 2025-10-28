from os import system
from abc import ABC, abstractmethod
system("cls")
print()


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def primetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
    def primetro(self):
        return 2 + (self.largura + self.altura)

objeto = Retangulo(22, 10)
print(objeto.area())
print(objeto.primetro())