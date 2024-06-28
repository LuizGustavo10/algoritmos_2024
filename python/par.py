#verificando se um número é par
numero = int(input("Insira um número"))
resto = numero % 2
print('Esse é o resto ',resto)

if resto == 0:
    print("É um número par")
else:
    print("É um número impar")