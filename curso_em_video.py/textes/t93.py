from os import system
system ("cls")
print()

valor_compra = float(input("Valor de compra: "))
valor_pago = float(input("Valor pago: "))
troco = valor_pago - valor_compra

if troco <= 0:
    print("Valor pago é suficiente.")
else:
    print(f"Troco total:{troco:.2f}")
    troco_em_kzs = int(troco)
    cedulas = [100, 50 , 20, 10, 1]
    for cedula in cedulas:
        quantidade = troco_em_kzs // cedulas 
        troco_em_kzs = troco_em_kzs
        if quantidade > 0:
            print(f"Cédulas de {cedulas}: {quantidade}")