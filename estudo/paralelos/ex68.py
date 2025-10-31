from os import system
from abc import ABC, abstractmethod
system("cls")
print()

class Pagamento(ABC):
    @abstractmethod
    def pagar(self):
        pass


class CartaoCredo(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        return f"Pagamento de {self.valor:.2f}kzs com cartão de crédito"
    
class Pix(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        return f"Pagamento de {self.valor:.2f}kzs via Pix"
    
pag = Pix()
print(pag.pagar(2000))
print()
pag1 = CartaoCredo()
print(pag1.pagar(1000))
        