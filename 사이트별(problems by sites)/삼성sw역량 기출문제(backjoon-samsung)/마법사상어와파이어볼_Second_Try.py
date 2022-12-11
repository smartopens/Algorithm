n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
answer = 0

for _ in range(m):
    r,c,m,s,d = map(int, input().split())
    r,c = r -1, c-1
    board[r][c].append([m,s,d])

for _ in range(k):
    board_tmp = [[[] for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if board[r][c]:
                for fire in board[r][c]:
                    m,s,d = fire
                    ori_s = s
                    s = s % n
                    nr, nc = (r + dr[d]*s)%n, (c + dc[d]*s)%n
                    board_tmp[nr][nc].append([m,ori_s,d])


    board_tmp2 = [x[:] for x in board_tmp]
    for r in range(n):
        for c in range(n):
            if len(board_tmp[r][c]) >= 2:
                fire_m_sum = 0
                fire_s_sum = 0
                fire_len = len(board_tmp[r][c])
                after_even = False
                d_even = 0
                d_n_even = 0

                for fire in board_tmp[r][c]:
                    m,s,d = fire
                    fire_m_sum += m
                    fire_s_sum += s

                    if d % 2 == 0:
                        d_even += 1
                    else:
                        d_n_even += 1

                if d_even > 0 and d_n_even > 0:
                    if fire_m_sum // 5 == 0:
                        board_tmp2[r][c] = []
                    else:
                        board_tmp2[r][c] = [[fire_m_sum // 5,fire_s_sum//fire_len,1],
                                            [fire_m_sum // 5,fire_s_sum//fire_len,3],
                                            [fire_m_sum // 5,fire_s_sum//fire_len,5],
                                            [fire_m_sum // 5,fire_s_sum//fire_len,7]]

                else:
                    if fire_m_sum // 5 == 0:
                        board_tmp2[r][c] = []
                    else:
                        board_tmp2[r][c] = [[fire_m_sum // 5, fire_s_sum // fire_len, 0],
                                            [fire_m_sum // 5, fire_s_sum // fire_len, 2],
                                            [fire_m_sum // 5, fire_s_sum // fire_len, 4],
                                            [fire_m_sum // 5, fire_s_sum // fire_len, 6]]
    board = [x[:] for x in board_tmp2]


for r in range(n):
    for c in range(n):
        if board[r][c]:
            for fire in board[r][c]:
                m,s,d = fire
                answer += m

print(answer)