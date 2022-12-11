import sys

sys.setrecursionlimit(100000)

test_case = int(input())


def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)

    for i in array[v]:
        if not (visited[i]):
            dfs(i)
        else:
            if i in cycle:
                result.extend(cycle[cycle.index(i):])


for _ in range(test_case):
    n = int(input())
    array = [[] for _ in range(n + 1)]
    info = list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        array[i].append(info[i - 1])

    for i in range(1, n + 1):
        if not (visited[i]):
            cycle = []
            dfs(i)

    print(n - len(result))