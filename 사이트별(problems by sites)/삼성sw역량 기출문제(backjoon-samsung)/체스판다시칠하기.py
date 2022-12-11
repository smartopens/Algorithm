n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]
min_answer = 1e9
target_board1 = \
    [["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ]

target_board2 = \
    [["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", 'B'],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ]

for dr in range(n - 7):
    for dc in range(m - 7):
        answer1 = 0
        answer2 = 0

        for r in range(8):
            for c in range(8):
                if board[r + dr][c + dc] != target_board1[r][c]:
                    answer1 += 1

        for r in range(8):
            for c in range(8):
                if board[r + dr][c + dc] != target_board2[r][c]:
                    answer2 += 1

        answer_tmp = min(answer1, answer2)
        if min_answer > answer_tmp:
            min_answer = answer_tmp

print(min_answer)
