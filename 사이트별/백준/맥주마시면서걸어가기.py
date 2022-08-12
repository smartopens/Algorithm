from collections import deque
from itertools import combinations

t = int(input())

def bfs(s):
    sx,sy = places[s]
    vi[s] = 1
    q = deque([(sx,sy,1000,vi)])


    while q:
        x,y,d,vi2 = q.popleft()
        if x == tx and y == ty:
            print("happy")
            return

        if (x,y) in plus:
            d = 1000

        for e in graph[s]:
            if vi2[e] == 0:
                nx,ny = places[e]
                cost = abs(x-nx) + abs(y-ny)

                if d >= cost:
                    if cost % 50 == 0:
                        d -= cost
                    else:
                        d -= 50*(cost//50) + 50
                    vi2[e] = 1
                    q.append((nx,ny,d,vi2))
                    vi2[e] = 0
    print("sad")
    return

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    places = deque([])
    graph = [[] for _ in range(n+2)]
    vi = [0]*(n+2)
    places.append((sx,sy))
    plus = set()

    for _ in range(n):
        x, y = map(int, input().split())
        places.append((x,y))
        plus.add((x,y))

    tx, ty = map(int, input().split())
    places.append((tx,ty))

    for com in combinations(range(n+2),2):
        x,y = com
        graph[x].append(y)
        graph[y].append(x)

    bfs(0)