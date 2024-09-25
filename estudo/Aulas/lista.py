from os import system
system('cls')
print('')

print(50*"=")
print("Trabalhando com Lista em python")
print(50*"=")

lista = [1,2,3,4]
print(lista)

print(20*"+")
print("Adicionando um elemento na lista")
lista.append(1.5)
print(lista)
print(20*"+")

print()

print(20*"+")
print("Removendo elemento da lista")
lista.remove(1.5)
print(lista)
print(20*"+")

print()
print(20*"+")
print("Adicionando um elemento na lista em uma posição especifica")
lista.insert(1,1.5)
print(lista)
print(20*"+")

print()

print("recorrendo dentrdo da lista com o *for*")

for elemento in lista:
    print(elemento)

print()

print("Vendo o comprimento da lista com o *len* ")

print(len(lista))

print()

print("Ordenando lista com o comando *Sort*")

lista  =  [20,30,40,10,11]

lista.sort()


print(lista)

print()

print("Fatiamento de Lista com")

fatiada = lista[1:4]

print(fatiada)

print()
