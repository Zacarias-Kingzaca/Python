def nova_tarefa():
  print("==================NOVO CONTATO==================")
  try:
    nome = input("Nome: ").title().strip()
    num = int(input("Número: ").strip())
  except:
    print("\033[1;31mErro, ao tentar adicionar novo contato.\033[m")
  else:
    print("\033[1;32mContato adicionado com sucesso!\033[m")
    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"Nome: {nome}\nNº: {num}\n")
      arquivo.write("==========================================\n")
