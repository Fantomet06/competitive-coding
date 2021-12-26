N = int(input())
list = []

remove = 0

for i in range(N):
    list.append(int(input()))

isNegative = 0

g = len(list)

save = []

for i in range(g):
    isNegative += list[i]
    save.append(isNegative)
    if isNegative < 0:
        remove += 1
        isNegative -= list[i]

print(remove)