from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
vi = [[0]*n for _ in range(n)]
can_win = False
dr = [1,0]
dc = [0,1]

def dfs(r,c):
    global can_win

    if r == n-1 and c == n-1:
        can_win = True
        return

    s = area[r][c]
    vi[r][c] = 1

    for i in range(2):
        nr, nc = r + dr[i]*s, c + dc[i]*s

        if 0 <= nr < n and 0 <= nc < n:
            if not vi[nr][nc]:
                dfs(nr,nc)

dfs(0,0)

if can_win:
    print("HaruHaru")
else:
    print("Hing")