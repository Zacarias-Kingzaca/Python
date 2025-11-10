from os import system
import json
system("cls")
print()

pessoas = [

     {
    "Nome": "Zacarias",
    "Idade": 30,
    "Hobbies": ["Escrever", "Jogar futebol", "programar"] 
    },

     {
    "Nome": "Agapé",
    "Idade": 3,
    "Hobbies": ["ler", "escrever", "atuar"] 
    },

     {
    "Nome": "Olna",
    "Idade": 3,
    "Hobbies": ["cantar", "escrever", "criar coisas"] 
    }

]


with open("usuario.json", "w", encoding="utf-8") as f:
    json.dump(pessoas, f, indent=4)

with open("usuario.json", "r", encoding="utf-8") as f:
    nome = input("Digitao nome da pesssoa que deseja ver os dados? ")
    dados = json.load(f)
    for n in dados:
        if n["Nome"].lower() == nome.lower():
            print(f"Nome: {n["Nome"]}")
            print(f"Idade: {n["Idade"]} anos")
            print(f"Hobbies: {n["Hobbies"]}")
            break
    else:
        print("Pessoa não encontrada...")

