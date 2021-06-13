n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
result = 0

for i in range(1, len(array) + 1):
    sum = abs(i - array[i - 1])
    result += sum

print(result)
