from os import system
system("cls")
print()


nomo_a_apagar = input("Nome: ").strip().title()

with open("contatos.txt", "r", encoding="UTF-8") as f:
    linhas = f.readlines()
novo_conteudo = []
remover_bloco = False
for linha in linhas:
    if linha.startswith("Nome:"):
        if linha.strip() == f"Nome: {nomo_a_apagar}":
            remover_bloco = True
            continue #não adiciona linha
        else:
            remover_bloco = False
    if not remover_bloco:
        novo_conteudo.append(linha)
with open("contatos.txt", "w", encoding="UTF-8") as f:
    f.writelines(novo_conteudo)

if remover_bloco == True:
    print(f"o aluno {nomo_a_apagar} foi removido com sucesso. ")