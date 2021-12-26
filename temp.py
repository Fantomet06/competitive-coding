numbers = [1, 3, 5, 6]

print(numbers[-1])

for i in range(len(numbers)):
    try:
        if numbers[i] != numbers[i-1] and numbers[i] != numbers[i+1]:
            print("hello world")
    except:
        print("failed")