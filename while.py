#exemplo de While, cont é como se fosse um marcador inicial, sendo uma variavel#
X = int(input("Adicione um valor: "))
cont = 0
while cont < X:
    print("Olá")
    cont +=1   # sem esse "cont" seria um loop infinito, então ele e necesário no código#
print("Fim")

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


#Desafio 3

print("Cachorro-quente | 100 | R$13,20")
print("Hambúrguer | 101 | R$19,90")
print("Chesseburguer | 102 | R$21,90")
print("Suco Natural | 103 | R$7,00")
print("Refrigerante | 104 | R$6,50")

resp = "sim"
total = 0

while resp == "sim":
    cod = int(input("informe o código do seu pedido: "))

    match cod:
        case 100:
            quant = int(input("Informe a quantidade: "))
            valor = quant*13.2
        case 101:
            quant = int(input("Informe a quantidade: "))
            valor = quant * 19.9
        case 102:
            quant = int(input("Informe a quantidade: "))
            valor = quant * 21.9
        case 103:
            quant = int(input("Informe a quantidade: "))
            valor = quant * 7
        case 104:
            quant = int(input("Informe a quantidade: "))
            valor = quant * 6.5
        case _:
            print(f"Código inválido!")
            continue


    total += valor

    resp = input("Deseja continuar seu pedido (sim ou não): ")

print(f"o valor total do seu pedido é R${total:.2f}")
