n = int(input())
array = [0]
for _ in range(n):
    array.append(int(input()))

dp = [0]
dp.append(array[1])

if n > 1:
    dp.append(array[1] + array[2])

for i in range(3, n+1):
    num = max(dp[i-3]+ array[i-1]+array[i], dp[i-2] + array[i], dp[i-1])
    dp.append(num)

print(dp[n])