from os import system
system ("cls")
print()


km = int(input("Qual será a distancia da sua viagem por km? "))

if km <= 200:
    passagem = km * 50
    print("A sua passagem vai custar {:.2f}kzs".format(passagem))
else:
    passagem = km * 45 
    print("A sua passagem vai custar {:.2f}kzs".format(passagem))

