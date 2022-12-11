test = int(input())

for _ in range(test):
    n = int(input())
    s = []
    dp = []
    for _ in range(2):
        s.append(list(map(int, input().split(' '))))
    s[0][1] += s[1][0]
    s[1][1] += s[0][0]

    for i in range(2, n):
        s[0][i] = max(s[1][i - 1] + s[0][i], s[1][i - 2] + s[0][i])
        s[1][i] = max(s[0][i - 1] + s[1][i], s[0][i - 2] + s[1][i])

    print(max(s[0][n - 1], s[1][n - 1]))
