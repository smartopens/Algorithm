from collections import deque
from itertools import combinations

t = int(input())

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    tx, ty = map(int, input().split())
    stores_vi = set()
    stores_vi.add((sx,sy))
    q = deque([(sx,sy)])
    can_go = False

    while q:
        x,y = q.popleft()
        if abs(tx - x) + abs(ty - y) <= 1000:
            print("happy")
            can_go = True
            break

        for store in stores:
            nx, ny = store[0],store[1]

            if abs(nx - x) + abs(ny - y) <= 1000 and (nx,ny) not in stores_vi:
                stores_vi.add((nx,ny))
                q.append((nx,ny))

    if not can_go:
        print("sad")

