arq = open("maneiro.txt", "r")
conteudo = arq.read()
for i in conteudo:
    print(i, sep="", end="")
arq.close()

arq2 = open("maneirasso.txt", "w+")
arq2.write("Gororoba azul")
arq2.seek(0)
conteudo2 = arq2.read()
print("")
for i in conteudo2:
    print(i, sep="", end="")
arq2.close()

