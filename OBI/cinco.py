# Rudigus - OBI 2018 - Programação Nível Senior - Fase 3 - Cinco

def maiorNumeroCinco(digitos):
    maiorNumero = -1
    for i in range(len(digitos) - 1):
        if(digitos[i] % 5 == 0):
            digitosAtuais = list(digitos)
            aux = digitosAtuais[ND - 1]
            digitosAtuais[ND - 1] = digitosAtuais[i]
            digitosAtuais[i] = aux
            numeroAtual = int(''.join(str(v) for v in digitosAtuais))
            if(numeroAtual > maiorNumero):
                maiorNumero = numeroAtual
    return maiorNumero
            

ND = int(input())
digitos = [int(x) for x in input().split()]
maiorNumero = maiorNumeroCinco(digitos)
if(maiorNumero != -1):
    maioresDigitos = " ".join(str(maiorNumero))
    print(maioresDigitos)
else:
    print("-1")

