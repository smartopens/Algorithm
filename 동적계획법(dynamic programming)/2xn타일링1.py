n = int(input())

dp = [0 for _ in range(n+1)]

if n < 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n]%10007)