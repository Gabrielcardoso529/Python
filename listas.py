vinhos = ['Malbec R$110,00', 'Chandon R$75,00', 'Tinto Argentino R$60,00',
          'Seco Chileno R$83,00', 'Suave Argentino R$70,00']
print(vinhos[0])
print(vinhos[1])
print(vinhos[2])
print(vinhos[3])
print(vinhos[4])


dados = ['Lucas', 20, 1.68, 'Gabriel', 18, 1.80]

for i in range(0,2,3,):
     print(dados[i])


nomes = ['Paulo', 'Ana', 'Pedro', 'Maria']

for i in range(-1,-5,-1):
    print(nomes[i])


#A função len() é utilizada para obter o tamanho de uma lista

nomes = ['Paulo', 'Ana', 'Pedro', 'Maria']
n = len(nomes)
print(f'A lista possui {n} itens')


nomes = ['Paulo', 'Ana', 'Pedro', 'Maria']
for item in nomes:        # A cada repetição acessa um item
    print(item)
nomes.append('Gabriel')
print(nomes)


numeros = []
for i in range(5):             #Preencher lista com 5 itens
    n = int(input('Informe um número: '))
    numeros.append(n)          #Insere número a cada lista
print(numeros)

numeros = [2, 0, 4, 18, 13]

soma = 0
for num in numeros:
    soma += num
b= len(numeros)
print(f"o somatório desta lista é {soma} e a média é igual a {soma/b}")

#Deixa a lista em ordem crescente
numeros.sort()
print(numeros)

#Deixa a lista em ordem decrescente
numeros.sort(reverse=True)
print(numeros)

print(min(numeros))   #Retorna o menor número
print(max(numeros))   #Retorna o maior número

print(sum(numeros))   #Faz o somatório completo da lista



