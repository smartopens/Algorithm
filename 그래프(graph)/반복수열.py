import sys
sys.setrecursionlimit(100000)

a, p = map(int, input().split())
a_arr = list(map(int, str(a).strip()))
array = [a]

while True:
    num = 0

    for i in range(len(a_arr)):
        num += a_arr[i] ** p
    a_arr = list(map(int, str(num).strip()))

    if num in array:
        break
    else:
        array.append(num)

result = []
for i in array:
    if i == num:
        break
    result.append(i)

print(len(result))