from os import system
system("cls")
print()

print(50*"=")
print("{:^50}".format("CÁLCULO DE COMBUSTÍVEL NECESSÁRIO"))
print(50*"=")

distancia = float(input("Qual é a distância da viagem em (km) "))
consumo = float(input("Qual é o consumo médio do veículo (em km/l) "))

total = distancia * consumo
print(f"Para a realizaçã da viagem será necessário {total}L de combustível.")