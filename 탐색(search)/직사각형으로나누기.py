t = int(input())

dp = [0] * (101)
for i in range(1, 4):
    dp[i] = 1

dp[4] = dp[1] + dp[3]
dp[5] = dp[4]

for i in range(6, 8):
    dp[i] = dp[i - 1] + dp[1]

for _ in range(t):
    n = int(input())
    if n >= 8:
        for i in range(8, n + 1):
            dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[n])
