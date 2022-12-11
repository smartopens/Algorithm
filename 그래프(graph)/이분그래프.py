from collections import deque

test_case = int(input())


def bfs(v):
    q = deque([v])
    bi[v] = 1

    while q:
        v = q.popleft()

        for i in array[v]:

            if bi[i] == 0:
                bi[i] = -bi[v]
                q.append(i)
            else:
                if bi[i] == bi[v]:
                    return False
    return True


for _ in range(test_case):
    v, e = map(int, input().split(' '))

    array = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split(' '))
        array[x].append(y)
        array[y].append(x)

    bi = [0] * (v + 1)
    IsTrue = True

    for i in range(1, v + 1):
        if bi[i] == 0:
            if not (bfs(i)):
                IsTrue = False
                break

    print("YES" if IsTrue else "NO")
