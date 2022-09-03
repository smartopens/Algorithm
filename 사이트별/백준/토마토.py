from collections import deque

m, n, h = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
vi = [[[0] * m for _ in range(n)] for _ in range(h)]
young_tomato = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = -1

for i in tomatos:
    for j in i:
        young_tomato += j.count(0)


def bfs():
    global young_tomato, ans

    q = deque([])
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatos[k][i][j] == 1:
                    q.append((k, i, j, 0))

    while q:
        k, r, c, day = q.popleft()

        if young_tomato <= 0:
            for i in vi:
                for j in i:
                    ans = max(ans, max(j))

            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if tomatos[k][nr][nc] == 0 and not vi[k][nr][nc]:
                    vi[k][nr][nc] = vi[k][r][c] + 1
                    young_tomato -= 1
                    q.append((k, nr, nc, day + 1))

        for i in [-1, 1]:
            nk = k + i
            if 0 <= nk < h and not vi[nk][r][c]:
                if tomatos[nk][r][c] == 0:
                    vi[nk][r][c] = vi[k][r][c] + 1
                    young_tomato -= 1
                    q.append((nk, r, c, day + 1))

    return

bfs()
print(ans)
