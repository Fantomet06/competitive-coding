N = int(input())
list = []

remove = 0

for i in range(N):
    list.append(int(input()))

isNegative = 0

from itertools import takewhile

#print(sum(1 for _ in takewhile(lambda x: x< 5,list)))

check = []
newCheck = []

for i in range(len(list)):
    isNegative += list[i]
    check = []
    newCheck = []
    if isNegative < 0:
        isNegative -= list[i]
        loop = len(list) - i
        for y in range(loop):
            check.append(list[i+y])
        l = sum(1 for _ in takewhile(lambda x: x< 0,check))
        for r in range(l-1):
            newCheck.append(check[r])
        
        newCheck.sort(reverse=True)
        over = 0
        for j in range(len(newCheck)):
            over += newCheck[j]
            if isNegative - over < 0:
                remove += 1
            elif isNegative - over > 0:
                remove += 1
                

print(remove)