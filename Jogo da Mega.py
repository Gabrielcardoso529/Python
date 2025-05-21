import random

def dados_usuario():
    dezena = []
    print('Digite 6 numeros entre 1 a 60 (sem repetição): ')
    while len(dezena) < 6:
        try:
            num = int(input(f'Dezena{len(dezena)+1}:'))
            if num < 1 or num > 60:
                print("Numero fora do permitido.")
            elif num in dezena:
                print("Numero repetido. Digite outro: ")
            else:
                dezena.append(num)
        except ValueError:
            print("Entrada inválida, Digite apenas numeros.")
    return dezena

#Função para sortear 6 dezenas aleatórias

def sortear_dezenas():
    return random.sample(range(1, 61), 6)

#Função para comparar e mostras os acertos

def verificar_acertos(escolhidas, sorteadas):
    acertos = set(escolhidas) & set(sorteadas)
    print("\nResultado")
    print(f"Suas dezenas: {sorted(escolhidas)}")
    print(f"Numeros acertados: {sorted(acertos)}")
    print(f"Numeros sorteados: {sorted(sorteadas)}")
    print(f"Total de acertos: {sorted(acertos)}")

#Codigo principal

def jogar_mega():
    usuarios_dezenas = dados_usuario()
    dezenas_sorteadas = sortear_dezenas()
    verificar_acertos(usuarios_dezenas,dezenas_sorteadas)

#rodar programa
jogar_mega()
