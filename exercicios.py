#exercicio 1

"""def somar(numero1: float, numero2: float) -> float:
    A função realiza a soma de dois números.
    return numero1 + numero2


a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
soma = somar(a, b)
print(f'O resultado da soma é {soma}')


#execicio 2 e 3

def quadrado(numero: float) -> float:
    Retorna o quadrado de um número.
    return numero ** 2

def soma_dos_quadrados(a: float, b: float) -> float:
    Retorna a soma dos quadrados de dois números.
    return quadrado(a) + quadrado(b)

a = float(input("Informe um número: "))
resultado = quadrado(a)
print(f'o numero elevado ao quadrado é {resultado}')

a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))
resultado = soma_dos_quadrados(a,b)
print(f'A soma dos quadrados é igual a {resultado}')"""


#exercicio 4

"""def media(a: float, b: float, c: float) -> float:
    Calcula a média de três números
    return (a + b + c) / 3

a = float(input("Digite a 1ª nota: "))
b = float(input("Digite a 2ª nota: "))
c = float(input("Digite a 3ª nota: "))
m = media (a,b,c)
print(f'A media é igual a {m}')



#exercicio 5

def calcular_salario(salario: float) -> float:
    Calcula e retorna o salário de um funcionário.
    if salario > 2000:
        return salario + salario * 7 / 100
    else:
        return salario + salario * 15 / 100

salario = float(input("Digite o salario recebido: "))
print(f'Salario atualizado: {calcular_salario(salario)}')



#exercicio 6

def soma_divisores(numero: int) -> int:
    Calcula o somatório dos divisores de um número inteiro.
    soma = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            soma += i
    return soma

def soma_divisores_com_lista(numero: int) -> int:
Calcula o somatório dos divisores de um número inteiro.
    lista = []
    for i in range(1, numero+1):
        if numero % i == 0:
            lista.append(i)
    return sum(lista)

n = int(input('Digite um numero inteiro: '))
print(f'Somatorio dos divisores: {soma_divisores(n)}')
print(f'Somatorio dos divisores: {soma_divisores_com_lista(n)}')"""


'''def informações(nome: str, idade: str, cidade: str) -> None:
    """ informaçõe do usuário"""

    print(f'Seu nome é: {n}')
    print(f'Sua idade é: {i}')
    print(f'Sua Cidade é: {c}')

n = input("Nome: ")
i = input("Idade: ")
c = input("Cidade: ")


informações(nome=n, idade=i, cidade=c)'''



def calcular_area_retangulo(base:int=1, altura:int=1) -> int:
    """Calcula e retorna a área de um retângulo"""
    return base * altura

base = int(input("Base: "))
altura = int(input("Altura: "))

area = calcular_area_retangulo(base, altura)
print(f'A area do retângulo é igual a {area}')




def soma(numero1: float, numero2: float) -> float:

    return numero1 + numero2

a = float(input("Digite o 1° numero: "))
b = float(input("Digite o 2° numero: "))


print(f'A soma dos numeros é igual a {soma(a,b)}')