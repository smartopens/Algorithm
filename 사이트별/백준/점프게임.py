import sys
input = sys.stdin.readline

n, k = map(int, input().split())
first_line = list(map(int, input().strip())) + [1]*k
second_line = list(map(int, input().strip())) + [1]*k
first_vi = [0]*(n+k)
second_vi = [0]*(n+k)
player = 0
delete_idx = 0
clear = False

def dfs(player,delete_idx,line):
    global clear
    if player >= n:
        clear = True
        return

    if line == 0:
        for di in [1, -1]:
            next_p = player + di

            if 0 <= next_p and next_p > delete_idx+1:
                if first_vi[next_p] == 0 and first_line[next_p] == 1:
                    first_vi[next_p] = 1
                    dfs(next_p,delete_idx+1,line)
                    first_vi[next_p] = 0

        next_p = player + k
        if 0 <= next_p and next_p > delete_idx + 1:
            if second_vi[next_p] == 0 and second_line[next_p] == 1:
                second_vi[next_p] = 1
                dfs(next_p, delete_idx + 1, 1)
                second_vi[next_p] = 0
    else:

        for di in [1, -1]:
            next_p = player + di

            if 0 <= next_p and next_p > delete_idx+1:
                if second_vi[next_p] == 0 and second_line[next_p] == 1:
                    second_vi[next_p] = 1
                    dfs(next_p,delete_idx+1,line)
                    second_vi[next_p] = 0

        next_p = player + k
        if 0 <= next_p and next_p > delete_idx + 1:
            if first_vi[next_p] == 0 and first_line[next_p] == 1:
                first_vi[next_p] = 1
                dfs(next_p, delete_idx + 1, 0)
                first_vi[next_p] = 0

dfs(0,-1,0)
if clear:
    print(1)
else:
    print(0)
