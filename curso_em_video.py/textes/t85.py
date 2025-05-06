from os import system
system("cls")
print()

print("="*50)
print("{:^50}".format("CAIXA COM TROCO"))
print("="*50)
nunced = 0
ced = 50
valordecompra = float(input("Qual foi o valor de compra? kzs "))
valorpago = float (input("Qual foi o valor pago? kzs "))
troco = valorpago - valordecompra 
print(f"\ntroco total: kzs{troco:.2f}")

ced_50 = troco // 50
troco = troco
ced_20 = troco // 20
troco = troco
ced_10 = troco // 10
troco = troco
ced_1 = troco // 1
troco = troco

print(f"cédulas de kzs50:{ced_50}")
print(f"cédulas de kzs20:{ced_20}")
print(f"cédulas de kzs10: {ced_10}")
print(f"cédulas de kzs1: {ced_1}")