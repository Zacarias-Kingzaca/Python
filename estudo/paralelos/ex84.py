from os import system
import json
system("cls")

dados = {
    'Nome': 'Zacarias',
    'Idade': 18,
    'Ativo': True,
    'Cursos': ["Python", "Git"]
}

with open("usuario.json", 'w', encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

with open("usuario.json", "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)