from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = [1e9,0]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start,end):
    global tmp
    vi = [0]*(n+1)
    q = deque([[start,0]])

    while q:
        v,cnt = q.popleft()
        vi[v] = 1

        if v == end:
            tmp += cnt
            break

        for i in graph[v]:
            if vi[i] == 0:
                q.append([i,cnt+1])

    return

for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if i == j:
            continue
        bfs(i,j)

    if tmp < ans[0]:
        ans = [tmp,i]

print(ans[1])