n = int(input())

dp = [0 for _ in range(31)]
dp[2] = 3

for i in range(4, n + 1, 2):
    _sum = 0
    for j in range(2, i-3, 2):
        _sum += 2*dp[j]
    dp[i] = dp[i-2]*3 + _sum + 2
print(dp[n])
