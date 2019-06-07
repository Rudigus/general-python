def fatorial(numero):
    if(numero == 1):
        return 1
    return numero * fatorial(numero - 1)

def main():
    opcao = True
    while(opcao):
        questao = int(input("Informe o número da questão (1, 2, 3 ou 4): "))
        if(questao == 1):
            questao1()
        elif(questao == 2):
            questao2()
        elif(questao == 3):
            questao3()
        elif(questao == 4):
            questao4()
        escolha = int(input("\nPara encerrar o programa, digite 1. Caso digite qualquer outra coisa, você poderá ver outras "
                        "questões ou ver a mesma questão novamente: "))
        if(escolha == 1):
            opcao = False
            
def questao1():
    print("\n1) Aplique V para as afirmações verdadeiras e F para as afirmações falsas. Justifique caso o item seja falso.")
    print("""
    \na) Os laços de repetição no Python tem a mesma escrita que na linguagem C - Falso. Apesar da estrutura de repetição 
    'while()' do Python e do C serem semelhantes, pois necessitam do mesmo parâmetro, que é um valor ou variável booleana, 
    O Python não possui a estrutura 'do... while()', enquanto o C tem. Além disso, a estrutura de repetição 'for()' do 
    Python e do C são bem diferentes. Uma dessas diferenças é a condição de iteração: O C utiliza comparações antes de 
    cada iteração para garantir que elas são válidas, enquanto o Python recebe uma sequência de números para o 
    funcionamento da sua iteração. Para obter um comportamento similar ao C, você precisa utilizar a função 'range()' 
    no Python. Além disso, a estrutura de repetição 'for()' do Python tem uma função muito útil: utilizar objetos 
    iteráveis, como listas e strings, e percorrer cada um de suas 'unidades', como os elementos das listas ou os caracteres 
    das strings.
          """)
    print("""
    \nb) No Python a indentação não é importante - Falso. Na verdade, podemos dizer que o Python é, provavelmente, a 
    linguagem que mais depende da indentação, pois, nessa linguagem, a indentação não é só um recurso organizacional, 
    e sim o que define o escopo das linhas de código. Ou seja, a indentação no Python é o que possibilita o funcionamento 
    do código.
          """)
    print("""
    \nc) Na linguagem C a indentação não é importante - Falso. Apesar da linguagem C não depender da indentação para o
    funcionamento do código, a indentação é um recurso muito útil para a legibilidade do código. Isso faz com que o código
    seja mais fácil de entender e de modificar. É extremamente recomendado, independentemente da linguagem.
          """)
    print("""
    \nd) No Python é impossivel abrir um arquivo para leitura e ler caractere por caractere - Falso. Uma das maneiras de fazer
    isso é utilizando um recurso fantástico do Python: os objetos iteráveis. Você pode iterar cada linha do arquivo, e, para
    cada linha, pode iterar os caracteres dessa linha. Só que essa maneira tem um revés - você não terá controle sobre um
    caractere em específico, e sim no conjunto deles. Outra maneira de fazer isso, para que também tenha o controle sobre qual
    caractere selecionar, é utilizar o 'nomeArquivo.read(1)', em que 'nomeArquivo' é o nome do arquivo em questão. Ele irá
    ler o proximo caractere de acordo com a stream. Para pegar o caractere que você quiser, basta você manipular a stream,
    com o método 'nomeArquivo.seek()', por exemplo.
          """)
    print("""
    \ne) No Python é sempre necessario criar pelo menos uma função para cada programa, nem que seja o main - Falso. Caso só
    seja necessária uma função no seu código, você pode simplesmente escrever o código sem definir função nenhuma, e esse
    código será tratado e executado como se estivesse na função 'main()' e será chamado automaticamente.
          """)
          
def questao2():
    escolha = int(input("Informe se deseja converter de binário para decimal (1) ou de decimal para binário (2): "))
    if(escolha == 1):
        numeroDec = int(input("Informe o número na base binária: "), 2)
        print(numeroDec)
    if(escolha == 2):
        numero = int(input("Informe o número na base decimal: "))
        numeroBin = bin(numero)
        print(numeroBin)
                
def questao3():
    palavra = input("Informe uma palavra: ")
    letras = list(palavra.lower())
    numeroVogais = 0
    for letra in letras:
        if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or
           letra == "á" or letra == "é" or letra == "í" or letra == "ó" or letra == "ú" or
           letra == "â" or letra == "ê" or letra == "ô" or
           letra == "ã" or letra == "õ" or
           letra == "à"):
            numeroVogais += 1
    print(f"A quantidade de vogais na palavra informada é {numeroVogais}")
    
def questao4():
    arquivo = open("arquivoMaluco.txt", "r")
    numero = int(arquivo.read())
    print(f"O fatorial de {numero} é {fatorial(numero)}")
    arquivo.close()
    

main()

    
