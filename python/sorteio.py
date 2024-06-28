#Algoritmo para sortear um número
import random

def sortear(minimo, maximo):
    return random.randint(minimo, maximo)

minimo = 1
maximo = 10

sorteado = sortear(minimo, maximo)

num = int(input("Insira qualquer número: "))

while True:

    if num > 10 or num < 0:
        print("O número tem que ser entre 1 e 10")
        num = int(input("Insira qualquer número: "))
    elif sorteado < num:
        print("O número sorteado é menor")
        num = int(input("Insira qualquer número: "))

    elif sorteado > num:
        print("O número sorteado é maior")
        num = int(input("Insira qualquer número: "))

    elif sorteado == num:
        print("Acertou! parabéns")
        break
            
    else:
        print("O número tem que ser entre 1 e 10")
        num = int(input("Insira qualquer número: "))


