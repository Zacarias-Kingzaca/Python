def cadastrar_produto():
    print("========================================")
    print("           CADASTRAR PRODUTO")
    print("========================================")

    try:
      nome = input("Nome: ").capitalize().strip()
      preco = float(input("Preço: ").strip())
      cod = int(input("Código: ").strip())
      encontrou = False
      while True:
         print(f"O Código {cod} já pertence a um produto.")
         cod = int(input("Código: ").strip())
         with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            bloco = []
            for linha in conteudo:
               bloco.append(linha)
               if "*******************************************" in linha.strip():
                for dado in bloco:
                   if dado.startswith("Código:"):
                     if dado in  f"Código: {cod}":
                        encontrou = False
                     else:
                         encontrou = True
                bloco = []
         if  encontrou:
            break
    except:
       print("\033[1;31mFalha ao cadastrar produto\033[m")
    else:
       print("\033[1;32mProduto cadastrado com sucesso!\033[m")
       try:
         with open("produtos.txt", "a", encoding="utf-8") as arquivo:
          arquivo.write(f"Código: {cod}\nNome: {nome}\nPreço: {preco:.2f}\n")
          arquivo.write("*******************************************")
       except:
           print("\033[1;31mErro ao tentar conectar-se com a Base de dados.\033[m\n")