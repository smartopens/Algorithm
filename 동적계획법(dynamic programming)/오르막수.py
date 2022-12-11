n = int(input())
dp = [[0] * 10 for _ in range(n)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

result = 0

for i in range(10):
    result += dp[n - 1][i]

print(result % 10007)