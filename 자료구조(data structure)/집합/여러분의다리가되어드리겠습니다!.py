from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
groups = []
answer = []
vi = [0]*(n+1)

for _ in range(n-2):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s):
    vi[s] = 1
    nodes = []
    q = deque([s])

    while q:
        v = q.popleft()
        nodes.append(v)

        for n_v in graph[v]:
            if not vi[n_v]:
                q.append(n_v)
                vi[n_v] = 1

    return nodes

for i in range(1,n+1):
    if not vi[i]:
        groups.append(bfs(i))

for nodes in groups:
    answer.append(nodes[0])

for i in range(2):
    if i == 1:
        print(answer[i], end='')
        break

    print(answer[i], end = ' ')