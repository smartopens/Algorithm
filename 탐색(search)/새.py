num = int(input())
sum = 0
result = 0
bird = 0

while num > 0:
    while num >= sum:
        bird = bird + 1
        sum = sum + bird
        result = result + 1

    sum = sum - bird
    result = result - 1
    num = num - sum
    bird = 0
    sum = 0

print(result)
