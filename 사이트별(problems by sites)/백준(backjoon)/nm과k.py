from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
answer = -1000000
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(idx,num_sum):
    global answer

    if idx >= k:
        if num_sum > answer:
            answer = num_sum
        return

    for r in range(n):
        for c in range(m):
            if vi[r][c] == 0:
                is_ok = True

                for i in range(4):
                    if 0 <= r + dr[i] < n and 0 <= c + dc[i] < m:
                        if vi[r+dr[i]][c+dc[i]] == 1:
                            is_ok = False
                            break

                if is_ok:
                    vi[r][c] = 1
                    dfs(idx+1,num_sum+board[r][c])
                    vi[r][c] = 0

    return

dfs(0,0)
print(answer)