from os import system
system("cls")
print()

distancia = float(input("Qual é a distancia da viagem por km: "))
velocidade =float(input("Qual é a velocidde média por km/h: "))
tottmpo = distancia / velocidade
hora = int(tottmpo)
minuto =int((tottmpo - hora)*60)
print(f"A viagem vai demorar {hora:.0f} hora(s) e {minuto:.0f} minuto(s)")