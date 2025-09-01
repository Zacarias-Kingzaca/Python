def nova_tarefa():
  print("==================NOVA TAREFA==================")
  try:
    tarefa = input("TAREFA: ").capitalize().strip()
  except:
    print("\033[1;31mErro, ao tentar adicionar noiva tarefa.\033[m")
  else:
    print("\033[1;32mTarefa adicionado com sucesso!")
    with open("tarefa.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"TAREFA: {tarefa}\n")
      arquivo.write("\n")

      

    