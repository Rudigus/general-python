import random, sys

listaAleatoria = []
conta = []
nomes = ["Rodrigo", "Luan", "Matheus", "Caio", "Magno", "Gilberto", "Marco", "Lucas", "Ellen", "Lizandra"]
telefones = ["(85)90000-0000", "(85)91111-1111", "(85)92222-2222", "(85)93333-3333", "(85)94444-4444",
            "(85)95555-5555", "(85)96666-6666", "(85)97777-7777", "(85)98888-8888", "(85)99999-9999"]
for i in range(2):
    listaAleatoria.append(int(random.randint(0, 9)))
listaAleatoria.append(int(random.randint(900, 25000)))
listaAleatoria.append(int(random.randint(15, 77)))
listaAleatoria.append(int(random.randint(0, 9)))
for i in range(10):
    if(listaAleatoria[0] == i):
        conta.append(nomes[i])
    if(listaAleatoria[1] == i):
        conta.append(telefones[i])
conta.append(listaAleatoria[2])
conta.append(listaAleatoria[3])
if(listaAleatoria[4] < 7):
    conta.append("Corrente")
else:
    conta.append("Poupança")
print(conta)
if(conta[3] >= 72 or conta[4] != "Corrente"):
    print("O empréstimo do Banco Milagre não é fornecido ao seu perfil de cliente.")
    sys.exit()
emprestimo = conta[2] * 5
if(emprestimo > 30000):
    emprestimo = 30000
valido = False
while(!valido):
    montante = emprestimo * pow(1.07, 3)
    numeroParcelas = (montante // 900) + 1
    if(numeroParcelas > 36):
        


        
        
