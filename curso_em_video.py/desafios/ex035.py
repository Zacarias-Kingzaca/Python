from os import system
system ("cls")
print()

print("\033[1;34m-=\033[m"*30)
print("\033[1;36m Analisador de Triângulo\033[m")
print("\033[1;34m-=\033[m"*30)



r1 = float(input("\033[1m Digita o primeiro seguimento: \033[m "))
r2 = float(input("\033[1m Digita o segundo segmento: \033[m"))
r3 = float(input("\033[1m Digita o terceiro segmento: \033[m"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("\033[1;32m OS SEGMENTOS A CIMA PODEM FORMAR UM TRIÂNGULO.\033[m")
else:
    print("\033[1;31m OS SEGMENTOS A CIMA NÃO PODEM FORMAR UM TRIÂNGULO\033[m")