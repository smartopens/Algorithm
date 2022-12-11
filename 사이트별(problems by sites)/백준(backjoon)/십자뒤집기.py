import sys
from copy import deepcopy
sys.setrecursionlimit(10**5)

p = int(input())
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def dfs(cnt,is_done,state,board):
    global answer,target_str,vi
    is_ok = True

    if state == target_str:
        print(cnt,answer)
        if cnt < answer:
            answer = cnt
        return

    print(vi,target_str,state)
    for r in range(3):
        for c in range(3):
            state_str = ""
            ori_board = [x[:] for x in board]

            for i in range(5):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < 3 and 0 <= nc < 3:
                    if ori_board[nr][nc] == ".":
                        ori_board[nr][nc] = "*"
                    else:
                        ori_board[nr][nc] = "."

            for r in range(3):
                for c in range(3):
                    state_str += ori_board[r][c]

            if state_str not in vi:
                vi.add(state_str)
                dfs(cnt + 1,is_done,state_str,ori_board)
    return


for _ in range(p):
    answer = 1e9
    board = [["."] * 3 for _ in range(3)]
    vi = set()
    target = [list(map(str, input().strip())) for _ in range(3)]
    target_str = ""

    for r in range(3):
        for c in range(3):
            target_str += target[r][c]

    dfs(0,False,"",board)

    print(answer)
