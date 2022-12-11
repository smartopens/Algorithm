arr = list(map(int, input().split()))
dp = [x for x in arr]
n = len(arr)
j_list = []

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[j])

print(max(dp))