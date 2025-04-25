from os import system 
system ("cls")
print()

peso = float(input("Digita o seu peso: "))
altura = float(input("Digita a sua altura: "))

imc = peso/altura**2

if imc < 18.5:
    print("O seu IMC está abaixo do peso.")
elif imc > 18.5 and imc <= 24.9:
    print("O seu IMC está no seu peso normal.")
elif imc > 25.0 and imc <= 29.9:
    print("O seu IMC está no seu sobrepeso")
elif imc >= 30:
    print("O seu IMC está em obesidade.") 