from os import system
system("cls")
print()
multa = 0
velocidade = int(input("Condutor digita a sua velocidade: kmh"))
if velocidade <= 80:
    print("Velecidade normal boa viagem!")
else:
     multa = velocidade - 80 
     multa *= 500
     print(f"Por estares a sima de 80kmh, a sua multa será de {multa:.2f}kzs por cada km excedido. ")