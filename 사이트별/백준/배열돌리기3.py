from collections import deque

n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

def convert_array(order_num, target_array):
    global n,m

    if order_num == 1:
        new_array = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_array[n-i-1][j] =target_array[i][j]

        return new_array

    elif order_num == 2:
        new_array = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_array[i][m-j-1] =target_array[i][j]

        return new_array
    elif order_num == 3:
        new_array = [[0]*n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                new_array[j][n-i-1] =target_array[i][j]

        n,m = m,n

        return new_array

    elif order_num == 4:
        new_array = [[0]*n for _ in range(m)]

        for i in range(n):
            for j in range(m-1,-1,-1):
                new_array[m-1-j][i] =target_array[i][j]
        n,m = m,n
        return new_array

    elif order_num == 5:
        new_array = [[0]*m for _ in range(n)]
        one_tmp = deque([])

        for i in range(n//2):
            for j in range(m//2):
                new_array[i][j+m//2] =target_array[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                new_array[i+n//2][j] =target_array[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                new_array[i][j-m//2] =target_array[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                new_array[i-n//2][j] =target_array[i][j]

        return new_array
    elif order_num == 6:
        new_array = [[0]*m for _ in range(n)]
        one_tmp = deque([])

        for i in range(n//2):
            for j in range(m//2):
                new_array[i][j] =target_array[i][j+m//2]
        for i in range(n//2):
            for j in range(m//2,m):
                new_array[i][j] =target_array[i+n//2][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                new_array[i][j] =target_array[i][j-m//2]
        for i in range(n//2,n):
            for j in range(m//2):
                new_array[i][j] =target_array[i-n//2][j]

        return new_array

from copy import deepcopy

for order in orders:
    n_array = convert_array(order, array)
    array = deepcopy(n_array)


for i in range(n):
    for j in range(m):
        print(array[i][j], end = ' ')
    print()