def main():
    n, m = input().split()
    u, v, p = [], [], []
    for i in range(int(m)):
        a, b, c = input().split()
        u.append(a)
        v.append(b)
        p.append(c)
    s = input()
    difPing = diferencaPing(n, m, u, v, p, s, 0, [], [])
    print(f"vai tilas{difPing}")

def diferencaPing(n, m, u, v, p, s, pingAtual, ilhasVisitadas, listaPing):
    ilhaAtual = s
    ilhasVisitadas.append(s)
    for i in range(int(m)):
        print(f"TESTE{ilhasVisitadas}")
        if(u[i] == ilhaAtual and v[i] not in ilhasVisitadas):
            pingAtual += int(p[i])
            ping = diferencaPing(n, m, u, v, p, v[i], pingAtual, ilhasVisitadas, listaPing)
            listaPing.append(ping)
        elif(v[i] == ilhaAtual and u[i] not in ilhasVisitadas):
            pingAtual += int(p[i])
            ping = diferencaPing(n, m, u, v, p, u[i], pingAtual, ilhasVisitadas, listaPing)
            listaPing.append(ping)
        elif(i == int(m) - 1):
            return pingAtual
    print(f"{listaPing}")
    return 0
        
main()
