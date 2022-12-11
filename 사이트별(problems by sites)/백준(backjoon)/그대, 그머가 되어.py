from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
vi = [0 for _ in range(n+1)]
answer = 1e9

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s):
    global answer

    vi[s] = 1
    q = deque([(s,0)])

    while q:
        v, cnt = q.popleft()

        if v == b:
            if answer > cnt:
                answer = cnt
            continue

        for e in graph[v]:
            if not vi[e]:
                vi[e] = 1
                q.append((e,cnt+1))

    return

bfs(a)
if answer == 1e9:
    print(-1)
else:
    print(answer)