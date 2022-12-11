import sys
from collections import deque

n = int(input())
bsize = 2
beat = 0
sea = [list(map(int, input().split( ))) for _ in range(n)]
br, bc = 0,0
ans = 0

for r in range(n):
    for c in range(n):
        if sea[r][c] == 9:
            br, bc = r, c
            break

def bfs(br,bc):
    global bsize, ans

    track = []
    di = [(-1,0),(1,0),(0,1),(0,-1)]
    vi = [[0] * n for _ in range(n)]
    vi[br][bc] = 1
    q = deque([(br, bc, 0)])

    while q:
        r,c, d2 = q.popleft()
        vi[r][c] = 1

        for dr,dc in di:
            nr, nc = r + dr, c + dc

            if 0<= nr < n and 0<= nc < n and not vi[nr][nc]:
                if sea[nr][nc] <= bsize:
                    vi[nr][nc] = 1
                    q.append((nr,nc,d2+1))
                    if sea[nr][nc] < bsize and sea[nr][nc] != 0:
                        track.append((d2+1,nr,nc))

    return track

while True:
    track = bfs(br,bc)

    if not track:
        break

    track.sort()
    ans += track[0][0]
    tr, tc = track[0][1], track[0][2]
    sea[tr][tc] = 9
    sea[br][bc] = 0
    beat += 1
    br = tr
    bc = tc

    if bsize <= beat:
        bsize += 1
        beat = 0

print(ans)



