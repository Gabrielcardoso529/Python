x = 10
y = 5


print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

idade = int(input('informe sua idade:'))
print(f'maior de idade: {idade>=18}')

x = 5
y = 10

print(x < 10 and y > 5)
print(x > 10 and y < 5)
print(x < 10 or y > 5)
print(x > 10 or y < 5)
print(not x < 10)
print(not x > 10)


idade = int(input("informe sua idade:"))
print(f"pode doar sangue: {not(idade  >= 16) and (idade <= 69)}")




