#entrada dos dados
altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))

#processamento de dados
imc = peso / (altura * altura)
imc = peso / (altura ** 2)

#saída
print(imc)

if imc < 15:
    print('Muito magro')
elif imc < 18.5:
    print('Magreza leve')
elif imc < 24.9:
    print('Peso normal')
elif imc < 29.9:
    print('Acima do peso')
elif imc < 39.8:
    print('Obesidade I')
elif imc < 40:
    print('Obesidade II')
else:
    print('Obesidade III')








