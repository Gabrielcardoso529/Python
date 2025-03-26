numero = int(input("digite um numero inteiro: "))

if (numero%2) == 0 :
    print(f"o numero {numero} é PAR!")
else:
    print(f"o numero {numero} é IMPAR!")

media = float(input("digite sua media: "))
faltas = int(input("digite a quantidade de faltas: "))
if (media >= 6.0 and faltas < 16):
    print(f"voce esta aprovado")
else:
    print("reprovado")


notas= float(input("media final do aluno: "))
faltas= int(input("numero de faltas: "))
if(media >=6 ) :
    if (faltas <=15) :
        print(f"voce esta aprovado")
    else:
        print("reprovado")
else:
    print("reprovado")




Indeferido = "Nao pode emprestimo"
Deferido = "pode emprestimo"


negativado = input("esta com o nome negativado? ")
if(negativado == "não"):
    carteira_ass = input("trabalha com carteira assinada? ")
    if(carteira_ass == "sim"):
        imovel = input("possui imovel? ")
        if(imovel == "sim"):
            print(Deferido)
        else:
            print(Indeferido)
    else:
        print(Indeferido)
else:
    print(Indeferido)