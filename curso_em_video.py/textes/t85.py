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
while True:
    if troco >= ced:
        troco -= ced
        nunced += 1
    else:
        if nunced > 0:
            print(f"O clinte receberá {nunced} cédula de {ced} para o seu troco")      
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            nunced = 0
        if troco == 0:
            break