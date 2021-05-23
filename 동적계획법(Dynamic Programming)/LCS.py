n = input()
m = input()

a = len(n)
b = len(m)

dp = [[0] * (a + 1) for _ in range(b + 1)]

for i in range(1, b + 1):
    for j in range(1, a + 1):
        if m[i - 1] == n[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[b][a])
