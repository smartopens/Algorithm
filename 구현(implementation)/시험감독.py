n = int(input())

iList = list(map(int, input().split(' ')))
b, c = map(int, input().split(' '))

index = 0

ansPlus = 0

for num in iList:
    temp = num
    if temp >= b:
        temp -= b
        ansPlus += 1
    else:
        temp = 0
        ansPlus += 1

    if temp > 0:
        if temp % c == 0:
            ansPlus += temp // c
        else:
            ansPlus += (temp // c + 1)

print(ansPlus)