import sys

input = sys.stdin.readline

array = list(input().strip())
result = -1
ans = 0

for i in array:
    ans += int(i)

array.sort(reverse=True)

if ans % 3 != 0 or '0' not in array:
    print(-1)
else:
    print(''.join(array))
