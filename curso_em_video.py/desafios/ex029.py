from os import system
system ("cls")
print()

print("\033[33m*\033[m"*50)
print("\033[1mLENDO VELOCIDADE DE UM CARRO\033[m")
print("\033[33m*\033[m"*50)

velocidade = int(input("\033[1mDigita a velocidade do seu carro por hora\033[m? "))

if  velocidade > 80:
    multa = velocidade - 80
    valor = multa * 1000
    print("O seu carro ultrapassou a velocidade de \033[31m80km/h\033[m tendo a velocidade de \033[31m{}km/h\033[m a sua multa vai ser de \033[32m{:.2f}kzs\033[m".format(velocidade,valor))
else:
    print("\033[1;32mParabens pela velocidade na média!\033[m")
    