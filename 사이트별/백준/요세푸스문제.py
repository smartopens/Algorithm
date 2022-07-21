n, k = map(int, input().split())

array = list(range(1, n + 1))
idx = -1
vi = [0] * (n + 1)
ans = []
m = n
tmp = k

while m > 0:
    idx += 1
    if idx >= n:
        idx = 0

    if vi[idx] == 0:
        tmp -= 1

        if tmp <= 0:
            ans.append(array[idx])
            vi[idx] = 1
            tmp = k
            m -= 1

print("<", end = '')
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end='')
        continue

    print(ans[i], end = ', ')
print(">", end = '')