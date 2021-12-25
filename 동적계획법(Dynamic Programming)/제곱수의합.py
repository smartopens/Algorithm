from math import sqrt
n = int(input())
n_s = int(sqrt(n))
pow_nums = []
dp = [0 for _ in range(n+1)]

for i in range(1,n_s+1):
    pow_nums.append(pow(i,2))

for i in range(1,n+1):
    dp_prev = []
    for j in pow_nums:
        if i < j:
            break
        dp_prev.append(dp[i-j])
    dp[i] = (min(dp_prev) + 1)

print(dp[n])
