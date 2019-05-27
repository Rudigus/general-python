import numpy as np

def main():
    a = int(input("Informe a sua opção (Aleatório = 0, Você escolhe = outro numero): "))
    if(a != 0):
        linhas = int(input("Informe o número de linhas da matriz: "))
        colunas = int(input("Informe o número de colunas da matriz: "))
    else:
        linhas = np.random.randint(1, 6)
        colunas = np.random.randint(1, 6)
    lista = np.floor(16 * np.random.random((linhas, colunas)))
    primeiro = lista[0, 0]
    quantVezes = 0
    media = 0
    for i in range(linhas):
        for j in range(colunas):
            if(lista[i][j] == primeiro):
                quantVezes += 1
            media += lista[i][j] / (linhas * colunas)
    menorDiferenca = lista[0, 0]
    somaPar = 0
    for i in range(linhas):
        for j in range(colunas):
            if(np.abs(lista[i][j] - media) < np.abs(menorDiferenca - media)):
               menorDiferenca = lista[i][j]
            if(lista[i][j] % 2 == 0):
                somaPar += lista[i][j]
    u, c = np.unique(lista, return_counts = True)
    quantRepetido = linhas * colunas - len(u)
    
    print(lista)
    print(f"O maior valor da lista é: {np.amax(lista)}")
    print(f"A soma dos elementos é: {np.sum(lista)}")
    print(f"A quantidade de vezes que o primeiro elemento aparece: {quantVezes}")
    print(f"A média é: {media}")
    print(f"O Valor mais próximo da média é: {menorDiferenca}")
    print(f"A soma dos valores múltiplos de 2 é: {somaPar}")
    print(f"A quantidade de números repetidos é: {quantRepetido}")
    print(f"Lista sem números repetidos: {u}") 
    
    
    
    
main()
