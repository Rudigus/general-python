def adicao(n1, n2):
    s = n1 + n2
    return s

def fatorial(n):
    if(n == 1):
        return 1
    return n * fatorial(n-1)

def fibonacci(l):
    a = 1
    b = 1
    c = 0
    for i in range(0, l):
        if(i == l - 1):
            print(b, ".", sep="", end="")
        else:
            print(b, ", ", sep="", end="")
        a = c
        c = b
        b += a

def main():
    escolha = int(input("Informe a operação desejada (1 - Adição, 2 - Fatorial, 3 - Fibonacci): "))
    if(escolha == 1):
        na1 = int(input("Informe o primeiro número: "))
        na2 = int(input("Informe o segundo número: "))
        s = adicao(na1, na2)
        print(f"A soma entre {na1} e {na2} é {s}")
    elif(escolha == 2):
        nf = int(input("Informe um número: "))
        f = fatorial(nf)
        print(f"O fatorial de {nf} é {f}")
    elif(escolha == 3):
        l = int(input("Informe a quantidade de números da sequência de Fibonacci que serão mostrados: "))
        fibonacci(l)
    else:
        print("Opção inválida. Que pena :/")

main()

# def fatorial(n):
 #   for i in range(n - 1, 0, -1):
  #      n *= i
   # return n
