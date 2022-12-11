n = int(input())

arr = list(map(int, input().split(' ')))

arr.sort()
ans = 0
plus = 0
for i in range(len(arr)):
    plus = 0
    for j in range(i + 1):
        plus += arr[j]
    ans += plus

print(ans)
