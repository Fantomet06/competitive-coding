def main():
    N, M = map(int, input().split())

    word1 = str(input())
    word2 = str(input())

    l1 = list(word1)
    #l2 = list(word2)

    for i in range(N):
        try:
            check = str(l1[i]+l1[i+1]+l1[i+2])
            if check not in word2:
                print(check)
                break

            for x in range(N):
                check = str(l1[x]+l1[x+1])
                if check not in word2:
                    print(check)
                    break
        except:
            print("ingen")

main()


