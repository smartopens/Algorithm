from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s,e):
    q = deque([(s,0)])
    total_cnt = 0
    vi = [0]*(n+1)
    vi[s] = 1

    while q:
        v, cnt = q.popleft()
        if v == e:
            total_cnt = cnt
            break

        for i in graph[v]:
            if vi[i] == 0:
                vi[i] = 1
                q.append((i,cnt+1))

    if total_cnt == 0:
        return -1
    return total_cnt

print(bfs(start,end))