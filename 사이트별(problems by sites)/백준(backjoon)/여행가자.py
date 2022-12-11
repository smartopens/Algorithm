from collections import deque

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
travel_order = list(map(int, input().split()))

def bfs(s_node,d_node):
    vi = [0]*n
    vi[s_node] = 1
    q = deque([s_node])

    while q:
        v = q.popleft()

        if v == d_node:
            return True

        for j in range(n):
            if graph[v][j] == 1 and not vi[j]:
                vi[j] = 1
                q.append(j)

    return False
is_ok = True

for t in range(len(travel_order)-1):
    s,d = travel_order[t]-1, travel_order[t+1]-1
    if not bfs(s,d):
        is_ok = False
        break

if is_ok:
    print("YES")
else:
    print("NO")
