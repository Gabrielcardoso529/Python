nota1 = float(input("Qual sua nota 1:"))
nota2 = float(input("Qual sua nota 2:"))
if(nota1 >=0.0 and nota1 <=10.0):
    if(nota2 >=0.0 and nota2 <=10.0):
        print(f"sua média foi {(nota1+nota2)/2}")
    else:
        print("media invalida")
else:
    print("media invalida")

