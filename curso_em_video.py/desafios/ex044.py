from os import system
system ("cls")
print()

print("================== LOJAS ZACARIAS ==================")
preco = float(input("Preço das compras: kzs "))

print("""FORMA DE PAGAMENTO

      [ 1 ]á vista dinheiro/cheque
      [ 2 ]á vista cartão 
      [ 3 ]2x no cartão
      [ 4 ]3x ou mais no cartão""")
print()
op = int(input("Qual é a opção? "))

if op == 1:
    total = preco - (preco * 10 / 100)
elif op == 2:
    total = preco - (preco * 5 / 100)
elif op == 3:
    total = preco
    parcela = total / 2
    print("Sua compraz será parcelada em 2x de kzs{:.2f} SEM JUROS".format(parcela))
elif op == 4:
    total = preco + (preco * 20 / 100)
    totalp = int(input("Quantas parcelas? "))
    parcela = total / totalp
    print("Sua compra será parcelada de {}x de kzs{:.2f} COM JUROS".format(totalp, parcela))
else:
  total = 0
  print("\033[1;31m Opcão iválida, tente novamente. \033[m")
print("Sua compra de kzs{:.2f} vai custar kzs{:.2F} no final.".format(preco, total))