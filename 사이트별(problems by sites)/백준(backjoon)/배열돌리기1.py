n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
plus_i = 0

if n < m:
    plus_i = n // 2
else:
    plus_i = m // 2

for i in range(plus_i):
    for _ in range(r):
        tmp = arr[i][i]

        for j in range(i,m-i-1):
            arr[i][j] = arr[i][j+1]
        for j in range(i,n-i-1):
            arr[j][m-i-1] = arr[j+1][m-i-1]
        for j in range(m-i-1,i,-1):
            arr[n-i-1][j] = arr[n-i-1][j-1]
        for j in range(n-i-1,i+1,-1):
            arr[j][i] = arr[j-1][i]

        arr[i+1][i] = tmp

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
