import sys

sys.setrecursionlimit(100000)

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def promising(x, y):
    promised = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행, 열 판단
    for i in range(9):
        if sudoku[x][i] in promised:
            promised.remove(sudoku[x][i])
        if sudoku[i][y] in promised:
            promised.remove(sudoku[i][y])
    x = x // 3
    y = y // 3
    # 3*3 네모 칸 판단
    for i in range(3 * x, 3 * (x + 1)):
        for j in range(3 * y, 3 * (y + 1)):
            if sudoku[i][j] in promised:
                promised.remove(sudoku[i][j])

    return promised


def dfs(x):
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        sys.exit(0)
    else:
        (i, j) = zeros[x]
        # 가능한 좌표 판단
        promise = promising(i, j)

        for num in promise:
            sudoku[i][j] = num
            dfs(x + 1)
            sudoku[i][j] = 0


dfs(0)
