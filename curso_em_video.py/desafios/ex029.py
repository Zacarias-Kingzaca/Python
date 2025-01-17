from os import system
system ("cls")
print()

print("*"*50)
print("LENDO VELOCIDADE DE UM CARRO")
print("*"*50)

velocidade = int(input("Digita a velocidade do seu carro por hora? "))

if  velocidade > 80:
    multa = velocidade - 80
    valor = multa * 1000
    print("O seu carro ultrapassou a velocidade de 80km/h tendo a velocidade de {}km/h a sua multa vai ser de {}kzs".format(velocidade,valor))
else:
    print("Parabens pela velocidade na média!")
    