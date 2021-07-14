n = int(input())


def dfs(v, s, v_arr, result):
    global f_result

    if len(v_arr) == n:
        if array[v][s] != 0:
            f_result = min(f_result, result + array[v][s])
        return

    for i in range(n):
        if array[v][i] != 0 and i not in v_arr:
            v_arr.append(i)
            dfs(i, s, v_arr, result + array[v][i])
            v_arr.pop()


array = [0] * n
for i in range(n):
    array[i] = (list(map(int, input().split(' '))))

visited = [False] * n
f_result = 10000000
result = 0
v_arr = [0]

for i in range(n):
    v_arr[0] = i
    dfs(i, i, v_arr, result)

print(f_result)
