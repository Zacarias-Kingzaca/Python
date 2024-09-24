from os import system
system ('cls')

Telefonis = ['Iphone XR','Sansung S20','Tecno Spark 10C','Sunmax Modelo 6 Pro','Itel S18']

Computadores = ['HP','DELL','ACER','Tochiba','Sansung']

print(20*'=')
print('   LOJA DE ELETRICOS')
print(20*'=')
print('')

print('1- Telefonis')
print('2- Computadores')
print('')

op = int(input('»»»»» '))

if op == 1:
    print(20*'-')
    for telefonis in Telefonis:
        print(telefonis)
        print ('')

elif op == 2:
        print(20*'-')
        for computadores in Computadores:
            print(computadores)
            
else:
    print('Escolha invalida')

    print('Obrigado e volte sempre')