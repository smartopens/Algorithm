import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
t = int(input())

def dfs(v):
    x, y, r = nodes[v][0], nodes[v][1], nodes[v][2]

    for j in range(n):
        if vi[j] == 0:
            nx, ny, nr = nodes[j][0], nodes[j][1], nodes[j][2]

            if ((x - nx)**2 + (y - ny)**2) <= (r + nr)**2:
                vi[j] = 1
                dfs(j)
    return

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n)]
    nodes = []

    for _ in range(n):
        x, y, r = map(int, input().split())
        nodes.append((x, y, r))

    g_num = 0
    vi = [0]*n

    for i in range(n):
        if vi[i] == 0:
            vi[i] = 1
            dfs(i)
            g_num += 1
    print(g_num)