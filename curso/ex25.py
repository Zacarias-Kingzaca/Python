from os import system
system("cls")
print("")


import json 
import os 
def carregar_clientes(arquivo):
    if os.pat.exists(arquivo): 
     with open(arquivo,'r')as f:
        return json.load(f)
    return 
def  salvar_cliente(arquivo,clientes):
    with open(arquivo,'w')as f:
     json.dump(clientes,f,indent=4)

def cadastrar_cliente(clientes):
   nome =input("Digita o nome do cliente: ")
   telefoni =input("Digita o telefoni do cliente: ")
   email =input("Digita o E-mail do cliente: ")
   morada =input("Digita a morada do cliente: ")

   cliente = {
    
     "nome" : nome,
     "telefoni" : telefoni,
     "E-mail" : email,
     "morada" : morada   

   }
   
   clientes.append(cliente)
   print("Cliente cadastrado com sucesso!")
def buscar_cliente(clientes):
      nome = input("Digita o nome do cliente que desjas buscar: ")
      for cliente in clientes:
         if cliente['nome'].lower() == nome.lower():
             print("cliente")
             return
         print("Cliente não encontrado.")

def alterar_cliente(cliente):
      nome = input("Digita o nome do cliente que desejas alter: ")
      for cliente in cliente:
         if cliente['nome'].lower() == nome.lower():
             telefoni = input("Digita o novo telefoni (ou preciona Enter para manter): ")
             email = input("Digita o novo E-mail (ou preciona Enter para manter): ") 
             morada = input("Digita a novo morada (ou preciona Enter par manter): ") 
         if telefoni:
                cliente['telefoni'] = telefoni
         if email:
               cliente['email'] = email
         if morada:
                cliente['morada'] = morada

         print("Dados do cliente atualizado com sucesso!")
             
      return
print("Cliente não encontrado.")
def apagar_cliente(clientes):
  nome=input("Digita o nome do cliente que deseja apagar: ")
  for i, cliente in enumerate(clientes):
     if cliente['nome'].lower() == nome.lower():
        del cliente[i]
        print("Cliente apagado com sucesso!")
        return
print("Cliente não encontrado.")
def mostrar_clientes(clientes):
    if not clientes:
      print("Nenhum cliente encontrado.")
      return
    for i, cliente in enumerate(clientes,start=1):
       print(f"Nome{cliente['nome']}, Telefoni:{cliente['telefoni']},E-mail{cliente['email']}, Morada {cliente['morada']}")
def main(): 
   arquivo = 'clientes.json'  
   clientes = carregar_clientes(arquivo)
   while True:
      print("\n1. Cadastrar cliente")
      print("2. Buscar cliente")
      print("3. Alterar cliente")
      print("4. Apagar cliente")
      print("5. Mostrar todos os clientes")
      print("6. Sair")

      opcao = input("Escolha uma opção: ")

      if opcao == '1':
         cadastrar_cliente(clientes) 
      elif opcao == '2':
         buscar_cliente(clientes)
      elif opcao == '3':
         alterar_cliente(clientes)
      elif opcao == '4':
         buscar_cliente(clientes)
      elif opcao == '5':
         mostrar_clientes(clientes)
      elif opcao == '6':
         break
      else: 
         print("Opção inválida.Tente novamente.")
      if "__name__":
       main()