n = int(input())

arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(n - 1):
    temp = max(dp[i] + arr[i + 1], arr[i + 1])
    dp.append(temp)

print(max(dp))
