from os import system
system("cls")
print()
pessoas = []
dados = {}
while True:
    dados.clear()
    dados["nome"]  = input("Nome: ")
    while True:
      dados["sexo"]  = input("Sexo [M/F]: ").upper()[0]
      if dados["sexo"] in "MF":
          break
      print("Erro! Por favor, digite apenas M ou F. ")
    dados["idade"] = int(input("Idade: "))
    pessoas.append(dados.copy())
    while True:
        res = input("Queres continuar [S/N]: ").upper()[0]
        if res in "SN":
            break
        print("Erro! Responda apenas S ou N.")
    if res in "N":
        break
    system("cls")
print("=" * 30)
