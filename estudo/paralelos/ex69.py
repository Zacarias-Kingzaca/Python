from os import system
from abc import ABC, abstractmethod
system("cls")
print()

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Forma):
    def area(self, lado):
        self.lado = lado
        return f"A area desse quadrado é de {self.lado * self.lado} centimetros." 
    
    def perimetro(self,lado):
        self.lado = lado
        return f"O perimetro desse quadrado é de {self.lado * 4} centimetros." 
    
class Circulo(Forma):
    def area(self, raio):
        self.raio = raio
        return f"A area desse Circulo é de { 3.14 * self.raio**2} centimetros." 
    
    def perimetro(self,raio):
        self.raio = raio
        return f"O perimetro desse quadrado é de {2 * 3.14 * self.raio } centimetros." 
    
quad = Quadrado()
print(quad.area(10))
print(quad.perimetro(10))
print()
circ = Circulo()
print(circ.area(11))
print(circ.perimetro(11))
       