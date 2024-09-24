from os import system
system("cls")
print("")

tupla = (0, 1, 3, 3, 5, 7, 7, 7)

print("Conteúdo da tupla: ", tupla)


qtde_elem = len(tupla)
print("Quantidade de elementos na tupla: ", qtde_elem)

qtde_elem = tupla.count(7)
print("Quantidade de elmentos igual a 7 na posição: ",qtde_elem)

qtde_elem_4 = tupla[4]

print("Elemento da posição 4 (quinta pos.): ", qtde_elem_4)