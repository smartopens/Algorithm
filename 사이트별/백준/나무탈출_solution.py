import sys
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
depth = [0]*(n+1)
vi = [0]*(n+1)
total_move = 0
is_win = False

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vi[1] = 1

def dfs(v,depth):
    vi[v] = 1
    for e in graph[v]:
        if vi[e] == 0:
            depth[e] = depth[v] + 1
            dfs(e,depth)

dfs(1,depth)

for i in range(2, n+1):
    if len(graph[i]) == 1:
        total_move += depth[i]

if total_move % 2 == 1:
    print("Yes")
else:
    print("No")
