def main():
    N, M = map(int, input().split())

    word1 = str(input())
    word2 = str(input())

    l1 = list(word1)
    l2 = []
    for y in range(N):
        for i in range(N):
            try:
                check = [l1[x+y] for x in range(i+1)]
            except:
                pass
            check2 = "".join(str(item) for item in check)
            if check2 not in word2:
                l2.append(check2)
            

    
    if len(l2) == 0:
        print("ingen")
    else:
        a = min(l2, key=len)
        print(a)
main()

