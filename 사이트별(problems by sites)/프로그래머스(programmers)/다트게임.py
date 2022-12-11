import sys
from collections import deque
import sys

n = int(input())
bsize = 2
beat = 0
sea = [list(map(int, input().split( ))) for _ in range(n)]
br, bc = 0,0
ans = 0

foodFish = deque([])

def makeTrack(foodFish,br,bc,d1):
    global bsize, ans

    track = []
    q = deque([br,bc,0])
    di = [(-1,0),(1,0),(0,1),(0,-1)]

    while foodFish:
        tr, tc = foodFish.popleft()
        vi = [[0] * n for _ in range(n)]
        vi[br][bc] = 1

        while q:
            r,c, d2 = q.popleft()

            if r == tr and c ==  tc:
                if d2 <= d1:
                    track.append((r,c))
                    d1 = d2

            for dr,dc in di:
                nr, nc = r + dr, c + dc

                if 0<= nr < n and 0<= nc < n and not vi[nr][nc]:
                    if sea[nr][nc] <= bsize:
                        vi[nr][nc] = 1
                        q.append((nr,nc,d2+1))
    ans += d1

    return track


def trackFish(foodFish, br,bc):
    global beat, bsize

    track = makeTrack(foodFish,br,bc,sys.maxsize)
    track.sort(key = lambda x : x[0])
    tr1, tc1 = track[0][0], track[0][1]
    track2 = []

    for fr, fc in track:
        if tr1 == fr:
            track2.append((fr,fc))

    track2.sort(key=lambda x: x[1])

    tr2, tc2 = track2[0][0], track2[0][1]
    sea[tr2][tc2] = 9
    beat += 1

    if bsize <= beat:
        bsize += 1

    return


def findFish():
    global br,bc

    for r in range(n):
        for c in range(n):
            if sea[r][c] < bsize:
                foodFish.append((r,c))
            if sea[r][c] == 9:
                br,bc = r,c

    return foodFish

while True:
    foodFish = findFish()

    if foodFish:
        trackFish(foodFish, br, bc)
    else:
        break

print(ans)





