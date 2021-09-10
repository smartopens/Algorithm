n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n
dp = [x for x in arr]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))
