def main():
    N, M = map(int, input().split())

    word1 = str(input())
    word2 = str(input())
    a = 1

    l1 = list(word1)
    #l2 = list(word2)
    for i in range(N):
        check = [l1[x+1] for x in range(i)] 
        check2 = ''.join(str(item) for item in check)
        if check2 not in word2:
            print(check2)
            a += 1
            break

    if a == 1:
        print("ingen")
main()


