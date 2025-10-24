from os import system
system("cls")
print()

class Carro:
    def __init__(self, modelo, ano, velocidade):
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade

    
    def set_acelerar(self, valor):
        if valor > self.__velocidade:
            self.__velocidade = valor
        return 0
        
    
    def set_frear(self, frear):
        if frear < self.__velocidade:
            self.__velocidade = frear
        return 0
    
    def get_componentes(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Ano: {self.__ano}")
        print(f"Velocidade: {self.__velocidade}km/h")

carro = Carro("Toyota2025", 2025, 80)
carro.set_acelerar(100)
carro.set_frear(50)
carro.get_componentes()