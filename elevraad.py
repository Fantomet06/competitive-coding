numbers = []
N = int(input('N '))

for i in range(N):
  numbers.append(int(input()))

numbers.sort()

for i in range(len(numbers)):
  try:
    if numbers[i] != numbers[i+1] and numbers[i] != numbers[i-1]:
        print(numbers(i))
        break
  except:
    try:
        if numbers[i] != numbers[i+1]:
            print(numbers[i])
            break
    except:
        if numbers[i] != numbers[i-1]:
            print(numbers[i])
            break
        else:
            print(-1)