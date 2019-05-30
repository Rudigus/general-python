n, c, m = input().split()
x = input().split()
y = input().split()
figurinhasFaltando = len(x)
for i in range(len(y)):
    for j in range(len(x)):
        if(y[i] == x[j]):
            figurinhasFaltando -= 1
            x[j] = -1
print(figurinhasFaltando)
