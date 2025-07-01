from os import system
system("cls")
print()
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador["nome"] = input("Nome do jogador: ")
    tot = int(input(f"Quantas partidas o {jogador["nome"]} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append( int(input(f"     Quantos gols na partida {c + 1}: ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy)
    while True:
        res = input("Quer continuar [S/N]: ").upper()[0]
        if res in "SN":
            break
        print("Erro! por favor digita apenas S ou N: ")
    if res == "N":
        break
system("cls")
print("=" * 50)
print("cod ", end="")
for i in jogador.keys():
    print(f" {i:<15}", end='')
print() 
print("-" * 50)
for k, v in enumerate(time):
    print(f'{k:>3}', end="")
    for k, d  in enumerate(time):
        print(f"{str(d):<15}", end=" ")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogdor (999 para parar):  "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador com código {busca} ")
    else:
        print(F" -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ")
        for i, g in enumerate(time[busca]['gols']):
            print(f"      No jogo {i + 1} fez {g} gols")
        print("-" * 40)
print("<<VOLTE SEMPRE>>")
