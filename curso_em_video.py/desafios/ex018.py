from os import system
import math
system ("cls")
print()

angulo = float(input("Digita o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o seno de {seno:.2f}")

cos = math.cos(math.radians(angulo))
print(f"O ângulo de {angulo} tem o cosseno de {cos:.2f}")

tan = math.tan(math.radians(angulo))
print(f"O  ângulo de {angulo} tem a tangente de {tan:.2f}")