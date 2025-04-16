
X = 0
Par = 0

while X <= 10:
    numero = int(input("informe um número inteiro: "))
    if numero % 2 == 0:
        Par += 1
    X+=1
print(f"Voçê digitou {Par} números pares")


media = float(input("Digite sua média: "))

while media < 0 or media > 10:
    print("nota inválida, digite novamente: ")
    media = float(input("Digite sua média: "))
if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Você esta de exame")
else:
    print("reprovado")
print(f"Sua media foi igual a: {media}")

#Desafio 1

cont = 1
tab = int(input("digite um numero para realizar a tabuada: "))

while cont <= 10:
    print(f"{tab} X {cont} = {tab*cont}")
    cont += 1


#Desafio 2

nome = input("Digite um nome: ")

while nome != "Diogo":
    print("Hoje não é seu aniversario Otário:\n")
    nome = input("Insira seu nome: ")
print("parabens Diogo, hoje é seu aniversário!")














