from os import system
from centralizar import center
from time import sleep
system("cls")
print()

def retificar_dado():
    print()
    center("\033[1;35m      =========================================\033[m")
    center("\033[1;35m       RETIFICAR DADOS\033[m")
    center("\033[1;35m      =========================================\033[m")
    print()
    num = input("Digite o Nº de estudante: ").strip()

    try:
        with open("aluno1.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    blocos = []
    bloco_atual = []

    for linha in linhas:
        if linha.strip() == "==========================================":
            if bloco_atual:
                blocos.append(bloco_atual)
                bloco_atual = []
        else:
            bloco_atual.append(linha)
    if bloco_atual:
        blocos.append(bloco_atual)

    encontrou = False
    for i, bloco in enumerate(blocos):
        if any(f"Nº estudante: {num}" in linha for linha in bloco):
            encontrou = True
            print("\nBloco encontrado:")
            print("".join(bloco))
            print("\nO que deseja retificar?")
            print("1 - Nome")
            print("2 - Notas")
            print("3 - Todo o bloco")
            opcao = input("Escolha uma opção: ").strip()
            if opcao not in ["1", "2", "3"]:
             while True:
              print("\033[1;31mOpção inválida, espere 5 segundos para voltar para o menu.\033[m")
              opcao = input("Escolha uma opção: ").strip()
              if opcao in ["1", "2", "3"]:
                  break
            if opcao == "1":
                while True:
                    nome = input("Nome: ").title().strip()
                    if not nome.isdigit():
                        break
                    else:
                        sleep(1)
                        system("cls")
                        print("\033[1;31mO nome não pode conter números nem símbolos.\033[m")
                for j in range(len(bloco)):
                    if bloco[j].startswith("Nome:"):
                        bloco[j] = f"Nome: {nome}\n"
                        break

            elif opcao == "2":
                while True:
                  try:
                     nova_nota1 = float(input("Nova Nota2: ").strip())
                  except:
                       system("cls")
                       print("\033[1;31mIntroduz apenas números inteiros\033[m")
                  else:
                      break
                for j in range(len(bloco)):
                    if bloco[j].startswith("Nota1:"):
                        bloco[j] = f"Nota1: {nova_nota1}\n"
                        break


                while True:
                  try:
                     nova_nota2 = float(input("Nova Nota2: ").strip())
                  except:
                       system("cls")
                       print("\033[1;31mIntroduz apenas números inteiros\033[m")
                  else:
                      break
                for j in range(len(bloco)):
                    if bloco[j].startswith("Nota2:"):
                        bloco[j] = f"Nota2: {nova_nota2}\n"
                        break


                media = (nova_nota1 + nova_nota2) / 2
                if media >= 10:
                    situacao = "Aprovado"
                else:
                    situacao = "Reprovado"
                for j in range(len(bloco)):
                    if bloco[j].startswith("Situação:"):
                        bloco[j] = f"Situação: {situacao}\n"
                        break

            elif opcao == "3":
              while True:
                    nome = input("Nome: ").title().strip()
                    if not nome.isdigit():
                        break
                    else:
                        sleep(1)
                        system("cls")
                        print("\033[1;31mO nome não pode conter números nem símbolos.\033[m")
              for j in range(len(bloco)):
                    if bloco[j].startswith("Nome:"):
                        bloco[j] = f"Nome: {nome}\n"
                        break  


              while True:
                  try:
                     nova_nota1 = float(input("Nova Nota2: ").strip())
                  except:
                       system("cls")
                       print("\033[1;31mIntroduz apenas números inteiros\033[m")
                  else:
                      break
              for j in range(len(bloco)):
                    if bloco[j].startswith("Nota1:"):
                        bloco[j] = f"Nota1: {nova_nota1}\n"
                        break


              while True:
                  try:
                     nova_nota2 = float(input("Nova Nota2: ").strip())
                  except:
                       system("cls")
                       print("\033[1;31mIntroduz apenas números inteiros\033[m")
                  else:
                      break
              for j in range(len(bloco)):
                    if bloco[j].startswith("Nota2:"):
                        bloco[j] = f"Nota2: {nova_nota2}\n"
                        break


              media = (nova_nota1 + nova_nota2) / 2
              if media >= 10:
                    situacao = "Aprovado"
              else:
                    situacao = "Reprovado"
              for j in range(len(bloco)):
                    if bloco[j].startswith("Situação:"):
                        bloco[j] = f"Situação: {situacao}\n"
                        break
            break

    if not encontrou:
        print("Aluno não encontrado.")
        return

    with open("aluno1.txt", "w", encoding="utf-8") as f:
        for bloco in blocos:
            for linha in bloco:
                f.write(linha)
            f.write("==========================================\n")

    print("\n\033[1;32mAlteração feita com sucesso!\033[m")
