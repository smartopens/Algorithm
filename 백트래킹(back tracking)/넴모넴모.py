import sys
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())
possible_set = set()
board = [[0]*(m+1) for _ in range(n+1)]
answer = 0
places = []

for r in range(n):
    for c in range(m):
        places.append((r,c))

places_len = len(places)

def dfs(idx):
    global answer

    if idx == places_len:
        answer += 1
        return

    r,c = places[idx]
    dfs(idx+1)

    if board[r][c-1] == 0 or board[r-1][c-1] == 0 or board[r-1][c] == 0:
        board[r][c] = 1
        dfs(idx + 1)
        board[r][c] = 0

dfs(0)
print(answer)