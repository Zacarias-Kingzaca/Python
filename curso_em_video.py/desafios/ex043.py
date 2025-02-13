from os import system
system ("cls")
print()

peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é a sua altura? (m)"))
imc = peso / (altura ** 2)

print("O IMC dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você está a baixo do peso normal.")
elif 18.5 <= imc < 25:
    print("Parabéns, você  está na faixa de peso normal.")
elif 25 <= imc < 30:
    print("Você está em Sobrepeso.")
elif 30 <= imc < 40:
    print("Você está em Obesidade.")
elif imc >= 40:
    print("Você está em obesidade mórbida cuidado.")