from os import system
system ("cls")
print("")

variavel_numerica = 5

print("Variável numérica (antes da alteração): ")
print("conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))
 
variavel_numerica = 10 

print("Variável numérica (depois da alteração): ")
print("conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))
 

l_mutavel = [1, 2, 3, 4]

print("Lista mutavel: ")
print("conteúdo:", l_mutavel)
print("ID:", id(l_mutavel))

l_mutavel.append(40)
l_mutavel [0] = 0

print("Lista mutavel: ")
print("conteúdo:", l_mutavel)
print("ID:", id(l_mutavel))
