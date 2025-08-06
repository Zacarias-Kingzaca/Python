from os import system
system("cls")
print()

def produtos(*produto, msg="Olá organizador!"):
    produto = list(set(produto))
    produto = [p.capitalize() for p in produto]

    inicias = {}
    for prod in produto:
        inicial = prod[0]
        inicias[inicial] = inicias.get(inicial, 0) + 1
    
    print(msg)
    print("\nLista de Produtos:")
    for p in sorted(produto):
        print(f"- {p}")
    print("\nQuantidade de produto por letra inicial:")
    for letra, qtd in sorted(inicias.items()):
        print(f"{letra}: {qtd} produto(s)")
  
produtos("carro", "cadeira", "banco","cadeira", "roupa", "banco", "mesa", "arca","carro","tv","fogão")
