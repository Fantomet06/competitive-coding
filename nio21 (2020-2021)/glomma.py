def main():
    H = []
    L = []
    M = []
    lenght = 0

    N,K,X = map(int, input().split())
    for i in range(N):
        M.append(int(input()))

    for i in range(N):
        if M[i] < X:
            L.append(M[i])
        else:
            H.append(M[i])

    L.sort()
    H.sort()

    while len(H) > 0:
        lenght += (H[len(H)-1]-X)*2
        for x in range(K):
            H.pop(len(H)-1)
            if len(H) <= 0:
                break

    while len(L) > 0:
        lenght += (X-L[0])*2
        for x in range(K):
            L.pop(0)
            if len(L) <= 0:
                break

    print(lenght)

main()

"""
l = sum(1 for _ in takewhile(lambda x: x< 50, H))
for r in range(l-1):
    L.append(H[r])
    H.pop(H.index(r))"""