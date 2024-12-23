from os import system
import math
system ("cls")
print()

angulo = float(input("Digita o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o seno de {seno:.2f}")

cosseno = math.cos(math.radians(angulo))
print(f"O ângulo  de {angulo} tem o cosseno {cosseno:.2f}")

tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem a tengente de {tangente:.2f}")
