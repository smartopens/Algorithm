t = int(input())

for t_c in range(t):

    is_sdoku = True
    board = [list(map(int, input().split())) for _ in range(9)]
    # 가로 판단
    for i in range(9):
        num_set = set()

        for j in range(9):
            if board[i][j] not in num_set:
                num_set.add(board[i][j])
            else:
                is_sdoku = False
                break

        if not is_sdoku:
            break

    # 세로 판단
    for i in range(9):
        num_set = set()

        for j in range(9):
            if board[j][i] not in num_set:
                num_set.add(board[j][i])
            else:
                is_sdoku = False
                break

        if not is_sdoku:
            break

    # 사각형 판단
    for si in range(0, 9, 3):
        for sj in range(0, 9, 3):
            num_set = set()
            for i in range(3):
                for j in range(3):
                    if board[si + i][sj + j] not in num_set:
                        num_set.add(board[si + i][sj + j])
                    else:
                        is_sdoku = False
                        break

                if not is_sdoku: break
            if not is_sdoku: break
        if not is_sdoku: break

    if is_sdoku:
        print("#{} {}".format(t_c+1,1))
    else:
        print("#{} {}".format(t_c+1,0))