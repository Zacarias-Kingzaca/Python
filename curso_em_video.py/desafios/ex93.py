from os import system
system("cls")
print()
dados = {}
gols_marcados = []
total = 0
dados["nome"] = input("Nome do jogador: ")
part = int(input(f"Quantas partidas o {dados["nome"]} jogou? "))
for i in range(0, part):
    gols_marcados.append( int(input(f"     Quantos gols na partida {i}: ")))
dados["gols"] = gols_marcados[:]
dados["total"] = sum(gols_marcados)
print("-=-"* 30)
print(dados)
print("-=-"* 30)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print("-=-" * 30)
print(f"O jogador {dados["nome"]} jogou {part}")
for i, g in enumerate(gols_marcados):
    print(f"   => Na partida {i}, fez {g} gols")
