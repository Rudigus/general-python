vetor = []
matriz = []
lista = []
limite = int(input("Informe o número de elementos do vetor / matriz: "))
for i in range(1, limite + 1):
    vetor.append(i)
print(vetor)
for i in range(1, limite + 1):
    for j in range(1, 4):
        lista.append((i - 1) * 3 + j)
    matriz.append(lista.copy())
    lista.clear()
for i in range(0, len(matriz)):
    print(matriz[i])
