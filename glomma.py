"""
import sys
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_number(): return sys.stdin.readline()
def get_ints(): return map(int, sys.stdin.readline().strip().split())"""

H = []

N,K,X = map(int, input().split())

for i in range(N):
    H.append(int(input()))


H.sort()
lenght = 0

returns = int(N/K)

for i in range(len(H)): 
    lenght += H[i]

for i in range(returns):
    try:
        lenght += H[i]
    except:
        break

lenght = lenght - ((returns*X)*2)

if returns == 1:
    lenght = int(lenght/2)

print(int(lenght))

