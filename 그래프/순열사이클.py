import sys

sys.setrecursionlimit(100000)

test_case = int(input())


def dfs(v):
    visited[v] = True

    for i in array[v]:
        if not (visited[i]):
            dfs(i)


for _ in range(test_case):
    n = int(input())

    nums = list(map(int, input().split(' ')))
    array = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for x in range(1, n + 1):
        array[x].append(nums[x - 1])

    count = 0

    for i in range(1, n + 1):
        if not (visited[i]):
            dfs(i)
            count += 1
    print(count)
