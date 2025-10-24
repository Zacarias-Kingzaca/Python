from os import system
system("cls")
print()
pessoas = []
dados = {}
soma = media = 0
while True:
    dados.clear()
    dados["nome"]  = input("Nome: ")
    while True:
      dados["sexo"]  = input("Sexo [M/F]: ").upper()[0]
      if dados["sexo"] in "MF":
          break
      print("Erro! Por favor, digite apenas M ou F. ")
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    pessoas.append(dados.copy())
    while True:
        res = input("Queres continuar [S/N]: ").upper()[0]
        if res in "SN":
            break
        print("Erro! Responda apenas S ou N.")
    if res in "N":
        break
    system("cls")
system("cls")
print("=" * 50)
print(f"A) Ao todo foram cadastrado {len(pessoas)} pessoas.")
media = soma / len(pessoas)
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram  ", end=" ")
for p in pessoas:
    if p["sexo"] in "Ff":
        print(f"{p["nome"]}", end=" ")
print()
print("D) Lista de pessoas que estão a sima da média: ")
for p in pessoas:
    if p["idade"] >= media:
        print("     ", end="")
        for k, v in p.items():
            print(f"{k} = {v}", end=" ")
        print()
print("=" * 50)
print("<< ENCERRADO >>")
