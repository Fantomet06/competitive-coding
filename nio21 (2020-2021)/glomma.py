def main():
    H = []
    L = []
    lenght = []

    N,K,X = map(int, input().split())
    for i in range(N):
        p = int(input())
        if p < X:
            L.append(p)
        else:
            H.append(p)
    L.sort(reverse=True)
    H.sort()

    try:
        Hlenght = [(H[x]-X)*2 for x in range(1, len(H)+1, K)]
    except:
        pass

    try:
        Llenght = [(X-L[-x])*2 for x in range(1, len(L)+1, K)]
    except:
        pass
            

    lenght2 = sum(Hlenght) + sum(Llenght)
    print(int(lenght2))

main()