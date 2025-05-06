from os import system
system("cls")
print()

v_inicial = float(input("Digita a velocidade inicial: "))
aceleracao = float(input("Digita a aceleração: "))
tempo = int(input("Digita o tempo: "))

deslocamento = v_inicial * tempo + 0.5 * aceleracao * (tempo**2)
print(f"O deslocamento é de {deslocamento:.2f} metros")