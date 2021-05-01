import random

#Exercicio feito por Rudigus e Magnus

linhas = int(input("Informe o número de linhas: "))
colunas = int(input("Informe o número de colunas: "))
matriz = []
aux = []
for i in range(linhas):
    for j in range(colunas):
        aux.append(random.randint(1,9))
    matriz.append(aux)
    print(aux)
    aux = []
posicao = []
l, c = map(int, input("Informe a posição (linha e coluna respectivamente): ").split())
operacao = input("Informe a operação ('media', 'zerar', 'zerarDiag'): ")
media = 0
quantVizinhos = 0
if(operacao == "media"):
    for i in range(l - 1, l + 2):
        for j in range(c - 1, c + 2):
            if((i < 0) or (j < 0)):
                continue
            if((i  == linhas) or (j == colunas)):
                continue
            if((i == l) and (j == c)):
                continue
            if((i == linhas) and (j == colunas)):
                break
            media += matriz[i][j]
            quantVizinhos += 1
    media /= quantVizinhos
    print(media)
elif(operacao == "zerar" or operacao == "zerarDiag"):
    matriz[l][c] = 0
    if(operacao == "zerarDiag"):
        if(l - 1 >= 0 or c - 1 >= 0):
            matriz[l - 1][c - 1] = 0
        if(l + 1 < linhas or c + 1 < linhas):
            matriz[l + 1][c + 1] = 0
    for i in range(linhas):
        print(matriz[i])


        




















            
