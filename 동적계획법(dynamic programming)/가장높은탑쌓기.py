n = int(input())

array = [(0, 0, 0, 0)]

for i in range(1, n + 1):
    width, height, weight = map(int, input().split())
    array.append((i, width, height, weight))

array.sort(key=lambda x: x[3])
dp = [0] * (n)

for i in range(n):
    for j in range(i):
        if array[i+1][1] > array[j+1][1]:
            dp[i] = max(dp[i], dp[j] + array[i+1][2])

max_height = max(dp)
result = []

index = n

while index != 0:

    if dp[index-1] == max_height:
        result.append(array[index][0])
        max_height -= array[index][2]

    else:
        index -= 1

result.reverse()

print(len(result))

for i in result:
    print(i)