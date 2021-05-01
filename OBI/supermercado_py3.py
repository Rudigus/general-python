# Rudigus - OBI 2019 - Programação Nível Senior - Fase 2 - Supermercado

numeroSupermercados = int(input())
precosCarne = []
menorPreco = -1
for i in range(numeroSupermercados):
    precoCarne = [float(i) for i in input().split()]
    precosCarne.append(precoCarne)
for i in precosCarne:
    precoGrama = i[0] / i[1]
    if(menorPreco == -1):
        menorPreco = precoGrama
    elif(precoGrama < menorPreco):
        menorPreco = precoGrama
menorPrecoTotal = format(menorPreco * 1000, ".2f")
print(menorPrecoTotal)
