nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota:"))

notaFinal = (nota1 + nota2 + nota3 + nota4) / 4

print(" A nota final é: ", notaFinal)
print(f"A nota final é {notaFinal}")
print("A nota final é {}".format(notaFinal))

if notaFinal < 60:
    print("O aluno está reprovado!")
elif notaFinal < 70:
    print("O resultado foi bom")
elif notaFinal < 80:
    print("O resultado foi ótimo")
else:
    print("Resultado Excelente! parabens!")

    




#fazer parte de análise de nota