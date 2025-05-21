#Jogo de dados
import random

def dados_usuario():
    n = []
    print("Digite um numero maior que 02 e menor que 12:")
    while True:
        try:
            num = int(input(f"Numero:"))
            if num < 2 or num >12:
                print("Numero fora do permitido")
            else:
                return num
        except ValueError:
            print("Entrada Invalida, digite apenas numeros.")


#Jogo de dados
import random

def dados_usuario():
    n = []
    print("Digite um numero maior que 02 e menor que 12:")
    while True:
        try:
            num = int(input(f"Numero:"))
            if num < 2 or num >12:
                print("Numero fora do permitido")
            else:
                return num
        except ValueError:
            print("Entrada Invalida, digite apenas numeros.")


#Função para sortear 2 numeros
def sortear_dados():
    dado1= random.randint (1,6)
    dado2 = random.randint(1, 6)
    soma = dado1+dado2
    return soma



#função para mostrar a probailidade
def mostrar_probabilidade(num):
    match num:
        case 2 | 12:
            print("Probabilidade baixa: 1/36")
        case 3 | 11:
            print("Probabilidade baixa: 2/36 ")
        case 4 | 10:
            print("Probabilidade média-baixa:3/36 ")
        case 5 | 9:
            print("Probabilidade alta: 4/36 ")
        case 6| 8 :
              print("Probabilidade média-alta: 3/36 ")
        case 7:
              print("Maior probabilidade: 6/36")

#Programa principal
num_usurario = dados_usuario()
mostrar_probabilidade(num_usurario)

#primeira comparação
soma = sortear_dados()


print(f"Dados sorteados: {soma} ")
if soma == num_usurario:
    print("Parabens, voce acerto!!")
else:
    print("Não foi dessa vez")


#Dicionario
frequencias = {soma: 0 for soma in range (2,13)}

#Sortear os dados 1000 vezes
for _ in range(1000):
    resultado = sortear_dados() # novo valor a cada vez
    frequencias[resultado] += 1

#Exibir resultados
print("frequencia das somas  após 1000 sorteios:")
for soma, freq in sorted(frequencias.items()):
    print(f"Soma {soma}: {freq} vezes ({freq / 10:.1f}%)")
