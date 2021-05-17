n, c = list(map(int, input().split()))
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array)

start = 1
end = array[-1] - array[0]
result = 0

while (end >= start):
    mid = (end + start) // 2
    num = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= num + mid:
            num = array[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
