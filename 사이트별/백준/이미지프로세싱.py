from  collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
orders = [list(map(int, input().split())) for _ in range(q)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc,co,board,ori_c):
    vi = [[0]*m for _ in range(n)]
    vi[sr][sc] = 1
    q = deque([(sr,sc)])
    board[sr][sc] = co

    while q:
        r,c = q.popleft()

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not vi[nr][nc] and board[nr][nc] == ori_c:
                board[nr][nc] = co
                vi[nr][nc] = 1
                q.append((nr,nc))

    return board

for sr,sc,num in orders:
    sr, sc = sr-1,sc-1
    board = bfs(sr,sc,num,board,board[sr][sc])

for r in range(n):
    for c in range(m):
        print(board[r][c],end=' ')
    print()
