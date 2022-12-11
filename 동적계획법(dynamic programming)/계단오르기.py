n = int(input())
w = [0]

for _ in range(n):
    w.append(int(input()))

dp = [0] * (n + 1)
dp[1] = w[1]
if n > 1:
    dp[2] = w[1] + w[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + w[i] + w[i - 1], dp[i - 2] + w[i])

print(dp[n])