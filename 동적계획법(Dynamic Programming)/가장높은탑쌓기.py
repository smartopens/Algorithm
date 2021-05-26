n = int(input())

array = [(0, 0, 0, 0)]

for i in range(1, n + 1):
    width, height, weight = map(int, input().split())
    array.append((i, width, height, weight))

array.sort(key=lambda x: x[3])
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(0, i):

        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])

max_height = max(dp)
result = []

index = n

while index != 0:

    if dp[index] == max_height:
        result.append(array[index][0])
        max_height -= array[index][1]
    else:
        index -= 1

result.reverse()

print(len(result))

for i in result:
    print(i)