n = int(input())
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split(' '))) for _ in range(n)]
ans = 1e9
total = 0
cnt = 0

for i in range(n + 1):
    for j in range(n + 1):
        total += arr[i][j]

def count(x, y, d1, d2):
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    parts = [0] * 5

    for i in range(d1):
        tmp[x + i][y - i] = 5

    for i in range(d2):
        tmp[x + i][y + i] = 5

    for i in range(d2):
        tmp[x + d1 + i][y - d1 + i] = 5

    for i in range(d1+1):
        tmp[x + d2 + i][y + d2 - i] = 5

    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if tmp[i][j] == 5:
                break
            parts[0] += arr[i][j]
            tmp[i][j] = 1

    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if tmp[i][j] == 5:
                break
            parts[1] += arr[i][j]
            tmp[i][j] = 2

    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if tmp[i][j] == 5:
                break
            parts[2] += arr[i][j]
            tmp[i][j] = 3

    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1):
            if tmp[i][j] == 5:
                break
            parts[3] += arr[i][j]
            tmp[i][j] = 4

    parts[4] = total - sum(parts)
    parts.sort()

    return parts[-1] - parts[0]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if x <= n - d1 - d2 and 1 + d1 <= y and y <= n - d2:
                    arrTmp = count(x, y, d1, d2)
                    ans = min(ans, arrTmp)

print(ans)