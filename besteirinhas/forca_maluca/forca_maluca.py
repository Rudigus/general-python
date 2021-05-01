import random

def main():
    arquivo = open("palavras.txt", "r")
    texto = arquivo.read()
    palavras = texto.split()
    indiceTema = random.randint(1,5) * 2 - 1
    temaEscolhido = palavras[indiceTema]
    palavraEscolhida = palavras[indiceTema - 1]
    letrasPalavra = list(palavraEscolhida)
    print(f"O tema é: {temaEscolhido}")
    tp = len(palavraEscolhida)
    letrasAcertadas = []
    for i in range(tp):
        letrasAcertadas.append('_')
        print("_ ", end="")
    jogoContinua = True
    vidas = 5
    acertouLetra = False
    while(jogoContinua):
        letraUsuario = input("\n\nInforme uma letra: ")
        for i in range(tp):
            if(letraUsuario.lower() == letrasPalavra[i].lower()):
                acertouLetra = True
                letrasAcertadas[i] = letrasPalavra[i]
            print(f"{letrasAcertadas[i]} ", end="")
        if(letrasAcertadas == letrasPalavra):
            jogoContinua = False
            print("\n\nVocê venceu!!!")
        if(not acertouLetra):
            vidas -= 1
        if(vidas == 0):
            print(f"\n\nQue pena, você perdeu... A palavra correta era: {palavraEscolhida}")
            jogoContinua = False
        acertouLetra = False
main()
