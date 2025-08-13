#matriz = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12]]

#print(matriz)

#linhas = int(input('Quantidade de linhas: '))
#colunas = int(input('Quantidade de Colunas: '))

#matriz = []
#for i in range(linhas):
 #   linha = []
  #  for j in range(colunas):
   #     n = int(input('Números: '))
    #    linha.append(n)
    #matriz.append(linha)
#print(matriz)

#matriz = [[1, 2, 3],
#          [4, 5, 6]]

#for linha in matriz:
 #   for item in linha:
  #      print(item)


#matriz = [[1, 2, 3],
#          [4, 5, 6]]

#for linha in range(len(matriz)):
 #   for coluna in range (len(matriz[0])):
  #      print(matriz[linha][coluna])



# exercicios Python
#linhas = 3
#colunas = 5

#matriz = []
#for i in range(linhas):
 #   linha = []
  #  for j in range(colunas):
   #     n = int(input('Números: '))
    #    linha.append(n)
    #matriz.append(linha)
#print(matriz)


#execicio 2 python
#for linha in range(len(matriz)):
 #   for coluna in range (len(matriz[0])):
  #      if (matriz[linha][coluna] >= 100):
  #          matriz[linha][coluna] = 0
#print(matriz)

#exercicio 3 e 4 python
linhas = 5
colunas = 5

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input('Digite números inteiros: '))
        linha.append(n)
    matriz.append(linha)
print(matriz)
soma = 0
for i in range (len(matriz)):
    soma += matriz[i][i]
print(f"O  valor da somátoria diagonal é igual a {soma} ")

menor = matriz [0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(f'Menor número encontrado: {menor}')