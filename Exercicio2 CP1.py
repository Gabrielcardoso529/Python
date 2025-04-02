"""Gabriel Cardoso 562103"""


Altura = float(input("Qual a altura da parede? "))
Largura = float(input("E largura? "))
Comprimento = float(input("Qual o comprimento? "))
quantidade = float(input("Quantas paredes tem contando com o teto? "))

A = Altura
B = Largura
C = Comprimento
D = quantidade


Area = (A*B*C) * D /3

print(f"área irá precisar de {Area:.2f} Litros de tinta: ")
