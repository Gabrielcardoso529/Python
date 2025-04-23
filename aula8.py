#estrutura de repetição "for":

# serve para sabermos quantas vezes vamos ter que entrar no laço de repetição
# Função é um conjunto de instruções que estão em algum lugar, e funciona chamando ele

# Range:
# A função range pode ser usada de três maneiras:
# - range(stop)
# - range(start, stop)
# - range(start, stop, step)

# range(stop)
#for numero in range(10):
    #print(numero)

# range (start, stop)
#for numero in range(5,10):
    #print(numero)

# range (start, stop, step)
#for numero in range(0,10,2):
    #print(numero)

#cont=0
#while cont < 10:
    #print(cont)
    #cont+=1

cont = 0
#for cont in range(10):
#    num = int(input("Digite um numero inteiro: "))
 #   if num%2 == 0:
  #      cont += 1
#print(f"Voce digitou {cont} de números pares")

#for i in range(10):
#    if i == 5:
#        break
#    print(i)


#usuario = int(input("Digite um valor de 1 a 10: "))
#for i in range (0,10):
 #   if i == usuario:
  #      break
   # print(i)

#for i in range(10):
#    if i % 3 == 0:
#        continue
#    print(i)


#cont = 0
#texto= "Esse é um texto exemplo"

#for caractere in texto:
#    cont +=1
#print(cont)

#Desafio cadastro do aluno

nome = input("Digite o nome do aluno: ")
rm = int(input("Digite o rm do aluno: "))
senha = int(input("Digite a senha do aluno: "))
senhav =  int(input("Digite a senha novamente: "))
while senhav != senha:
    senhav = int(input("Senha não concide, digite novamente: "))


print("--- Aluno cadastrado!---")

print("--- Boletim ---")
rmlog = int (input("Digite o rm do aluno: "))
while rmlog != rm:
    rmlog = int(input("RM não encontrado, digite novamente: "))
senhalog = input("Digite a senha do aluno: ")

cont = 0
if senhalog !=
while cont < 3:
    senhalog = int(input("Digite sua senha: "))
    if senhalog == senha:
        print("Acesso permitido!")
        break
    else:
        cont +=1
        print(f"Senha incorreta. Tentativas restantes: {3 - cont}")
if cont == 3:
    print("Número de tentativas excedido. Sistema travado")


cp1 = float(input("Digite o valor do checkpoint 1: "))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))
cp2 = float(input("Digite o valor do checkpoint 2: "))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))
cp3 = float(input("Digite o valor do checkpoint 3: "))
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))

cps = 0
if cp1 < cp2 and cp1 < cp3:
    cps = cp2 + cp3
elif cp2 < cp1 and cp2 < cp3
    cps = cp1 + cp3
else:
    cps = cp1 + cp2

sprint1 = float(input("Digite o valor do sprint1: "))
while sprint1 < 0 or sprint1 > 10:
    sprint1 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))
sprint2 = float(input("Digite o valor do sprint2: "))
while sprint2 < 0 or sprint2 > 10:
    sprint2 = float(input("A nota deve ser entre 0 e 10, digite novamente: "))


print(f"A nota necessária para passar é {6 - resultado}")