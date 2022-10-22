n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sr,sc = n//2, n//2
s = 1
answer = 0
is_done = False

# 10,7,1,2,5,10,7,1,2
dr0 = [-1,-1,-1,-2,0,1,1,1,2]
dc0 = [-1,0,1,0,-2,-1,0,1,0]

# 10,7,1,2,5,10,7,1,2
dr1 = [1,0,-1,0,2,1,0,-1,0]
dc1 = [-1,-1,-1,-2,0,1,1,1,2]

# 1,7,10,2,5,1,7,10,2
dr2 = [-1,-1,-1,-2,0,1,1,1,2]
dc2 = [-1,0,1,0,2,-1,0,1,0]

# 1,7,10,2,5,1,7,10,2
dr3 = [1,0,-1,0,-2,1,0,-1,0]
dc3 = [-1,-1,-1,-2,0,1,1,1,2]

res1 = [10,7,1,2,5,10,7,1,2]
res2 = [1,7,10,2,5,1,7,10,2]

while True:

    for _ in range(s):
        if sr == 0 and sc == 0:
            is_done=True
            break
        sr,sc = sr, sc -1
        total_sand = board[sr][sc]
        one = int(total_sand * 0.01)
        two = int(total_sand * 0.02)
        five = int(total_sand * 0.05)
        seven = int(total_sand * 0.07)
        ten = int(total_sand * 0.1)
        rest = total_sand - 2 * one - 2 * two - five - 2 * seven - 2 * ten
        d = 0
        if d == 0:
            in_sand = 0
            for i in range(9):
                nr, nc = sr + dr0[i], sc + dc0[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if res1[i] == 10:
                        board[nr][nc] += ten
                        in_sand += ten
                    elif res1[i] == 7:
                        board[nr][nc] += seven
                        in_sand += seven
                    elif res1[i] == 1:
                        board[nr][nc] += one
                        in_sand += one
                    elif res1[i] == 2:
                        board[nr][nc] += two
                        in_sand += two
                    elif res1[i] == 5:
                        board[nr][nc] += five
                        in_sand += five

            if 0 <= sr < n and 0 <= sc - 1 < n:
                board[sr][sc-1] += rest
                in_sand += rest
            answer += (total_sand - in_sand)
            board[sr][sc] = 0

    if is_done:
        break
    for _ in range(s):
        sr, sc = sr+1, sc
        total_sand = board[sr][sc]
        one = int(total_sand * 0.01)
        two = int(total_sand * 0.02)
        five = int(total_sand * 0.05)
        seven = int(total_sand * 0.07)
        ten = int(total_sand * 0.1)
        rest = total_sand - 2 * one - 2 * two - five - 2 * seven - 2 * ten
        d = 1
        if d == 1:
            in_sand = 0
            for i in range(9):
                nr, nc = sr + dr1[i], sc + dc1[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if res1[i] == 10:
                        board[nr][nc] += ten
                        in_sand += ten
                    elif res1[i] == 7:
                        board[nr][nc] += seven
                        in_sand += seven
                    elif res1[i] == 1:
                        board[nr][nc] += one
                        in_sand += one
                    elif res1[i] == 2:
                        board[nr][nc] += two
                        in_sand += two
                    elif res1[i] == 5:
                        board[nr][nc] += five
                        in_sand += five

            if 0 <= sr+1 < n and 0 <= sc < n:
                board[sr+1][sc] += rest
                in_sand += rest
            answer += (total_sand - in_sand)
            board[sr][sc] = 0

    s += 1
    for _ in range(s):
        sr, sc = sr, sc + 1
        total_sand = board[sr][sc]
        one = int(total_sand * 0.01)
        two = int(total_sand * 0.02)
        five = int(total_sand * 0.05)
        seven = int(total_sand * 0.07)
        ten = int(total_sand * 0.1)
        rest = total_sand - 2 * one - 2 * two - five - 2 * seven - 2 * ten
        d = 2
        if d == 2:
            in_sand = 0
            for i in range(9):
                nr, nc = sr + dr2[i], sc + dc2[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if res2[i] == 10:
                        board[nr][nc] += ten
                        in_sand += ten
                    elif res2[i] == 7:
                        board[nr][nc] += seven
                        in_sand += seven
                    elif res2[i] == 1:
                        board[nr][nc] += one
                        in_sand += one
                    elif res2[i] == 2:
                        board[nr][nc] += two
                        in_sand += two
                    elif res2[i] == 5:
                        board[nr][nc] += five
                        in_sand += five

            if 0 <= sr < n and 0 <= sc + 1 < n:
                board[sr][sc+1] += rest
                in_sand += rest

            answer += (total_sand - in_sand)
            board[sr][sc] = 0

    for _ in range(s):
        sr, sc = sr-1, sc
        total_sand = board[sr][sc]
        one = int(total_sand * 0.01)
        two = int(total_sand * 0.02)
        five = int(total_sand * 0.05)
        seven = int(total_sand * 0.07)
        ten = int(total_sand * 0.1)
        rest = total_sand - 2 * one - 2 * two - five - 2 * seven - 2 * ten
        d = 3
        if d == 3:
            in_sand = 0
            for i in range(9):
                nr, nc = sr + dr3[i], sc + dc3[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if res2[i] == 10:
                        board[nr][nc] += ten
                        in_sand += ten
                    elif res2[i] == 7:
                        board[nr][nc] += seven
                        in_sand += seven
                    elif res2[i] == 1:
                        board[nr][nc] += one
                        in_sand += one
                    elif res2[i] == 2:
                        board[nr][nc] += two
                        in_sand += two
                    elif res2[i] == 5:
                        board[nr][nc] += five
                        in_sand += five

            if 0 <= sr-1 < n and 0 <= sc < n:
                board[sr-1][sc] += rest
                in_sand += rest

            answer += (total_sand - in_sand)
            board[sr][sc] = 0

    s += 1

print(answer)
