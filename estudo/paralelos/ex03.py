from os import system
system("cls")
print()

def convidados(*nome,saudacao="Bem-Vindo"):
    nomes_unicos = list(set(nome))
    nomes_unicos = [n.capitalize() for n in nomes_unicos]
    agrupados = {}
    for nome in nomes_unicos:
        ultima = nome[-1].lower()
        if ultima not in agrupados:
            agrupados[ultima] = []
            agrupados[ultima].append(nome)
   
    print(f"{saudacao}! Lista de convidados: \n")
    for letra,lista in agrupados.items():
        print(f"Letra '{letra}': {lista}")

    print(f"\nTotal de convidados: {len(nomes_unicos)}")

convidados("ana", "joão", "maria", "luana", "joão", "bia", "maria",saudacao='ola')