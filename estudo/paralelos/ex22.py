from os import system
system("cls")
print()

class carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
          self.velocidade += 10
    
    def frear(self):
        self.velocidade -= 10

    
meu_carro = carro("Toyota", "preto")
meu_carro.acelerar()
print(meu_carro.velocidade)