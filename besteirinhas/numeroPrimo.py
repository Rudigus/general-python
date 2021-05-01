from math import sqrt

executar = True
while(executar):
    numeroTestes = 0
    n = int(input("Informe um número: "))
    primo = True
    for i in range(2, int(sqrt(n)) + 1):
        numeroTestes += 1
        if(n % i == 0):
            primo = False
            divisor = i
            break
    if(primo):
        print(f"O número {n} é primo.\nNúmero de testes: {numeroTestes}")
    else:
        print(f"O número {n} não é primo.\nNúmero de testes: {numeroTestes}. Divisor: {divisor}")
    
    comando = input("Para sair, digite \"1\": ")
    if(comando == "1"):
        executar = False
