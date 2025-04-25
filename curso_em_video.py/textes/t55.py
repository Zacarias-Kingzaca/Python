from os import system
system("cls")
print()

print("=========================")
print("CONVERSOR DE VELOCIDADE")
print("=========================")
m_s = 0
kmh = float(input(" velocidade em Km/h: "))
from time import sleep
sleep(1)
print("Convertendo...")
sleep(1)
m_s = kmh / 3.6
print(f"{kmh:.2f}km/h é igual a {m_s:.2f}m/s ")

