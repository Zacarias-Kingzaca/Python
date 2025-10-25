from os import system
system("cls")
print()


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numer_de_portas):
        super().__init__(marca, modelo, ano)
        self.n_portas = numer_de_portas


    def descricao(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano de fabrico: {self.ano}")
        print(f"Número de portas: {self.n_portas}")

    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    

    def descricao(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano de fabrico: {self.ano}")
        print(f"Cilindro: {self.cilindradas}")


v1 = Carro("Ferrar", "Turbo20x", 2020, 2)
v1.descricao()
print()
v2 = Moto("Lingkeny", "ask22", 2018, 4)
v2.descricao()
