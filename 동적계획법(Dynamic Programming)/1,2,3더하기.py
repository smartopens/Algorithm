test_case = int(input())

for _ in range(test_case):
    n = int(input())

    dp = [0 for _ in range(n + 3)]

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n > 3:
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])
