n = int(input())

area = [[False] * (100) for _ in range(100)]
result = 0

for _ in range(n):
    x, y = map(int, input().split(' '))

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            area[i][j] = True

for i in range(100):
    for j in range(100):
        if area[i][j] == True:
            result += 1

print(result)
