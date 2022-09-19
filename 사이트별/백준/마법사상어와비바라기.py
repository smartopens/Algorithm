from collections import deque

n, m = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(m)]
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
total_water = 0

for di, dist in orders:
    di -= 1
    new_clouds = set()

    while clouds:
        nr, nc = clouds.popleft()
        nr = (nr+dr[di]*dist)%n
        nc = (nc+dc[di]*dist)%n
        new_clouds.add((nr, nc))

    cloud_vi = [[0] * n for _ in range(n)]
    for r, c in new_clouds:
        baskets[r][c] += 1
        cloud_vi[r][c] = 1

    for r, c in new_clouds:
        basket_num = 0

        for di in [1,3,5,7]:
            nr, nc = r + dr[di], c + dc[di]

            if 0 <= nr < n and 0 <= nc < n:
                if baskets[nr][nc] > 0:
                    basket_num += 1

        baskets[r][c] += basket_num
    for r in range(n):
        for c in range(n):
            if baskets[r][c] >= 2 and cloud_vi[r][c] == 0:

                baskets[r][c] -= 2
                if baskets[r][c] < 0:
                    baskets[r][c] = 0

                clouds.append((r, c))


for b in baskets:
    total_water += sum(b)
print(total_water)