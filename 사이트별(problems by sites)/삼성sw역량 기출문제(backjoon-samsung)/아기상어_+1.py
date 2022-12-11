import sys
from collections import deque
import sys

n = int(input())
bsize = 2
beat = 0
sea = [list(map(int, input().split())) for _ in range(n)]
br, bc = 0, 0
ans = 0


def makeTrack(foodFish, d1, br, bc):
    global bsize, ans

    track = []
    di = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while foodFish:
        tr, tc = foodFish.popleft()
        vi = [[0] * n for _ in range(n)]
        vi[br][bc] = 1
        q = deque([(br, bc, 0)])

        while q:
            r, c, d2 = q.popleft()
            if r == tr and c == tc:
                if d2 <= d1:
                    if d2 < d1:
                        d1 = d2
                        track = [(r, c)]
                    elif d2 == d1:
                        track.append((r, c))

            for dr, dc in di:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not vi[nr][nc]:
                    if sea[nr][nc] <= bsize:
                        vi[nr][nc] = 1
                        q.append((nr, nc, d2 + 1))

    """
    if track:
        track.sort()
        d1 = track[0][0]

        for t in track:
            if t[0] == d1:
                t2.append((t[1],t[2]))


    """
    ans += d1
    return track


def trackFish(foodFish):
    global beat, bsize, br, bc

    track = makeTrack(foodFish, sys.maxsize, br, bc)
    if not track:
        return False

    track.sort()

    tr2, tc2 = track[0][0], track[0][1]
    sea[tr2][tc2] = 0
    sea[br][bc] = 0
    beat += 1
    br = tr2
    bc = tc2

    if bsize <= beat:
        bsize += 1
        beat = 0

    return True


def findFish():
    global br, bc

    foodFish = deque([])

    for r in range(n):
        for c in range(n):
            if sea[r][c] < bsize and sea[r][c] != 0:
                foodFish.append((r, c))
            if sea[r][c] == 9:
                br, bc = r, c

    return foodFish


while True:
    foodFish = findFish()

    if foodFish:
        isOk = trackFish(foodFish)
    else:
        break

    if not isOk:
        break

print(ans)



