t = int(input())

def rotate90(board):
    new_board = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            new_board[r][c] = board[n-c-1][r]

    return new_board

for t_c in range(t):
    n = int(input())
    boards = []
    board1 = [list(map(str, input().split())) for _ in range(n)]
    board2 = rotate90(board1)
    board3 = rotate90(board2)
    board4 = rotate90(board3)

    ans = ""

    for i in range(n):
        tmp_ans = ""
        for j in range(n):
            tmp_ans += board2[i][j]
        tmp_ans += " "
        for j in range(n):
            tmp_ans += board3[i][j]
        tmp_ans += " "
        for j in range(n):
            tmp_ans += board4[i][j]
        ans += (tmp_ans+"\n")

    print("#{}".format(t_c+1))
    print(ans, end = '')