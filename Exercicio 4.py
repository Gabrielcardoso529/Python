
X = int(input("digite um numero inteiro de 0 a 1000: "))
if (X>0 and X<1000):
    B = X
    C = X//100
    X = X-C*100
    D = X//10
    X = X-D*10
    print(C+D+X)
else:
    print("numero invalido,")