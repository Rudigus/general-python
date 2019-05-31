import random

# Exercicio feito por Rudigus e Magnus

numeroVezes = int(input("Informe o número de vezes que o dado será rolado: "))
for i in range(numeroVezes):
    numeroVicio = random.randint(1,100)
    if(numeroVicio < 6):
        numeroDado = 1
    elif(numeroVicio < 26):
        numeroDado = 2
    elif(numeroVicio < 50):
        numeroDado = 3
    elif(numeroVicio < 80):
        numeroDado = 4
    elif(numeroVicio < 100):
        numeroDado = 5
    else:
        numeroDado = 6
    print(numeroDado)











            
