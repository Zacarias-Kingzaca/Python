from os import system
system ("cls")
print() 

print(50*"*")
print("Trabalhando com Matriz em python")
print(50*"*")

matriz =  [

            [1 ,2 , 3],
            [4, 5, 6]
            
            ]

print(matriz)

elemento = matriz[0][1]
print()
print(elemento)
print()
matriz.append([7,8])
print()

for linha in matriz:
    linha.append(0)

print("OPERÇÃO COM MATRIZES")

def soma_matriz (matriz1,matriz2) :
    resultado = []
    for i in range(len(matriz1)):
        linha = []
    for j in range(len(matriz1 [0])):
          linha.append(matriz1[i] [j] + matriz2[i] [j])
          linha.append(linha)
          return resultado

matriz_a = [[1, 2, 3,],[4,5,6]]
matriz_b =[[7,8,9,],[10,11,12]]
soma_matrizes = soma_matriz(matriz_a,matriz_b)
print(soma_matrizes)


  
print(50*"*")
print("Finish")
print(50*"*")