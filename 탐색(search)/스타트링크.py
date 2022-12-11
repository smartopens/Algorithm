from collections import deque

f, s, g, u, d = map(int, input().split(' '))
visited = [False] * (f + 1)


def bfs():
    q = deque([[s, 0]])
    visited[s] = True

    while q:
        v, cnt = q.popleft()
        if v == g:
            print(cnt)
            return 0
            break
        for nv in [v + u, v - d]:
            if 1 <= nv <= f:
                if not (visited[nv]):
                    visited[nv] = True
                    q.append([nv, cnt + 1])

    return -1


if bfs() == -1:
    print("use the stairs")