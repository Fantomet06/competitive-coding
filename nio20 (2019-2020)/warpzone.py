N = int(input())
list = []

for i in range(N-1):
    a,b,c = map(int, input().split())
    insert = [a, b, c]
    insert.sort()
    list.append(insert)

y = 0
jumps = 1

run = True

for i in list:
    if N in list:
        print(i)
        
print(jumps)