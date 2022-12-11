n = int(input())

array = [[] for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split(' '))
    array[i].extend([x,y])

array.sort(key = lambda x : x[0])
array.sort(key = lambda x : x[1])

last = 0
cnt = 0

for i,j in array:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
