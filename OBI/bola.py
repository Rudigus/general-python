# Rudigus - OBI 2018 - Programação Nível Senior - Fase 3 - Bolas

def sequenciaPossivel(bolas):
    for i in range(len(bolas) - 1):
        cont = 1
        for j in range(i + 1, len(bolas)):
            if(bolas[j] == bolas[i]):
                cont = cont + 1
            if(cont >= 5):
                return False
    return True

bolas = [int(x) for x in input().split()]
if sequenciaPossivel(bolas):
    print("S")
else:
    print("N")
