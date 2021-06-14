import sys

n = int(input())
k = int(input())

if k > n:
    print(0)
    sys.exit()

array = list(map(int, input().split(' ')))

array.sort()
distances = []

for i in range(1, n):
    distances.append(array[i] - array[i - 1])

distances.sort(reverse=True)

for i in range(k - 1):
    distances[i] = 0

print(sum(distances))
