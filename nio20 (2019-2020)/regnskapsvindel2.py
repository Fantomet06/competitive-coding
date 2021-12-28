def main():
    N = int(input())

    list = [] * N
    nlist = []
    remove = 0
    isNegative = 0

    for i in range(N):
        list[i] = int(input())

    for i in range(N):
        o = list[i]
        isNegative += o
        if isNegative < 0:
            nlist.append(o)
            x = min(nlist)
            isNegative -= x
            nlist.pop(nlist.index(x))
            remove += 1
        else:
            nlist.append(o)

    print(remove)

main()